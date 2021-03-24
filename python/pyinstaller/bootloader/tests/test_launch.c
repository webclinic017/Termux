/*
 * ****************************************************************************
 * Copyright (c) 2013-2020, PyInstaller Development Team.
 *
 * Distributed under the terms of the GNU General Public License (version 2
 * or later) with exception for distributing the bootloader.
 *
 * The full license is in the file COPYING.txt, distributed with this software.
 *
 * SPDX-License-Identifier: (GPL-2.0-or-later WITH Bootloader-exception)
 * ****************************************************************************
 */

/* TODO move this code to file  pyi_win32.c. */

/*
 * Functions in this file are windows specific and are mostly related to handle
 * Side-by-Side assembly:
 *
 * https://en.wikipedia.org/wiki/Side-by-side_assembly
 */

#ifdef _WIN32

/* windows.h will use API for WinServer 2003 with SP1 and WinXP with SP2 */
#define _WIN32_WINNT 0x0502

/* TODO: use safe string functions */
#define _CRT_SECURE_NO_WARNINGS 1

#include <windows.h>
#include <commctrl.h> /* InitCommonControls */
#include <stdio.h>    /* _fileno */
#include <io.h>       /* _get_osfhandle */
#include <signal.h>   /* signal */
#include <sddl.h>     /* ConvertStringSecurityDescriptorToSecurityDescriptorW */

/* PyInstaller headers. */
#include "msvc_stdint.h" /* int32_t */
#include "pyi_global.h"  /* PATH_MAX */
#include "pyi_utils.h"
#include "pyi_win32_utils.h"

static HANDLE hCtx = INVALID_HANDLE_VALUE;
static ULONG_PTR actToken;

#ifndef STATUS_SXS_EARLY_DEACTIVATION
    #define STATUS_SXS_EARLY_DEACTIVATION 0xC015000F
#endif

#define ERROR_STRING_MAX 4096
static char errorString[ERROR_STRING_MAX];

/* GetWinErrorString
 *
 * Return a pointer to a null-terminated string containing a textual description of the
 * given error code. If the error code is zero, the result of GetLastError() is used.
 * The text is localized and ANSI-encoded. The caller is not responsible for freeing
 * this pointer.
 *
 * Returns a pointer to statically-allocated storage. Not thread safe.
 */

char * GetWinErrorString(DWORD error_code) {
    wchar_t local_buffer[ERROR_STRING_MAX];
    DWORD result;

    if (error_code == 0) {
        error_code = GetLastError();
    }
    /* Note: Giving 0 to dwLanguageID means MAKELANGID(LANG_NEUTRAL,
     * SUBLANG_NEUTRAL), but we should use SUBLANG_DEFAULT instead of
     * SUBLANG_NEUTRAL. Please see the note written in
     * "Language Identifier Constants and Strings" on MSDN.
     * https://docs.microsoft.com/en-us/windows/desktop/intl/language-identifier-constants-and-strings
     */
    result = FormatMessageW(
        FORMAT_MESSAGE_FROM_SYSTEM, // dwFlags
        NULL,                       // lpSource
        error_code,                 // dwMessageID
        MAKELANGID(LANG_NEUTRAL, SUBLANG_DEFAULT), // dwLanguageID
        local_buffer,               // lpBuffer
        ERROR_STRING_MAX,           // nSize
        NULL                        // Arguments
        );

    if (!result) {
        FATAL_WINERROR("FormatMessageW", "No error messages generated.\n");
        return "PyInstaller: FormatMessageW failed.";
    }
    if (!pyi_win32_utils_to_utf8(errorString,
                                 local_buffer,
                                 ERROR_STRING_MAX)) {
        return "PyInstaller: pyi_win32_utils_to_utf8 failed.";
    }
    return errorString;
}

