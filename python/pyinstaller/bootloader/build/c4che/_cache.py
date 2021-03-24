# -*- mode: python -*- vim: filetype=python
# -----------------------------------------------------------------------------
# Copyright (c) 2014-2020, PyInstaller Development Team.
#
# Distributed under the terms of the GNU General Public License (version 2
# or later) with exception for distributing the bootloader.
#
# The full license is in the file COPYING.txt, distributed with this software.
#
# SPDX-License-Identifier: (GPL-2.0-or-later WITH Bootloader-exception)
# -----------------------------------------------------------------------------


"""
Bootloader building script.
"""

import os
import platform
import sys
import re
import sysconfig
from waflib.Configure import conf
from waflib import Logs, Utils, Options
from waflib.Build import BuildContext, InstallContext

# The following two variables are used by the target "waf dist"
VERSION = 'nodist'
APPNAME = 'PyInstallerBootloader'

# These variables are mandatory ('/' are converted automatically)
top = '.'
out = 'build'

# Build variants of bootloader.
# PyInstaller provides debug/release bootloaders and console/windowed
# variants.
# Every variant has different exe name.
variants = {
    'debug': 'run_d',
    'debugw': 'runw_d',
    'release': 'run',
    'releasew': 'runw',
}

# PyInstaller only knows platform.system(), so we need to
# map waf's DEST_OS to these values.
DESTOS_TO_SYSTEM = {
    'linux': 'Linux',
    'freebsd': 'FreeBSD',
    'openbsd': 'OpenBSD',
    'win32': 'Windows',
    'darwin': 'Darwin',
    'sunos': platform.system(),  ## FIXME: inhibits cross-compile
    'hpux': 'HP-UX',
    'aix': 'AIX',
}

# Map from platform.system() to waf's DEST_OS
SYSTEM_TO_BUILDOS = {
    'Linux': 'linux',
    'FreeBSD': 'freebsd',
    'Windows': 'win32',
    'Darwin': 'darwin',
    'Solaris': 'sunos',
    'SunOS': 'sunos',
    'HP-UX': 'hpux',
    'AIX': 'aix',
}

# waf's name of the system we are building on
BUILD_OS = SYSTEM_TO_BUILDOS.get(platform.system(), platform.system())

is_cross = None


def machine():
    """
    Differenciate path to bootloader with machine name if necessary.

    Machine name in bootloader is necessary only for non-x86 architecture.
    """
    # IMPORTANT: Keep this in line with PyInstaller.compat.machine()
    mach = platform.machine()
    if mach.startswith('arm'):
        return 'arm'
    elif mach.startswith('aarch'):
        return 'aarch'
    else:
        # Assume x86/x86_64 machine.
        return None


def assoc_programm(ctx, name):
    # Search other programs we need, based on the name of the compiler
    # (replace "gcc" or "clang" by the tool name)
    cc = ctx.env.CC[0]
    prog = re.sub(r'(^|^.*-)(gcc|clang)(-.*|\.exe$|$)',
                  r'\1' + name + r'\3',
                  os.path.basename(cc))
    prog = os.path.join(os.path.dirname(cc), prog)
    # waf unconditionally appends the extension even if there is one already.
    # So we need to remove the existing one here.
    exts = Utils.is_win32 and r'\.(exe|com|bat|cmd)$' or r'\.(sh|pl|py)$'
    prog = re.sub(exts, '', prog)
    return prog


