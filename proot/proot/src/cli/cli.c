/* -*- c-set-style: "K&R"; c-basic-offset: 8 -*-
 *
 * This file is part of PRoot.
 *
 * Copyright (C) 2015 STMicroelectronics
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License as
 * published by the Free Software Foundation; either version 2 of the
 * License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
 * 02110-1301 USA.
 */

#include <stdio.h>         /* printf(3), */
#include <stdbool.h>       /* bool, true, false,  */
#include <linux/limits.h>  /* ARG_MAX, PATH_MAX, */
#include <string.h>        /* str*(3), basename(3),  */
#include <talloc.h>        /* talloc*,  */
#include <stdlib.h>        /* exit(3), EXIT_*, strtol(3), {g,s}etenv(3), */
#include <assert.h>        /* assert(3),  */
#include <sys/types.h>     /* getpid(2),  */
#include <unistd.h>        /* getpid(2),  */
#include <errno.h>         /* errno(3), */
#include <libgen.h>        /* basename(3), */
#ifdef __GLIBC__
#include <execinfo.h>      /* backtrace_symbols(3), */
#endif
#include <limits.h>        /* INT_MAX, */

#include "cli/cli.h"
#include "cli/note.h"
#include "extension/extension.h"
#include "tracee/tracee.h"
#include "tracee/event.h"
#include "path/binding.h"
#include "path/canon.h"
#include "path/path.h"
#include <extension/extension.h>
#include <extension/sysvipc/sysvipc.h>

#include "build.h"

/**
 * Print a (@detailed) usage of PRoot.
 */
void print_usage(Tracee *tracee, const Cli *cli, bool detailed)
{
	const char *current_class = "none";
	const Option *options;
	size_t i, j;

#define DETAIL(a) if (detailed) a

	DETAIL(printf("%s %s: %s.\n\n", cli->name, cli->version, cli->subtitle));
	printf("Usage:\n  %s\n", cli->synopsis);
	DETAIL(printf("\n"));

	options = cli->options;
	for (i = 0; options[i].class != NULL; i++) {
		for (j = 0; ; j++) {
			const Argument *argument = &(options[i].arguments[j]);

			if (!argument->name || (!detailed && j != 0)) {
				DETAIL(printf("\n"));
				printf("\t%s\n", options[i].description);
				if (detailed) {
					if (options[i].detail[0] != '\0')
						printf("\n%s\n\n", options[i].detail);
					else
						printf("\n");
				}
				break;
			}

			if (strcmp(options[i].class, current_class) != 0) {
				current_class = options[i].class;
				printf("\n%s:\n", current_class);
			}

			if (j == 0)
				printf("  %s", argument->name);
			else
				printf(", %s", argument->name);

			if (argument->separator != '\0')
				printf("%c*%s*", argument->separator, argument->value);
			else if (!detailed)
				printf("\t");
		}
	}

	notify_extensions(tracee, PRINT_USAGE, detailed, 0);

	if (detailed)
		printf("%s\n", cli->colophon);
}

/**
 * Print the version of PRoot.
 */
void print_version(const Cli *cli)
{
	printf("%s %s\n\n", cli->logo, cli->version);
	printf("built-in accelerators: process_vm = %s, seccomp_filter = %s\n",
#if defined(HAVE_PROCESS_VM)
		"yes",
#else
		"no",
#endif
#if defined(HAVE_SECCOMP_FILTER)
		"yes"
#else
		"no"
#endif
		);
}

static void print_execve_help(const Tracee *tracee, const char *argv0, int status)
{
	note(tracee, ERROR, SYSTEM, "execve(\"%s\")", argv0);

	/* termux-exec replaced execve with path with one that doesn't exist inside proot?  */
	if (status == -ENOENT && getenv("LD_PRELOAD") != NULL && strstr(getenv("LD_PRELOAD"), "libtermux-exec.so") != NULL) {
		note(tracee, INFO, USER,
"It seems that termux-exec is active and is prepending /data/data/com.termux/... to executable paths\n"
"If this is path is not available inside proot, please \"unset LD_PRELOAD\"");
		return;
	}

	/* Ubuntu kernel bug?  */
	if (status == -EPERM && getenv("PROOT_NO_SECCOMP") == NULL) {
		note(tracee, INFO, USER,
"It seems your kernel contains this bug: https://bugs.launchpad.net/ubuntu/+source/linux/+bug/1202161\n"
"To workaround it, set the env. variable PROOT_NO_SECCOMP to 1.");
		return;
	}

	note(tracee, INFO, USER, "possible causes:\n"
"  * the program is a script but its interpreter (eg. /bin/sh) was not found;\n"
"  * the program is an ELF but its interpreter (eg. ld-linux.so) was not found;\n"
"  * the program is a foreign binary but qemu was not specified;\n"
"  * qemu does not work correctly (if specified);\n"
"  * the loader was not found or doesn't work.");
}

