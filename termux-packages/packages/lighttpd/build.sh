TERMUX_PKG_HOMEPAGE=https://www.lighttpd.net
TERMUX_PKG_DESCRIPTION="Fast webserver with minimal memory footprint"
TERMUX_PKG_LICENSE="BSD 3-Clause"
TERMUX_PKG_MAINTAINER="@termux"
TERMUX_PKG_VERSION=1.4.58
TERMUX_PKG_SRCURL=https://download.lighttpd.net/lighttpd/releases-1.4.x/lighttpd-${TERMUX_PKG_VERSION}.tar.xz
TERMUX_PKG_SHA256=267feffda13a190ebdce7b15172d8be16da98008457f30fddecd72832d126d0e
TERMUX_PKG_EXTRA_CONFIGURE_ARGS="--with-bzip2 --with-openssl --with-pcre --with-zlib"
TERMUX_PKG_DEPENDS="libbz2, openssl, pcre, libcrypt, libandroid-glob, zlib"
TERMUX_PKG_RM_AFTER_INSTALL="bin/lighttpd-angel"
TERMUX_PKG_SERVICE_SCRIPT=("lighttpd" 'if [ -f "$HOME/.lighttpd/lighttpd.conf" ]; then CONFIG="$HOME/.lighttpd/lighttpd.conf"; else CONFIG="$PREFIX/etc/lighttpd/lighttpd.conf"; fi\nexec lighttpd -D -f $CONFIG 2>&1')

termux_step_pre_configure() {
	LDFLAGS="$LDFLAGS -landroid-glob"
}

termux_step_post_make_install() {
	# Install example config file
	mkdir -p $TERMUX_PREFIX/etc/lighttpd
	install -Dm600 $TERMUX_PKG_SRCDIR/doc/config/lighttpd.conf $TERMUX_PREFIX/etc/lighttpd/
}