def options(ctx):
    ctx.load('compiler_c')

    ctx.add_option('--debug',
                   action='store_true',
                   help='Include debugging info for GDB.',
                   default=False,
                   dest='debug')
    ctx.add_option('--leak-detector',
                   action='store_true',
                   help='Link with Boehm garbage collector to detect memory leaks.',
                   default=False,
                   dest='boehmgc')
    ctx.add_option('--clang',
                   action='store_true',
                   help='Try to find clang C compiler instead of gcc.',
                   default=False,
                   dest='clang')
    ctx.add_option('--gcc',
                   action='store_true',
                   help='Try to find GNU C compiler.',
                   default=False,
                   dest='gcc')
    ctx.add_option('--target-arch',
                   action='store',
                   help='Target architecture format (32bit, 64bit). '
                        'This option allows to build 32bit bootloader with 64bit compiler '
                        'and 64bit Python.',
                   default=None,
                   dest='target_arch')
    ctx.add_option('--show-warnings', action='store_true',
                   help='Make gcc print out the warnings we consider as '
                        'being non-fatal. All other warinings are still '
                        'treated as errors. Mind deleting the `build` '
                        'directory first to ensure all files are actually '
                        'recompiled.',
                   dest='show_warnings')

    grp = ctx.add_option_group('Linux Standard Base (LSB) compliance',
                               'These options have effect only on Linux.')
    grp.add_option('--no-lsb',
                   action='store_true',
                   help=('Build "normal" (non-LSB-compliant) bootloader.'
                         '(this is the default).'),
                   default=True,
                   dest='nolsb')
    grp.add_option('--lsb',
                   action='store_false',
                   help='Build LSB compliant bootloader.',
                   default=True,
                   dest='nolsb')
    grp.add_option('--lsbcc-path',
                   action='store',
                   help='Path where to look for lsbcc. By default PATH is '
                        'searched for lsbcc otherwise is tried file '
                        '/opt/lsb/bin/lsbcc. [Default: lsbcc]',
                   default=None,
                   dest='lsbcc_path')
    grp.add_option('--lsb-target-version',
                   action='store',
                   help='Specify LSB target version [Default: 4.0]',
                   default='4.0',
                   dest='lsb_version')


@conf
def set_lsb_compiler(ctx):
    """
    Build LSB (Linux Standard Base) bootloader.

    LSB bootloader allows to build bootloader binary that is compatible
    with almost every Linux distribution.
    'lsbcc' just wraps gcc in a special way.
    """
    Logs.pprint('CYAN', 'Building LSB (Linux Standard Base) bootloader.')
    lsb_paths = ['/opt/lsb/bin']
    if ctx.options.lsbcc_path:
        lsb_paths.insert(0, ctx.options.lsbcc_path)
    try:
        ctx.find_program('lsbcc', var='LSBCC', path_list=lsb_paths)
    except ctx.errors.ConfigurationError:
        # Fail hard and print warning if lsbcc is not available.
        # if not ctx.env.LSBCC:
        ctx.fatal('LSB (Linux Standard Base) tools >= 4.0 are '
                  'required.\nTry --no-lsb option if not interested in '
                  'building LSB binary.')

    # lsbcc as CC compiler
    ctx.env.append_value('CFLAGS', '--lsb-cc=%s' % ctx.env.CC[0])
    ctx.env.append_value('LINKFLAGS', '--lsb-cc=%s' % ctx.env.CC[0])
    ctx.env.CC = ctx.env.LSBCC
    ctx.env.LINK_CC = ctx.env.LSBCC
    ## check LSBCC flags
    # --lsb-besteffort - binary will work on platforms without LSB stuff
    # --lsb-besteffort - available in LSB build tools >= 4.0
    ctx.check_cc(cflags='--lsb-besteffort',
                 msg='Checking for LSB build tools >= 4.0',
                 errmsg='LSB >= 4.0 is required', mandatory=True)
    ctx.env.append_value('CFLAGS', '--lsb-besteffort')
    ctx.env.append_value('LINKFLAGS', '--lsb-besteffort')
    # binary compatibility with a specific LSB version
    # LSB 4.0 can generate binaries compatible with 3.0, 3.1, 3.2, 4.0
    # however because of using function 'mkdtemp', loader requires
    # using target version 4.0
    lsb_target_flag = '--lsb-target-version=%s' % ctx.options.lsb_version
    ctx.env.append_value('CFLAGS', lsb_target_flag)
    ctx.env.append_value('LINKFLAGS', lsb_target_flag)


def check_sizeof_pointer(ctx):

    def check(type, expected):
        # test code taken from autoconf resp. Scons: this is a pretty clever
        # hack to find that a type is of a given size using only compilation.
        # This speeds things up quite a bit compared to straightforward code
        # actually running the code.
        # Plus: This works cross :-)
        fragment = '''
        int main() {
            static int test_array[1 - 2 * !(sizeof(%s) == %d)];
            test_array[0] = 0;
            return 0;
        }''' % (type, expected)
        return ctx.check_cc(fragment=fragment, execute=False, mandatory=False)

    ctx.start_msg("Checking size of pointer")
    for size in (4, 8):
        if check("void *", size):
            break
    else:
        ctx.end_msg(False)
        ctx.fatal("Couldn't determine pointer size, only 32 or 64 bit are supported. Please use `--target-arch' to set the pointer size.")
    ctx.end_msg(size)
    return size