int
CreateActContext(const char *manifestpath)
{
    wchar_t * manifestpath_w;
    ACTCTXW ctx;
    BOOL activated;
    HANDLE k32;

    HANDLE (WINAPI * CreateActCtx)(PACTCTXW pActCtx);
    BOOL (WINAPI * ActivateActCtx)(HANDLE hActCtx, ULONG_PTR * lpCookie);

    /* Setup activation context */
    VS("LOADER: manifestpath: %s\n", manifestpath);
    manifestpath_w = pyi_win32_utils_from_utf8(NULL, manifestpath, 0);

    k32 = LoadLibraryA("kernel32");
    CreateActCtx = (void*)GetProcAddress(k32, "CreateActCtxW");
    ActivateActCtx = (void*)GetProcAddress(k32, "ActivateActCtx");

    if (!CreateActCtx || !ActivateActCtx) {
        VS("LOADER: Cannot find CreateActCtx/ActivateActCtx exports in kernel32.dll\n");
        return 0;
    }

    ZeroMemory(&ctx, sizeof(ctx));
    ctx.cbSize = sizeof(ACTCTX);
    ctx.lpSource = manifestpath_w;
    ctx.dwFlags = ACTCTX_FLAG_SET_PROCESS_DEFAULT;

    hCtx = CreateActCtx(&ctx);
    free(manifestpath_w);

    if (hCtx != INVALID_HANDLE_VALUE) {
        VS("LOADER: Activation context created\n");
        activated = ActivateActCtx(hCtx, &actToken);

        if (activated) {
            VS("LOADER: Activation context activated\n");
            return 1;
        }
    }

    hCtx = INVALID_HANDLE_VALUE;
    VS("LOADER: Error activating the context: ActivateActCtx: \n%s\n", GetWinErrorString(0));
    return 0;
}

/* Convert a wide string to an ANSI string.
 *
 *  Returns a newly allocated buffer containing the ANSI characters terminated by a null
 *  character. The caller is responsible for freeing this buffer with free().
 *
 *  Returns NULL and logs error reason if encoding fails.
 */

char *
pyi_win32_wcs_to_mbs(const wchar_t *wstr)
{
    DWORD len, ret;
    char * str;

    /* NOTE: setlocale hysterics are not needed on Windows - this function
     *  has an explicit codepage parameter. CP_ACP means "current ANSI codepage"
     *  which is set in the "Language for Non-Unicode Programs" control panel setting. */

    /* Get buffer size by passing NULL and 0 for output arguments */
    len = WideCharToMultiByte(CP_ACP,  /* CodePage */
                              0,       /* dwFlags */
                              wstr,    /* lpWideCharStr */
                              -1,      /* cchWideChar - length in chars */
                              NULL,    /* lpMultiByteStr */
                              0,       /* cbMultiByte - length in bytes */
                              NULL,    /* lpDefaultChar */
                              NULL     /* lpUsedDefaultChar */
                              );

    if (0 == len) {
        FATAL_WINERROR("WideCharToMultiByte", "Failed to get ANSI buffer size.\n");
        return NULL;
    }

    str = (char *)calloc(len + 1, sizeof(char));
    if (str == NULL) {
        FATAL_WINERROR("win32_wcs_to_mbs", "Out of memory.");
        return NULL;
    };

    ret = WideCharToMultiByte(CP_ACP,    /* CodePage */
                              0,         /* dwFlags */
                              wstr,      /* lpWideCharStr */
                              -1,        /* cchWideChar - length in chars */
                              str,       /* lpMultiByteStr */
                              len,       /* cbMultiByte - length in bytes */
                              NULL,      /* lpDefaultChar */
                              NULL       /* lpUsedDefaultChar */
                              );

    if (0 == ret) {
        FATAL_WINERROR("WideCharToMultiByte", "Failed to encode filename as ANSI.\n");
        return NULL;
    }
    return str;
}

/* We shouldn't need to convert ANSI to wchar_t since everything is provided as wchar_t */

/* The following are used to convert the UTF-16 strings provided by Windows
 * into UTF-8 so we can store them in the `char *` variables and fields
 * we use on Linux. Storing them like this is a wart, but storing them as `wchar_t *`
 * and converting back and forth everywhere on Linux/OS X is an even bigger wart
 */

/* Convert elements of wargv to UTF-8 */

