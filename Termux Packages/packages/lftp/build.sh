TERMUX_PKG_HOMEPAGE=https://lftp.tech/
TERMUX_PKG_DESCRIPTION="FTP/HTTP client and file transfer program"
TERMUX_PKG_LICENSE="GPL-3.0"
TERMUX_PKG_VERSION=4.9.1
TERMUX_PKG_SRCURL=https://lftp.tech/ftp/lftp-${TERMUX_PKG_VERSION}.tar.xz
TERMUX_PKG_SHA256=5969fcaefd102955dd882f3bcd8962198bc537224749ed92f206f415207a024b
TERMUX_PKG_DEPENDS="libandroid-support, libc++, libexpat, libiconv, openssl, readline, libidn2, zlib"

# (1) Android has dn_expand, but lftp assumes that dn_skipname then exists, which it does not on android.
# (2) Use --with-openssl to use openssl instead of gnutls.
TERMUX_PKG_EXTRA_CONFIGURE_ARGS="
ac_cv_header_glob_h=no
ac_cv_func_dn_expand=no
--with-openssl
--with-expat=$TERMUX_PREFIX
--with-readline=$TERMUX_PREFIX
--with-zlib=$TERMUX_PREFIX
"

termux_step_pre_configure() {
	if $TERMUX_DEBUG; then
		# When doing debug build, -D_FORTIFY_SOURCE=2 gives this error:
		# /home/builder/.termux-build/_lib/16-aarch64-21-v3/bin/../sysroot/usr/include/bits/fortify/string.h:79:26: error: use of undeclared identifier '__USE_FORTIFY_LEVEL'
		export CFLAGS=${CFLAGS/-D_FORTIFY_SOURCE=2/}
	fi

	CXXFLAGS+=" -DNO_INLINE_GETPASS=1"
}