@conf
def detect_arch(ctx):
    """
    Handle options --target-arch or use the same
    architecture as the compiler.
    """
    try:
        system = DESTOS_TO_SYSTEM[ctx.env.DEST_OS]
    except KeyError:
        ctx.fatal('Unrecognized target system: %s' % ctx.env.DEST_OS)

    # Get arch values either from CLI or detect it.
    if ctx.options.target_arch:
        arch = ctx.options.target_arch
        ctx.msg('Platform', '%s-%s manually chosen' % (system, arch))
        ctx.env.ARCH_FLAGS_REQUIRED = True
    else:
        # PyInstaller uses the result of platform.architecture() to determine
        # the bits and this is testing the pointer size (via module struct).
        # We do the same here.
        arch = "%sbit" % (8 * check_sizeof_pointer(ctx))
        ctx.msg('Platform', '%s-%s detected based on compiler' % (system, arch))
        ctx.env.ARCH_FLAGS_REQUIRED = False
    if not arch in ('32bit','64bit'):
        ctx.fatal('Unrecognized target architecture: %s' % arch)

    # Pass return values as environment variables.
    ctx.env.PYI_ARCH = arch  # '32bit' or '64bit'
    ctx.env.PYI_SYSTEM = system


@conf
def set_arch_flags(ctx):
    """
    Set properly architecture flag (32 or 64 bit) cflags for compiler
    and CPU target for compiler.
    """
    def check_arch_cflag(cflag32, cflag64):
        cflag = cflag32 if ctx.env.PYI_ARCH == '32bit' else cflag64
        if ctx.check_cc(cflags=cflag,
                        features='c', # only compile, don't link
                        mandatory=ctx.env.ARCH_FLAGS_REQUIRED):
            ctx.env.append_value('CFLAGS', cflag)
        if ctx.check_cc(linkflags=cflag,
                        mandatory=ctx.env.ARCH_FLAGS_REQUIRED):
            ctx.env.append_value('LINKFLAGS', cflag)

    if ctx.env.DEST_OS == 'win32' and ctx.env.CC_NAME == 'msvc':
        # Set msvc linkflags based on architecture.
        if ctx.env.PYI_ARCH == '32bit':
            ctx.env['MSVC_TARGETS'] = ['x86']
            ctx.env.append_value('LINKFLAGS', '/MACHINE:X86')
            # Set LARGE_ADDRESS_AWARE_FLAG to True.
            # On Windows this allows 32bit apps to use 4GB of memory and
            ctx.env.append_value('LINKFLAGS', '/LARGEADDRESSAWARE')
        elif ctx.env.PYI_ARCH == '64bit':
            ctx.env['MSVC_TARGETS'] = ['x64']
            ctx.env.append_value('LINKFLAGS', '/MACHINE:X64')

        # Enable 64bit porting warnings and other warnings too.
        ctx.env.append_value('CFLAGS', '/W3')
        # We use SEH exceptions in winmain.c; make sure they are activated.
        ctx.env.append_value('CFLAGS', '/EHa')

    # Ensure proper architecture flags on Mac OS X.
    elif ctx.env.DEST_OS == 'darwin':
        # Default compiler on Mac OS X is Clang.
        # Clang does not have flags '-m32' and '-m64'.
        if ctx.env.PYI_ARCH == '32bit':
            mac_arch = ['-arch', 'i386']
        else:
            mac_arch = ['-arch', 'x86_64']
        ctx.env.append_value('CFLAGS', mac_arch)
        ctx.env.append_value('CXXFLAGS', mac_arch)
        ctx.env.append_value('LINKFLAGS', mac_arch)

    # AIX specific flags
    elif ctx.env.DEST_OS == 'aix':
        if ctx.env.CC_NAME == 'gcc':
            check_arch_cflag('-maix32', '-maix64')
        else:
            # We are using AIX/xlc compiler
            check_arch_cflag('-q32', '-q64')

    elif ctx.env.DEST_OS == 'sunos':
        if ctx.env.CC_NAME == 'gcc':
            check_arch_cflag('-m32', '-m64')
        else:
            # We use SUNWpro C compiler
            check_arch_cflag('-xarch=generic', '-xarch=v9')

    elif ctx.env.DEST_OS == 'hpux':
        if ctx.env.CC_NAME == 'gcc':
            check_arch_cflag('-milp32', '-mlp64')
        else:
            # We use xlc compiler
            pass

    # Other compiler - not msvc.
    else:
        if machine() == 'sw_64':
            # The gcc has no '-m64' option under sw64 machine, but the
            # __x86_64__ macro needs to be defined
            conf.env.append_value('CCDEFINES', '__x86_64__')
        # This ensures proper compilation with 64bit gcc and 32bit Python
        # or vice versa or with manually choosen --target-arch.
        # Option -m32/-m64 has to be passed to cflags and linkflages.
        else:
            check_arch_cflag('-m32', '-m64')
        if ctx.env.PYI_ARCH == '32bit' and ctx.env.DEST_OS == 'win32':
            # Set LARGE_ADDRESS_AWARE_FLAG to True.
            # On Windows this allows 32bit apps to use 4GB of memory and
            # not only 2GB.
            # TODO verify if this option being as default might cause any side
            # effects.
            ctx.env.append_value('LINKFLAGS', '-Wl,--large-address-aware')

    # We need to pass architecture switch to the 'windres' tool.
    if ctx.env.DEST_OS == 'win32' and ctx.env.CC_NAME != 'msvc':
        if ctx.env.PYI_ARCH == '32bit':
            ctx.env.WINRCFLAGS = ['--target=pe-i386']
        else:
            ctx.env.WINRCFLAGS = ['--target=pe-x86-64']
        # Since WINRC config changed above, must set other options as well
        ctx.env.WINRC_TGT_F = '-o'
        ctx.env.WINRC_SRC_F = '-i'


