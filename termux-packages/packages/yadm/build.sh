TERMUX_PKG_HOMEPAGE=https://github.com/TheLocehiliosan/yadm
TERMUX_PKG_DESCRIPTION="Yet Another Dotfiles Manager"
TERMUX_PKG_LICENSE="GPL-2.0"
TERMUX_PKG_MAINTAINER="@termux"
TERMUX_PKG_VERSION=3.0.0
TERMUX_PKG_SRCURL=https://github.com/TheLocehiliosan/yadm/archive/$TERMUX_PKG_VERSION.tar.gz
TERMUX_PKG_SHA256=af968c815817e9de85b60dc9c9a7e6159ed34e4f91ea78cadbcd6c73a0301c06
TERMUX_PKG_DEPENDS="git"
TERMUX_PKG_BUILD_IN_SRC=true

termux_step_make() {
	# Do not try to run 'make' as it causes a build failure.
	return
}

termux_step_make_install() {
	install -Dm700 "$TERMUX_PKG_SRCDIR"/yadm "$TERMUX_PREFIX"/bin/
	install -Dm600 "$TERMUX_PKG_SRCDIR"/yadm.1 "$TERMUX_PREFIX"/share/man/man1/
}
