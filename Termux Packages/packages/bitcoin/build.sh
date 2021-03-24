TERMUX_PKG_HOMEPAGE=https://bitcoincore.org/
TERMUX_PKG_DESCRIPTION="Bitcoin Core"
TERMUX_PKG_LICENSE="MIT"
TERMUX_PKG_VERSION=0.19.1
TERMUX_PKG_SRCURL=https://github.com/bitcoin/bitcoin/archive/v$TERMUX_PKG_VERSION.tar.gz
TERMUX_PKG_SHA256=3b9d582ba36b50955f6dfad12cdf139462d19ad30604b49766dc2ca21a1a322c
TERMUX_PKG_CONFFILES="var/service/bitcoind/run var/service/bitcoind/log/run"
TERMUX_PKG_BUILD_IN_SRC=true

TERMUX_PKG_EXTRA_CONFIGURE_ARGS="
--disable-tests
--with-daemon
--with-gui=no
--without-libs
--prefix=${TERMUX_PKG_SRCDIR}/depends/$TERMUX_HOST_PLATFORM
--bindir=$TERMUX_PREFIX/bin
"

termux_step_pre_configure() {
	(cd depends && make HOST=$TERMUX_HOST_PLATFORM NO_QT=1 -j $TERMUX_MAKE_PROCESSES)
	./autogen.sh
}

termux_step_post_make_install() {
	mkdir -p $TERMUX_PREFIX/var/service
	cd $TERMUX_PREFIX/var/service
	mkdir -p bitcoind/log
	echo "#!$TERMUX_PREFIX/bin/sh" > bitcoind/run
	echo 'exec bitcoind 2>&1' >> bitcoind/run
	chmod +x bitcoind/run
	touch bitcoind/down
	ln -sf $TERMUX_PREFIX/share/termux-services/svlogger bitcoind/log/run
}
