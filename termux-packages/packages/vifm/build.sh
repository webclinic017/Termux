TERMUX_PKG_HOMEPAGE=https://vifm.info/
TERMUX_PKG_DESCRIPTION="File manager with vi like keybindings"
TERMUX_PKG_LICENSE="GPL-2.0"
TERMUX_PKG_MAINTAINER="@termux"
TERMUX_PKG_VERSION=0.11
TERMUX_PKG_SRCURL=https://github.com/vifm/vifm/archive/v${TERMUX_PKG_VERSION}.tar.gz
TERMUX_PKG_SHA256=7b76f39b2225db2960ee125da204ce6264fe992ec2d9f2954ab74ba3c28ce0ec
TERMUX_PKG_DEPENDS="ncurses, file"

termux_step_pre_configure() {
	autoreconf -if
	if $TERMUX_DEBUG; then
		# Debug build fails with:
		# /home/builder/.termux-build/vifm/src/src/fops_common.c:745:27: error: 'umask' called with invalid mode
		#      saved_umask = umask(~0600);
		export CFLAGS=${CFLAGS/-D_FORTIFY_SOURCE=2/}
	fi
}
