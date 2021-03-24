TERMUX_PKG_HOMEPAGE=https://www.gnu.org/software/bash/
TERMUX_PKG_DESCRIPTION="A sh-compatible shell that incorporates useful features from the Korn shell (ksh) and C shell (csh)"
TERMUX_PKG_LICENSE="GPL-3.0"
_MAIN_VERSION=5.0
_PATCH_VERSION=17
TERMUX_PKG_VERSION=${_MAIN_VERSION}.${_PATCH_VERSION}
TERMUX_PKG_SRCURL=https://mirrors.kernel.org/gnu/bash/bash-${_MAIN_VERSION}.tar.gz
TERMUX_PKG_SHA256=b4a80f2ac66170b2913efbfb9f2594f1f76c7b1afd11f799e22035d63077fb4d
TERMUX_PKG_DEPENDS="libandroid-support, libiconv, ncurses, readline (>= 8.0), termux-tools"
TERMUX_PKG_RECOMMENDS="command-not-found"
TERMUX_PKG_BREAKS="bash-dev"
TERMUX_PKG_REPLACES="bash-dev"
TERMUX_PKG_ESSENTIAL=true
TERMUX_PKG_BUILD_IN_SRC=true

TERMUX_PKG_EXTRA_CONFIGURE_ARGS="--enable-multibyte --without-bash-malloc --with-installed-readline"
TERMUX_PKG_EXTRA_CONFIGURE_ARGS+=" bash_cv_job_control_missing=present"
TERMUX_PKG_EXTRA_CONFIGURE_ARGS+=" bash_cv_sys_siglist=yes"
TERMUX_PKG_EXTRA_CONFIGURE_ARGS+=" bash_cv_func_sigsetjmp=present"
TERMUX_PKG_EXTRA_CONFIGURE_ARGS+=" bash_cv_unusable_rtsigs=no"
TERMUX_PKG_EXTRA_CONFIGURE_ARGS+=" ac_cv_func_mbsnrtowcs=no"
# Use bash_cv_dev_fd=whacky to use /proc/self/fd instead of /dev/fd.
# After making this change process substitution such as in 'cat <(ls)' works.
TERMUX_PKG_EXTRA_CONFIGURE_ARGS+=" bash_cv_dev_fd=whacky"
# Bash assumes that getcwd is broken and provides a wrapper which
# does not work when not all parent directories up to root are
# accessible, which they are not under Android (/data). See
# - http://permalink.gmane.org/gmane.linux.embedded.yocto.general/25204
# - https://github.com/termux/termux-app/issues/200
TERMUX_PKG_EXTRA_CONFIGURE_ARGS+=" bash_cv_getcwd_malloc=yes"

TERMUX_PKG_CONFFILES="etc/bash.bashrc etc/profile"

TERMUX_PKG_RM_AFTER_INSTALL="share/man/man1/bashbug.1 bin/bashbug"

termux_step_pre_configure() {
	declare -A PATCH_CHECKSUMS

	PATCH_CHECKSUMS[001]=f2fe9e1f0faddf14ab9bfa88d450a75e5d028fedafad23b88716bd657c737289
	PATCH_CHECKSUMS[002]=87e87d3542e598799adb3e7e01c8165bc743e136a400ed0de015845f7ff68707
	PATCH_CHECKSUMS[003]=4eebcdc37b13793a232c5f2f498a5fcbf7da0ecb3da2059391c096db620ec85b
	PATCH_CHECKSUMS[004]=14447ad832add8ecfafdce5384badd933697b559c4688d6b9e3d36ff36c62f08
	PATCH_CHECKSUMS[005]=5bf54dd9bd2c211d2bfb34a49e2c741f2ed5e338767e9ce9f4d41254bf9f8276
	PATCH_CHECKSUMS[006]=d68529a6ff201b6ff5915318ab12fc16b8a0ebb77fda3308303fcc1e13398420
	PATCH_CHECKSUMS[007]=17b41e7ee3673d8887dd25992417a398677533ab8827938aa41fad70df19af9b
	PATCH_CHECKSUMS[008]=eec64588622a82a5029b2776e218a75a3640bef4953f09d6ee1f4199670ad7e3
	PATCH_CHECKSUMS[009]=ed3ca21767303fc3de93934aa524c2e920787c506b601cc40a4897d4b094d903
	PATCH_CHECKSUMS[010]=d6fbc325f0b5dc54ddbe8ee43020bced8bd589ddffea59d128db14b2e52a8a11
	PATCH_CHECKSUMS[011]=2c4de332b91eaf797abbbd6c79709690b5cbd48b12e8dfe748096dbd7bf474ea
	PATCH_CHECKSUMS[012]=2943ee19688018296f2a04dbfe30b7138b889700efa8ff1c0524af271e0ee233
	PATCH_CHECKSUMS[013]=f5d7178d8da30799e01b83a0802018d913d6aa972dd2ddad3b927f3f3eb7099a
	PATCH_CHECKSUMS[014]=5d6eee6514ee6e22a87bba8d22be0a8621a0ae119246f1c5a9a35db1f72af589
	PATCH_CHECKSUMS[015]=a517df2dda93b26d5cbf00effefea93e3a4ccd6652f152f4109170544ebfa05e
	PATCH_CHECKSUMS[016]=ffd1d7a54a99fa7f5b1825e4f7e95d8c8876bc2ca151f150e751d429c650b06d
	PATCH_CHECKSUMS[017]=4cf3b9fafb8a66d411dd5fc9120032533a4012df1dc6ee024c7833373e2ddc31

	for PATCH_NUM in $(seq -f '%03g' ${_PATCH_VERSION}); do
		PATCHFILE=$TERMUX_PKG_CACHEDIR/bash_patch_${PATCH_NUM}.patch
		termux_download \
			"https://mirrors.kernel.org/gnu/bash/bash-${_MAIN_VERSION}-patches/bash${_MAIN_VERSION/./}-$PATCH_NUM" \
			$PATCHFILE \
			${PATCH_CHECKSUMS[$PATCH_NUM]}
		patch -p0 -i $PATCHFILE
	done
	unset PATCH_CHECKSUMS PATCHFILE PATCH_NUM
}

termux_step_post_make_install() {
	sed -e "s|@TERMUX_PREFIX@|$TERMUX_PREFIX|" \
		-e "s|@TERMUX_HOME@|$TERMUX_ANDROID_HOME|" \
		$TERMUX_PKG_BUILDER_DIR/etc-profile > $TERMUX_PREFIX/etc/profile

	# /etc/bash.bashrc - System-wide .bashrc file for interactive shells. (config-top.h in bash source, patched to enable):
	sed -e "s|@TERMUX_PREFIX@|$TERMUX_PREFIX|" \
		-e "s|@TERMUX_HOME@|$TERMUX_ANDROID_HOME|" \
		$TERMUX_PKG_BUILDER_DIR/etc-bash.bashrc > $TERMUX_PREFIX/etc/bash.bashrc
}