static void print_error_separator(const Tracee *tracee, const Argument *argument)
{
	if (argument->separator == '\0')
		note(tracee, ERROR, USER, "option '%s' expects no value.", argument->name);
	else
		note(tracee, ERROR, USER, "option '%s' and its value must be separated by '%c'.",
			argument->name, argument->separator);
}

static void print_argv(const Tracee *tracee, const char *prompt, char *const argv[])
{
	char string[ARG_MAX] = "";
	size_t i;

	if (!argv)
		return;

#define APPEND(post)							\
	do {								\
		ssize_t length = sizeof(string) - (strlen(string) + strlen(post)); \
		if (length <= 0)					\
			return;						\
		strncat(string, post, length);				\
	} while (0)

	APPEND(prompt);
	APPEND(" =");
	for (i = 0; argv[i] != NULL; i++) {
		APPEND(" ");
		APPEND(argv[i]);
	}
	string[sizeof(string) - 1] = '\0';

#undef APPEND

	note(tracee, INFO, USER, "%s", string);
}

static void print_config(Tracee *tracee, char *const argv[])
{
	assert(tracee != NULL);

	if (tracee->verbose <= 0)
		return;

	if (tracee->qemu)
		note(tracee, INFO, USER, "host rootfs = %s", HOST_ROOTFS);

	if (tracee->glue)
		note(tracee, INFO, USER, "glue rootfs = %s", tracee->glue);

	note(tracee, INFO, USER, "exe = %s", tracee->exe);
	print_argv(tracee, "argv", argv);
	print_argv(tracee, "qemu", tracee->qemu);
	note(tracee, INFO, USER, "initial cwd = %s", tracee->fs->cwd);
	note(tracee, INFO, USER, "verbose level = %d", tracee->verbose);

	notify_extensions(tracee, PRINT_CONFIG, 0, 0);
}

/**
 * Initialize @tracee's current working directory.  This function
 * returns -1 if an error occurred, otherwise 0.
 */
static int initialize_cwd(Tracee *tracee)
{
	char path2[PATH_MAX];
	char path[PATH_MAX];
	int status;

	/* Compute the base directory.  */
	if (tracee->fs->cwd[0] != '/') {
		status = getcwd2(tracee->reconf.tracee, path);
		if (status < 0) {
			note(tracee, ERROR, INTERNAL, "getcwd: %s", strerror(-status));
			return -1;
		}
	}
	else
		strcpy(path, "/");

	/* The ending "." ensures canonicalize() will report an error
	 * if tracee->fs->cwd does not exist or if it is not a
	 * directory.  */
	status = join_paths(3, path2, path, tracee->fs->cwd, ".");
	if (status < 0) {
		note(tracee, ERROR, INTERNAL, "getcwd: %s", strerror(-status));
		return -1;
	}

	/* Initiale state for canonicalization.  */
	strcpy(path, "/");

	status = canonicalize(tracee, path2, true, path, 0);
	if (status < 0) {
		note(tracee, WARNING, USER, "can't chdir(\"%s\") in the guest rootfs: %s",
			path2, strerror(-status));
		note(tracee, INFO, USER, "default working directory is now \"/\"");
		strcpy(path, "/");
	}
	chop_finality(path);

	/* Replace with the canonicalized working directory.  */
	TALLOC_FREE(tracee->fs->cwd);
	tracee->fs->cwd = talloc_strdup(tracee->fs, path);
	if (tracee->fs->cwd == NULL)
		return -1;
	talloc_set_name_const(tracee->fs->cwd, "$cwd");

	/* Keep this special environment variable consistent.  */
	setenv("PWD", path, 1);

	return 0;
}

/**
 * Initialize @tracee->exe from @exe, i.e. canonicalize it from a
 * guest point-of-view.
 */