def configure(ctx):
    ctx.msg('Python Version', sys.version.replace(os.linesep, ''))
    # For MSVC the target arch must already been set when the compiler is
    # searched.
    if ctx.options.target_arch == '32bit':
        ctx.env['MSVC_TARGETS'] = ['x86']
    elif ctx.options.target_arch == '64bit':
        ctx.env['MSVC_TARGETS'] = ['x64']

    ### C compiler

    # Allow to use Clang if preferred.
    if ctx.options.clang:
        ctx.load('clang')
    # Allow to use gcc if preferred.
    elif ctx.options.gcc:
        ctx.load('gcc')
    else:
        ctx.load('compiler_c')  # Any available C compiler.

    # LSB compatible bootloader only for Linux and without cli option --no-lsb.
    if ctx.env.DEST_OS == 'linux' and not ctx.options.nolsb:
        ctx.set_lsb_compiler()

    global is_cross
    is_cross = (BUILD_OS != ctx.env.DEST_OS)

    if is_cross:
        ctx.msg('System', 'Assuming cross-compilation for %s' %
                DESTOS_TO_SYSTEM[ctx.env.DEST_OS])

        if ctx.env.DEST_OS in ('freebsd', 'hpux', 'sunos'):
            # For these FreeBSD and HP-UX we determine some settings from
            # Python's sysconfig. For cross-compiling somebody needs to
            # implement options to overwrite these values as they may be
            # wrong.
            # For SunOS/Solaris mappgin DEST_OS to system is not yet known.
            ctx.fatal('Cross-compiling for target %s is not yet supported. '
                      'If you want this feature, please help implementing. '
                      'See the wscript file for details.' % ctx.env.DEST_OS)

    # Detect architecture after completing compiler search
    ctx.detect_arch()

    # Set proper architecture and CPU for C compiler
    ctx.set_arch_flags()

    ### Other Tools

    if ctx.env.DEST_OS == 'win32':
        # Do not embed manifest file when using MSVC (Visual Studio).
        # Manifest file will be added in the phase of packaging python
        # application by PyInstaller.
        ctx.env.MSVC_MANIFEST = False

        if ctx.env.CC_NAME != 'msvc':
            # Load tool to process *.rc* files for C/C++ like icon for exe
            # files. For msvc waf loads this tool automatically
            ctx.find_program([assoc_programm(ctx, 'windres')], var='WINRC')
            ctx.load('winres')

    ### C Compiler optimizations.
    # TODO Set proper optimization flags for MSVC (Visual Studio).

    if ctx.options.debug:
        if ctx.env.DEST_OS == 'win32' and ctx.env.CC_NAME == 'msvc':
            # Include information for debugging in MSVC/msdebug
            ctx.env.append_value('CFLAGS', '/Z7')
            ctx.env.append_value('CFLAGS', '/Od')
            ctx.env.append_value('LINKFLAGS', '/DEBUG')
        else:
            # Include gcc debugging information for debugging in GDB.
            ctx.env.append_value('CFLAGS', '-g')
    else:
        if ctx.env.DEST_OS != 'sunos':
            ctx.env.append_value('CFLAGS', '-O2')
        else:
            # Solaris SUN CC doesn't support '-O2' flag
            ctx.env.append_value('CFLAGS', '-O')

    if ctx.env.CC_NAME == 'gcc':
        # !! These flags are gcc specific
        # Turn on all warnings to improve code quality and avoid
        # errors. Unused variables and unused functions are still
        # accepted to avoid even more conditional code.
        # If you are ever tempted to change this, review the commit
        # history of this place first.
        ctx.env.append_value('CFLAGS', ['-Wall',
                                        '-Werror',
                                        '-Wno-error=unused-variable',
                                        '-Wno-error=unused-function'])
        if not ctx.options.show_warnings:
            ctx.env.append_value('CFLAGS', ['-Wno-unused-variable',
                                            '-Wno-unused-function'])

    ### Defines, Includes

    if not ctx.env.DEST_OS == 'win32':
        # Defines common for Unix and Unix-like platforms.
        # For details see:
        #   http://man.he.net/man7/feature_test_macros
        ctx.env.append_value('DEFINES', '_REENTRANT')

        # mkdtemp() is available only if _BSD_SOURCE is defined.
        ctx.env.append_value('DEFINES', '_BSD_SOURCE')

        if ctx.env.DEST_OS == 'linux':
            # Recent GCC 5.x complains about _BSD_SOURCE under Linux:
            #     _BSD_SOURCE and _SVID_SOURCE are deprecated, use _DEFAULT_SOURCE
            ctx.env.append_value('DEFINES', '_DEFAULT_SOURCE')

            # TODO What other platforms support _FORTIFY_SOURCE macro? OS X?
            # TODO OS X's CLang appears to support this macro as well. See:
            # https://marc.info/?l=cfe-dev&m=122032133830183

            # For security, enable the _FORTIFY_SOURCE macro detecting buffer
            # overflows in various string and memory manipulation functions.
            if ctx.options.debug:
                ctx.env.append_value('CFLAGS', '-U_FORTIFY_SOURCE')
            elif ctx.env.CC_NAME == 'gcc':
                # Undefine this macro if already defined by default to avoid
                # "macro redefinition" errors.
                ctx.env.append_value('CFLAGS', '-U_FORTIFY_SOURCE')

                # Define this macro.
                ctx.env.append_value('DEFINES', '_FORTIFY_SOURCE=2')
        # On Mac OS X, mkdtemp() is available only with _DARWIN_C_SOURCE.
        elif ctx.env.DEST_OS == 'darwin':
            ctx.env.append_value('DEFINES', '_DARWIN_C_SOURCE')

    if ctx.env.DEST_OS == 'win32':
        ctx.env.append_value('DEFINES', 'WIN32')
        ctx.env.append_value('CPPPATH', '../zlib')

    elif ctx.env.DEST_OS == 'sunos':
        ctx.env.append_value('DEFINES', 'SUNOS')
        if ctx.env.CC_NAME == 'gcc':
            # On Solaris using gcc the linker options for shared and static
            # libraries are slightly different from other platforms.
            ctx.env['SHLIB_MARKER'] = '-Wl,-Bdynamic'
            ctx.env['STLIB_MARKER'] = '-Wl,-Bstatic'
            # On Solaris using gcc, the compiler needs to be gnu99
            ctx.env.append_value('CFLAGS', '-std=gnu99')

    elif ctx.env.DEST_OS == 'aix':
        ctx.env.append_value('DEFINES', 'AIX')
        # On AIX some APIs are restricted if _ALL_SOURCE is not defined.
        # In the case of PyInstaller, we need the AIX specific flag RTLD_MEMBER
        # for dlopen() which is used to load a shared object from a library
        # archive. We need to load the Python library like this:
        #  dlopen("libpython2.7.a(libpython2.7.so)", RTLD_MEMBER)
        ctx.env.append_value('DEFINES', '_ALL_SOURCE')

        # On AIX using gcc the linker options for shared and static
        # libraries are slightly different from other platforms.
        ctx.env['SHLIB_MARKER'] = '-Wl,-bdynamic'
        ctx.env['STLIB_MARKER'] = '-Wl,-bstatic'

    elif ctx.env.DEST_OS == 'hpux':
        ctx.env.append_value('DEFINES', 'HPUX')
        if ctx.env.CC_NAME == 'gcc':
            if ctx.env.PYI_ARCH == '32bit':
                ctx.env.append_value('LIBPATH', '/usr/local/lib/hpux32')
                ctx.env.append_value('STATICLIBPATH', '/usr/local/lib/hpux32')
            else:
                ctx.env.append_value('LIBPATH', '/usr/local/lib/hpux64')
                ctx.env.append_value('STATICLIBPATH', '/usr/local/lib/hpux64')


    elif ctx.env.DEST_OS == 'darwin':
        # OS X 10.7 might not understand some load commands.
        # The following variable fixes 10.7 compatibility.
        # According to OS X doc this variable is equivalent to gcc option:
        #   -mmacosx-version-min=10.7
        if not os.environ.get('MACOSX_DEPLOYMENT_TARGET'):
            os.environ['MACOSX_DEPLOYMENT_TARGET'] = '10.7'

    ### Libraries

    if ctx.env.DEST_OS == 'win32':
        if ctx.env.CC_NAME == 'msvc':
            ctx.check_libs_msvc('user32 comctl32 kernel32 advapi32 ws2_32',
                                mandatory=True)
        else:
            ctx.check_cc(lib='user32', mandatory=True)
            ctx.check_cc(lib='comctl32', mandatory=True)
            ctx.check_cc(lib='kernel32', mandatory=True)
            ctx.check_cc(lib='advapi32', mandatory=True)
            ctx.check_cc(lib='ws2_32', mandatory=True)
    else:
        # Mac OS X and FreeBSD do not need libdl.
        # https://stackoverflow.com/questions/20169660/where-is-libdl-so-on-mac-os-x
        if ctx.env.DEST_OS not in ('darwin', 'freebsd', 'openbsd'):
            ctx.check_cc(lib='dl', mandatory=True)
        if ctx.env.DEST_OS == 'freebsd' and sysconfig.get_config_var('HAVE_PTHREAD_H'):
            # On FreeBSD if python has threads: libthr needs to be loaded in
            # the main process, so the bootloader needs to be link to thr.
            ctx.check_cc(lib='thr', mandatory=True)
        elif ctx.env.DEST_OS == 'hpux' and sysconfig.get_config_var('HAVE_PTHREAD_H'):
            ctx.check_cc(lib='pthread', mandatory=True)
        ctx.check_cc(lib='m', mandatory=True)
        ctx.check_cc(lib='z', mandatory=True, uselib_store='Z')
        # This uses Boehm GC to manage memory - it replaces malloc() / free()
        # functions. Some messages are printed if memory is not deallocated.
        if ctx.options.boehmgc:
            ctx.check_cc(lib='gc', mandatory=True)
            ctx.env.append_value('DEFINES', 'PYI_LEAK_DETECTOR')
            ctx.env.append_value('DEFINES', 'GC_FIND_LEAK')
            ctx.env.append_value('DEFINES', 'GC_DEBUG')
            ctx.env.append_value('DEFINES', 'SAVE_CALL_CHAIN')

    ctx.recurse("tests")

    ### Functions

    # The old ``function_name`` parameter to ``check_cc`` is no longer
    # supported. This code is based on old waf source at
    # https://gitlab.com/ita1024/waf/commit/62fe305d04ed37b1be1a3327a74b2fee6c458634#255b2344e5268e6a34bedd2f8c4680798344fec7.
    SNIP_FUNCTION = '''
    #include <%s>

    int main(int argc, char **argv) {
        void (*p)();

        (void)argc; (void)argv;
        p=(void(*)())(%s);
        return !p;
    }
'''
    # OS support for these functions varies.
    for header, function_name in (('stdlib.h', 'unsetenv'),
                                  ('stdlib.h', 'mkdtemp'),
                                  ('libgen.h', 'dirname'),
                                  ('libgen.h', 'basename'),
                                  ('string.h', 'strndup'),
                                  ('string.h', 'strnlen')):
        ctx.check(
            fragment=SNIP_FUNCTION % (header, function_name),
            mandatory=False,
            define_name=ctx.have_define(function_name),
            msg='Checking for function %s' % function_name)

    ### CFLAGS

    if ctx.env.DEST_OS == 'win32':
        if ctx.env.CC_NAME == 'msvc':
            # Use Unicode entry point wmain/wWinMain and wchar_t WinAPI
            ctx.env.append_value('CFLAGS', '-DUNICODE')
            ctx.env.append_value('CFLAGS', '-D_UNICODE')
            # set XP target as minimal target OS ver. when using Windows w/MSVC
            # https://blogs.msdn.microsoft.com/vcblog/2012/10/08/windows-xp-targeting-with-c-in-visual-studio-2012/
            ctx.env.append_value('LINKFLAGS', '/SUBSYSTEM:CONSOLE,%s' % (
                '5.01' if ctx.env.PYI_ARCH == '32bit' else '5.02'))
        else:
            # Use Visual C++ compatible alignment
            ctx.env.append_value('CFLAGS', '-mms-bitfields')

            # Define UNICODE and _UNICODE for wchar_t WinAPI
            ctx.env.append_value('CFLAGS', '-municode')

            # Use Unicode entry point wmain/wWinMain
            ctx.env.append_value('LINKFLAGS', '-municode')

    if ctx.env.DEST_OS == 'darwin':
        if not any(x for x in ctx.env.CPPFLAGS + ctx.env.CFLAGS
                   if x.startswith('-mmacosx-version-min=')):
            ctx.env.append_value('CFLAGS', '-mmacosx-version-min=10.7')
        if not any(x for x in ctx.env.LDFLAGS + ctx.env.LINKFLAGS
                   if x.startswith('-mmacosx-version-min=')):
            ctx.env.append_value('LINKFLAGS', '-mmacosx-version-min=10.7')

    # On linux link only with needed libraries.
    # -Wl,--as-needed is on some platforms detected during configure but
    # fails during build. (Mac OS X, Solaris, AIX)
    if ctx.env.DEST_OS == 'linux' and ctx.check_cc(cflags='-Wl,--as-needed'):
        ctx.env.append_value('LINKFLAGS', '-Wl,--as-needed')

    if ctx.env.CC_NAME != 'msvc':
        # This tool allows reducing the size of executables.
        ctx.find_program([assoc_programm(ctx, 'strip')], var='STRIP')
        ctx.load('strip', tooldir='tools')

    def windowed(name, baseenv):
        """Setup windowed environment based on `baseenv`."""
        ctx.setenv(name, baseenv)  # Inherit from `baseenv`.
        ctx.env.append_value('DEFINES', 'WINDOWED')

        if ctx.env.DEST_OS == 'win32':
            if ctx.env.CC_NAME != 'msvc':
                # For MinGW disable console window on Windows - MinGW option
                # TODO Is it necessary to have -mwindows for C and LINK flags?
                ctx.env.append_value('LINKFLAGS', '-mwindows')
                ctx.env.append_value('CFLAGS', '-mwindows')
            else:
                _link_flags = ctx.env._get_list_value_for_modification('LINKFLAGS')
                _subsystem = [x for x in _link_flags if x.startswith('/SUBSYSTEM:')]
                for parameter in _subsystem:
                    _link_flags.remove(parameter)
                ctx.env.append_value('LINKFLAGS', '/SUBSYSTEM:WINDOWS,%s' % (
                    '5.01' if ctx.env.PYI_ARCH == '32bit' else '5.02'))
        elif ctx.env.DEST_OS == 'darwin':
            # To support catching AppleEvents and running as ordinary OSX GUI
            # app, we have to link against the Carbon framework.
            # This linkage only needs to be there for the windowed bootloaders.
            ctx.env.append_value('LINKFLAGS', '-framework')
            ctx.env.append_value('LINKFLAGS', 'Carbon')
            # TODO Do we need to link with this framework?
            # conf.env.append_value('LINKFLAGS', '-framework')
            # conf.env.append_value('LINKFLAGS', 'ApplicationServices')

    ### DEBUG and RELEASE environments
    basic_env = ctx.env

    ## setup DEBUG environment
    ctx.setenv('debug', basic_env)  # Ensure env contains shared values.
    debug_env = ctx.env
    # This defines enable verbose console output of the bootloader.
    ctx.env.append_value('DEFINES', ['LAUNCH_DEBUG'])
    ctx.env.append_value('DEFINES', 'NDEBUG')

    ## setup windowed DEBUG environment
    windowed('debugw', debug_env)

    ## setup RELEASE environment
    ctx.setenv('release', basic_env)  # Ensure env contains shared values.
    release_env = ctx.env
    ctx.env.append_value('DEFINES', 'NDEBUG')

    ## setup windowed RELEASE environment
    windowed('releasew', release_env)