char **
pyi_win32_argv_to_utf8(int argc, wchar_t **wargv)
{
    int i, j;
    char ** argv;

    argv = (char **)calloc(argc + 1, sizeof(char *));
    if (argv == NULL) {
        return NULL;
    };

    for (i = 0; i < argc; i++) {
        argv[i] = pyi_win32_utils_to_utf8(NULL, wargv[i], 0);

        if (NULL == argv[i]) {
            goto err;
        }
    }
    argv[argc] = NULL;

    return argv;
err:

    for (j = 0; j <= i; j++) {
        free(argv[j]);
    }
    free(argv);
    return NULL;
}

/* Convert elements of wargv back from UTF-8. Used when calling
 *  PySys_SetArgv on Python 3.
 */

wchar_t **
pyi_win32_wargv_from_utf8(int argc, char **argv)
{
    int i, j;
    wchar_t ** wargv;

    wargv = (wchar_t **)calloc(argc + 1, sizeof(wchar_t *));
    if (wargv == NULL) {
        return NULL;
    };

    for (i = 0; i < argc; i++) {
        wargv[i] = pyi_win32_utils_from_utf8(NULL, argv[i], 0);

        if (NULL == wargv[i]) {
            goto err;
        }
    }
    wargv[argc] = NULL;

    return wargv;
err:

    for (j = 0; j <= i; j++) {
        free(wargv[j]);
    }
    free(wargv);
    return NULL;
}

/*
 * Encode wchar_t (UTF16) into char (UTF8).
 *
 * `wstr` must be null-terminated.
 *
 * If `str` is not NULL, copies the result into the given buffer, which must hold
 * at least `len` bytes. Returns the given buffer if successful. Returns NULL on
 * encoding failure, or if the UTF-8 encoding requires more than `len` bytes.
 *
 * If `str` is NULL, allocates and returns a new buffer to store the result. The
 * `len` argument is ignored. Returns NULL on encoding failure. The caller is
 * responsible for freeing the returned buffer using free().
 *
 */
char *
pyi_win32_utils_to_utf8(char *str, const wchar_t *wstr, size_t len)
{
    char * output;

    if (NULL == str) {
        /* Get buffer size by passing NULL and 0 for output arguments
         * -1 for cchWideChar means string is null-terminated
         */
        len = WideCharToMultiByte(CP_UTF8,              /* CodePage */
                                  0,                    /* dwFlags */
                                  wstr,                 /* lpWideCharStr */
                                  -1,                   /* cchWideChar - length in chars */
                                  NULL,                 /* lpMultiByteStr */
                                  0,                    /* cbMultiByte - length in bytes */
                                  NULL,                 /* lpDefaultChar */
                                  NULL                  /* lpUsedDefaultChar */
                                  );

        if (0 == len) {
            FATAL_WINERROR("WideCharToMultiByte", "Failed to get UTF-8 buffer size.\n");
            return NULL;
        }

        output = (char *)calloc(len + 1, sizeof(char));
        if (output == NULL) {
            FATAL_WINERROR("win32_utils_to_utf8", "Out of memory.");
            return NULL;
        };
    }
    else {
        output = str;
    }

    len = WideCharToMultiByte(CP_UTF8,              /* CodePage */
                              0,                    /* dwFlags */
                              wstr,                 /* lpWideCharStr */
                              -1,                   /* cchWideChar - length in chars */
                              output,               /* lpMultiByteStr */
                              (DWORD)len,           /* cbMultiByte - length in bytes */
                              NULL,                 /* lpDefaultChar */
                              NULL                  /* lpUsedDefaultChar */
                              );

    if (len == 0) {
        FATAL_WINERROR("WideCharToMultiByte",
                       "Failed to encode wchar_t as UTF-8.\n");
        return NULL;
    }
    return output;
}