static int initialize_exe(Tracee *tracee, const char *exe)
{
	char path[PATH_MAX];
	int status;

	status = which(tracee, tracee->reconf.paths, path, exe ?: "/bin/sh");
	if (status < 0)
		return -1;

	status = detranslate_path(tracee, path, NULL);
	if (status < 0)
		return -1;

	tracee->exe = talloc_strdup(tracee, path);
	if (tracee->exe == NULL)
		return -1;
	talloc_set_name_const(tracee->exe, "$exe");

	return 0;
}

/**
 * Configure @tracee according to the command-line arguments stored in
 * @argv[].  This function returns the index in @argv[] of the command
 * to launch, otherwise -1 if an error occured.
 */
static int parse_config(Tracee *tracee, size_t argc, char *const argv[])
{
	option_handler_t handler = NULL;
	const Option *options;
	const Cli *cli = NULL;
	size_t argc_offset;
	size_t i, j, k;
	int status;

	/* Unknown tool name?  Default to PRoot.  */
	if (cli == NULL)
		cli = get_proot_cli(tracee->ctx);
	tracee->tool_name = cli->name;

	if (argc == 1) {
		print_usage(tracee, cli, false);
		return -1;
	}

	for (i = 1; i < argc; i++) {
		const char *arg = argv[i];

		/* The current argument is the value of a short option.  */
		if (handler != NULL) {
			status = handler(tracee, cli, arg);
			if (status < 0)
				return -1;
			handler = NULL;
			continue;
		}

		if (arg[0] != '-')
			break; /* End of PRoot options. */

		options = cli->options;
		for (j = 0; options[j].class != NULL; j++) {
			const Option *option = &options[j];

			/* A given option has several aliases.  */
			for (k = 0; ; k++) {
				const Argument *argument;
				size_t length;

				argument = &option->arguments[k];

				/* End of aliases for this option.  */
				if (!argument->name)
					break;

				length = strlen(argument->name);
				if (strncmp(arg, argument->name, length) != 0)
					continue;

				/* Avoid ambiguities.  */
				if (strlen(arg) > length
				    && arg[length] != argument->separator) {
					print_error_separator(tracee, argument);
					return -1;
				}

				/* No option value.  */
				if (!argument->value) {
					status = option->handler(tracee, cli, NULL);
					if (status < 0)
						return -1;
					goto known_option;
				}

				/* Value coalesced with to its option.  */
				if (argument->separator == arg[length]) {
					assert(strlen(arg) >= length);
					status = option->handler(tracee, cli, &arg[length + 1]);
					if (status < 0)
						return -1;
					goto known_option;
				}

				/* Avoid ambiguities.  */
				if (argument->separator != ' ') {
					print_error_separator(tracee, argument);
					return -1;
				}

				/* Short option with a separated value.  */
				handler = option->handler;
				goto known_option;
			}
		}

		note(tracee, ERROR, USER, "unknown option '%s'.", arg);
		return -1;

	known_option:
		if (handler != NULL && i == argc - 1) {
			note(tracee, ERROR, USER, "missing value for option '%s'.", arg);
			return -1;
		}
	}
	argc_offset = i;

#define HOOK_CONFIG(callback)						\
	do {								\
		if (cli->callback != NULL) {				\
			status = cli->callback(tracee, cli, argc, argv, i); \
			if (status < 0)					\
				return -1;				\
			i = status;					\
		}							\
	} while (0)

	HOOK_CONFIG(pre_initialize_bindings);

	/* The guest rootfs is now known: bindings specified by the
	 * user (tracee->bindings.user) can be canonicalized.  */
	status = initialize_bindings(tracee);
	if (status < 0)
		return -1;

	HOOK_CONFIG(post_initialize_bindings);
	HOOK_CONFIG(pre_initialize_cwd);

	/* Bindings are now installed (tracee->bindings.guest &
	 * tracee->bindings.host): the current working directory can
	 * be canonicalized.  */
	status = initialize_cwd(tracee);
	if (status < 0)
		return -1;

	HOOK_CONFIG(post_initialize_cwd);
	HOOK_CONFIG(pre_initialize_exe);

	/* Bindings are now installed and the current working
	 * directory is canonicalized: resolve path to @tracee->exe
	 * and configure @tracee->cmdline.  */
	status = initialize_exe(tracee, argv[argc_offset]);
	if (status < 0)
		return -1;

	HOOK_CONFIG(post_initialize_exe);
#undef HOOK_CONFIG

	print_config(tracee, &argv[argc_offset]);

	return argc_offset;
}