# TODO Use 'strip' command to decrease the size of compiled bootloaders.
def build(ctx):
    if not ctx.variant:
        ctx.fatal('Call "python waf all" to compile all bootloaders.')

    exe_name = variants[ctx.variant]

    install_path = os.path.join(os.getcwd(), '../PyInstaller/bootloader',
                                ctx.env.PYI_SYSTEM + "-" + ctx.env.PYI_ARCH)
    install_path = os.path.normpath(install_path)

    if machine():
        install_path += '-' + machine()

    if not ctx.env.LIB_Z:
        # If the operating system does not provide zlib, build our own. The
        # configure phase defines whether or not zlib is mandatory for a
        # platform.
        ctx.stlib(
            source=ctx.path.ant_glob('zlib/*.c'),
            target='static_zlib',
            name='Z',
            includes='zlib')

    # By default strip final executables to make them smaller.
    features = 'strip'
    if ctx.env.CC_NAME == 'msvc':
        # Do not strip bootloaders when using MSVC.
        features = ''

    ctx.objects(source=ctx.path.ant_glob('src/*.c', excl="src/main.c"),
                includes='src windows zlib',
                target="OBJECTS")

    ctx.env.link_with_dynlibs = []
    ctx.env.link_with_staticlibs = []
    if ctx.env.DEST_OS == 'win32':
        # Use different RC file (icon) for console/windowed mode - remove '_d'
        icon_rc = 'windows/' + exe_name.replace('_d', '') + '.rc'
        # On Windows we need to link library zlib statically.
        ctx.program(
            source=['src/main.c', icon_rc],
            target=exe_name,
            install_path=install_path,
            use='OBJECTS USER32 COMCTL32 KERNEL32 ADVAPI32 WS2_32 Z',
            includes='src windows zlib',
            features=features,
        )
    else:
        # Linux, Darwin (MacOSX), ...
        # Only the libs found will actually be used, so it's safe to list all
        # here. The decision if a lib is required for a specific platform is
        # made in the configure phase.
        libs = ['DL', 'M', 'Z',  # 'z' - zlib, 'm' - math,
                'THR']  # may be used on FreBSD
        staticlibs = []
        if ctx.env.DEST_OS == 'aix':
            # link statically with zlib, case sensitive
            libs.remove('Z')
            staticlibs.append('z')

        if ctx.options.boehmgc:
            libs.append('GC')

        ctx.env.link_with_dynlibs = libs
        ctx.env.link_with_staticlibs = staticlibs

        ctx.program(
            source='src/main.c',
            target=exe_name,
            includes='src',
            use=libs + ["OBJECTS"],
            stlib=staticlibs,
            install_path=install_path,
            features=features)

    ctx.recurse("tests")


class make_all(BuildContext):
    """
    Do build and install in one step.
    """
    cmd = 'make_all'

    def execute_build(ctx):
        Options.commands = ['build_debug', 'build_release']
        # On Windows and Mac OS X we also need console/windowed bootloaders.
        # On other platforms they make no sense.
        if ctx.env.DEST_OS in ('win32', 'darwin'):
            Options.commands += ['build_debugw', 'build_releasew']
        # Install bootloaders.
        Options.commands += ['install_debug', 'install_release']
        if ctx.env.DEST_OS in ('win32', 'darwin'):
            Options.commands += ['install_debugw', 'install_releasew']


def all(ctx):
    """
    Do configure, build and install in one step.
    """
    # `all` is run prior to `configure`, thus it does not get a build context.
    # Thus another command `make_all` is required which gets the build
    # context and can make decisions based on the outcome of `configure`.
    Options.commands = ['distclean', 'configure', 'make_all']


# Set up building several variants of bootloader.
for x in variants:
    class BootloaderContext(BuildContext):
        cmd = 'build' + '_' + x
        variant = x

    class BootloaderInstallContext(InstallContext):
        cmd = 'install' + '_' + x
        variant = x