/*
 * Decode char (UTF8) into wchar_t (UTF16).
 *
 * `str` must be null-terminated.
 *
 * If `wstr` is not NULL, copies the result into the given buffer, which must hold
 * at least `wlen` characters. Returns the given buffer if successful. Returns NULL on
 * encoding failure, or if the UTF-16 encoding requires more than `wlen` characters.
 *
 * If `wstr` is NULL, allocates and returns a new buffer to store the result. The
 * `wlen` argument is ignored. Returns NULL on encoding failure. The caller is
 * responsible for freeing the returned buffer using free().
 */

wchar_t *
pyi_win32_utils_from_utf8(wchar_t *wstr, const char *str, size_t wlen)
{
    wchar_t * output;

    if (NULL == wstr) {
        /* Get buffer size by passing NULL and 0 for output arguments
         * -1 for cbMultiByte means string is null-terminated.
         */
        wlen = MultiByteToWideChar(CP_UTF8,             /* CodePage */
                                   0,                   /* dwFlags */
                                   str,                 /* lpMultiByteStr */
                                   -1,                  /* cbMultiByte - length in bytes */
                                   NULL,                /* lpWideCharStr */
                                   0                    /* cchWideChar - length in chars */
                                   );

        if (0 == wlen) {
            FATAL_WINERROR("MultiByteToWideChar", "Failed to get wchar_t buffer size.\n");
            return NULL;
        }

        output = (wchar_t *)calloc(wlen + 1, sizeof(wchar_t));
        if (output == NULL) {
            FATAL_WINERROR("win32_utils_from_utf8", "Out of memory.");
            return NULL;
        };
    }
    else {
        output = wstr;
    }

    wlen = MultiByteToWideChar(CP_UTF8,              /* CodePage */
                               0,                    /* dwFlags */
                               str,                  /* lpMultiByteStr */
                               -1,                   /* cbMultiByte - length in bytes */
                               output,               /* lpWideCharStr */
                               (DWORD)wlen           /* cchWideChar - length in chars */
                               );

    if (wlen == 0) {
        FATAL_WINERROR("MultiByteToWideChar", "Failed to decode wchar_t from UTF-8\n");
        return NULL;
    }
    return output;
}

/* Convert an UTF-8 string to an ANSI string.
 *
 *  Returns NULL if encoding fails.
 */
char *
pyi_win32_utf8_to_mbs(char * dst, const char * src, size_t max)
{
    wchar_t * wsrc;
    char * mbs;

    wsrc = pyi_win32_utils_from_utf8(NULL, src, 0);

    if (NULL == wsrc) {
        return NULL;
    }

    mbs = pyi_win32_wcs_to_mbs(wsrc);

    free(wsrc);

    if (NULL == mbs) {
        return NULL;
    }

    if (dst) {
        strncpy(dst, mbs, max);
        free(mbs);
        return dst;
    }
    else {
        return mbs;
    }
}

/* Create a directory at path with restricted permissions.
 *  The directory owner will be the only one with permissions on the created
 *  dir. Calling this function is equivalent to callin chmod(path, 0700) on
 *  Posix.
 *  Returns 0 on success, -1 on error.
 */
int
pyi_win32_mkdir(const wchar_t *path)
{
    wchar_t stringSecurityDesc[] = // ACE String :
        L"D:" // DACL (D) :
        L"(A;" // Authorize (A)
        L";FA;" // FILE_ALL_ACCESS (FA)
        L";;S-1-3-4)"; // For the current directory owner (SID: S-1-3-4)
        // no other permissions are granted

    SECURITY_ATTRIBUTES securityAttr;
    PSECURITY_DESCRIPTOR *lpSecurityDesc;
    securityAttr.nLength = sizeof(SECURITY_ATTRIBUTES);
    securityAttr.bInheritHandle = FALSE;
    lpSecurityDesc = &securityAttr.lpSecurityDescriptor;

    if (!ConvertStringSecurityDescriptorToSecurityDescriptorW(
             stringSecurityDesc,
             SDDL_REVISION_1,
             lpSecurityDesc,
             NULL)) {
        return -1;
    }
    if (!CreateDirectoryW(path, &securityAttr)) {
        return -1;
    };
    return 0;
}

#endif  /* _WIN32 */