bool exit_failure = true;

int main(int argc, char *const argv[])
{
	Tracee *tracee;
	int status;

	/* Configure the memory allocator.  */
	talloc_enable_leak_report();

#if defined(TALLOC_VERSION_MAJOR) && TALLOC_VERSION_MAJOR >= 2
	talloc_set_log_stderr();
#endif

	if (argc == 2 && strcmp(argv[1], "--shm-helper") == 0) {
		sysvipc_shm_helper_main();
	}

	/* Pre-create the first tracee (pid == 0).  */
	tracee = get_tracee(NULL, 0, true);
	if (tracee == NULL)
		goto error;
	tracee->pid = getpid();

	/* Set verboseness from env variable, may be overriden by option */
	{
		const char *verbose_env = getenv("PROOT_VERBOSE");
		if (verbose_env != NULL) {
			tracee->verbose = strtol(verbose_env, NULL, 10);
			global_verbose_level = tracee->verbose;
		}
	}

	/* Pre-configure the first tracee.  */
	status = parse_config(tracee, argc, argv);
	if (status < 0)
		goto error;

	/* Start the first tracee.  */
	status = launch_process(tracee, &argv[status]);
	if (status < 0) {
		print_execve_help(tracee, tracee->exe, status);
		goto error;
	}

	/* Start tracing the first tracee and all its children.  */
	exit(event_loop());

error:
	TALLOC_FREE(tracee);

	if (exit_failure) {
		fprintf(stderr, "fatal error: see `%s --help`.\n", basename(argv[0]));
		exit(EXIT_FAILURE);
	}
	else
		exit(EXIT_SUCCESS);
}

/**
 * Convert @value into an integer, then put the result into
 * *@variable.  This function prints a warning and returns -1 if a
 * conversion error occured, otherwise it returns 0.
 */
int parse_integer_option(const Tracee *tracee, int *variable, const char *value, const char *option)
{
	char *end_ptr = NULL;

	errno = 0;
	*variable = strtol(value, &end_ptr, 10);
	if (errno != 0 || end_ptr == value) {
		note(tracee, ERROR, USER, "option `%s` expects an integer value.", option);
		return -1;
	}

	return 0;
}

/**
 * Expand the environment variable in front of @string, if any.  For
 * example, this function can expand "$HOME" or "$HOME/.ICEauthority".
 */
const char *expand_front_variable(TALLOC_CTX *context, const char *string)
{
	const char *suffix;
	char *expanded;
	ptrdiff_t size;

	if (string[0] != '$')
		return string;

	suffix = strchr(string, '/');
	if (suffix == NULL)
		return (getenv(&string[1]) ?: string);

	size = suffix - string;
	if (size <= 1)
		return string;

	expanded = talloc_strndup(context, &string[1], size - 1);
	if (expanded == NULL)
		return string;

	expanded = getenv(expanded);
	if (expanded == NULL)
		return string;

	expanded = talloc_asprintf(context, "%s%s", expanded, suffix);
	if (expanded == NULL)
		return string;

	return expanded;
}

/* Here follows the support for GCC function instrumentation.  Build
 * with CFLAGS='-finstrument-functions -O0 -g' and LDFLAGS='-rdynamic'
 * to enable this mechanism.  */

static int indent_level = 0;

void __cyg_profile_func_enter(void *this_function, void *call_site) DONT_INSTRUMENT;
void __cyg_profile_func_enter(void *this_function, void *call_site)
{
	void *const pointers[] = { this_function, call_site };
	char **symbols = NULL;

#ifdef __GLIBC__
	symbols = backtrace_symbols(pointers, 2);
#endif
	if (symbols == NULL)
		goto end;

	fprintf(stderr, "%*s from %s\n", (int) strlen(symbols[0]) + indent_level, symbols[0], symbols[1]);

end:
	if (symbols != NULL)
		free(symbols);

	if (indent_level < INT_MAX)
		indent_level++;
}

void __cyg_profile_func_exit(void *this_function UNUSED, void *call_site UNUSED) DONT_INSTRUMENT;
void __cyg_profile_func_exit(void *this_function UNUSED, void *call_site UNUSED)
{
	if (indent_level > 0)
		indent_level--;
}
