TERMUX_PKG_HOMEPAGE=https://www.ruby-lang.org/
TERMUX_PKG_DESCRIPTION="Dynamic programming language with a focus on simplicity and productivity"
TERMUX_PKG_LICENSE="BSD 2-Clause"
TERMUX_PKG_VERSION=2.7.1
TERMUX_PKG_SRCURL=https://cache.ruby-lang.org/pub/ruby/${TERMUX_PKG_VERSION:0:3}/ruby-${TERMUX_PKG_VERSION}.tar.xz
TERMUX_PKG_SHA256=b224f9844646cc92765df8288a46838511c1cec5b550d8874bd4686a904fcee7
# libbffi is used by the fiddle extension module:
TERMUX_PKG_DEPENDS="gdbm, libandroid-support, libffi, libgmp, readline, openssl, libyaml, zlib"
TERMUX_PKG_BREAKS="ruby-dev"
TERMUX_PKG_REPLACES="ruby-dev"
# Needed to fix compilation on android:
TERMUX_PKG_EXTRA_CONFIGURE_ARGS="ac_cv_func_setgroups=no ac_cv_func_setresuid=no ac_cv_func_setreuid=no --enable-rubygems --with-coroutine=copy"
# The gdbm module seems to be very little used:
TERMUX_PKG_EXTRA_CONFIGURE_ARGS+=" --without-gdbm"
# Do not link in libcrypt.so if available (now in disabled-packages):
TERMUX_PKG_EXTRA_CONFIGURE_ARGS+=" ac_cv_lib_crypt_crypt=no"
# Fix DEPRECATED_TYPE macro clang compatibility:
TERMUX_PKG_EXTRA_CONFIGURE_ARGS+=" rb_cv_type_deprecated=x"
# getresuid(2) does not work on ChromeOS - https://github.com/termux/termux-app/issues/147:
# TERMUX_PKG_EXTRA_CONFIGURE_ARGS+=" ac_cv_func_getresuid=no"
TERMUX_PKG_HOSTBUILD=true

termux_step_host_build() {
	"$TERMUX_PKG_SRCDIR/configure" --prefix=$TERMUX_PKG_HOSTBUILD_DIR/ruby-host
	make -j $TERMUX_MAKE_PROCESSES
	make install
	export PATH=$TERMUX_PKG_HOSTBUILD_DIR/ruby-host/bin:$PATH
}

termux_step_pre_configure() {
	if [ "$TERMUX_ARCH_BITS" = 32 ]; then
		# process.c:function timetick2integer: error: undefined reference to '__mulodi4'
		TERMUX_PKG_EXTRA_CONFIGURE_ARGS+=" rb_cv_builtin___builtin_mul_overflow=no"
	fi
}

termux_step_make_install() {
	make install
	make uninstall # remove possible remains to get fresh timestamps
	make install

	local RBCONFIG=$TERMUX_PREFIX/lib/ruby/${TERMUX_PKG_VERSION:0:3}.0/${TERMUX_HOST_PLATFORM}/rbconfig.rb

	# Fix absolute paths to executables:
	perl -p -i -e 's/^.*CONFIG\["INSTALL"\].*$/  CONFIG["INSTALL"] = "install -c"/' $RBCONFIG
	perl -p -i -e 's/^.*CONFIG\["PKG_CONFIG"\].*$/  CONFIG["PKG_CONFIG"] = "pkg-config"/' $RBCONFIG
	perl -p -i -e 's/^.*CONFIG\["MAKEDIRS"\].*$/  CONFIG["MAKEDIRS"] = "mkdir -p"/' $RBCONFIG
	perl -p -i -e 's/^.*CONFIG\["MKDIR_P"\].*$/  CONFIG["MKDIR_P"] = "mkdir -p"/' $RBCONFIG
	perl -p -i -e 's/^.*CONFIG\["EGREP"\].*$/  CONFIG["EGREP"] = "grep -E"/' $RBCONFIG
	perl -p -i -e 's/^.*CONFIG\["GREP"\].*$/  CONFIG["GREP"] = "grep"/' $RBCONFIG
}

termux_step_post_massage() {
	if [ ! -f $TERMUX_PREFIX/lib/ruby/${TERMUX_PKG_VERSION:0:3}.0/${TERMUX_HOST_PLATFORM}/readline.so ]; then
		echo "Error: The readline extension was not built"
	fi
}
