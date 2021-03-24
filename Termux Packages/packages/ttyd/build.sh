TERMUX_PKG_HOMEPAGE=https://tsl0922.github.io/ttyd/
TERMUX_PKG_DESCRIPTION="Command-line tool for sharing terminal over the web"
TERMUX_PKG_LICENSE="MIT"
TERMUX_PKG_VERSION=1.6.0
TERMUX_PKG_REVISION=1
TERMUX_PKG_SRCURL=https://github.com/tsl0922/ttyd/archive/$TERMUX_PKG_VERSION.tar.gz
TERMUX_PKG_SHA256=d14740bc82be0d0760dd0a3c97acbcbde490412a4edc61edabe46d311b068f83
TERMUX_PKG_DEPENDS="json-c, libuv, libwebsockets, zlib"
TERMUX_PKG_EXTRA_CONFIGURE_ARGS="-DCMAKE_XXD=$TERMUX_PKG_TMPDIR/xxd"

termux_step_pre_configure() {
	termux_download \
		https://raw.githubusercontent.com/vim/vim/v8.1.0427/src/xxd/xxd.c \
		$TERMUX_PKG_CACHEDIR/xxd.c \
		021b38e02cd31951a80ef5185271d71f2def727eb8ff65b7a07aecfbd688b8e1
	gcc $TERMUX_PKG_CACHEDIR/xxd.c -o $TERMUX_PKG_TMPDIR/xxd
}
