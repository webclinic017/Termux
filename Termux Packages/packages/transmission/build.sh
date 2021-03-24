TERMUX_PKG_HOMEPAGE=https://transmissionbt.com/
TERMUX_PKG_DESCRIPTION="Easy, lean and powerful BitTorrent client"
TERMUX_PKG_LICENSE="MIT"
TERMUX_PKG_VERSION=2.94
TERMUX_PKG_REVISION=6
TERMUX_PKG_SRCURL=https://github.com/transmission/transmission/archive/${TERMUX_PKG_VERSION}.tar.gz
TERMUX_PKG_SHA256=440c2fd0f89b1ab59d8a4b79ecd7bffd61bc000e36fb5b6c8e88142a4fadbb1f
TERMUX_PKG_DEPENDS="libcurl, libevent, miniupnpc, openssl"
TERMUX_PKG_EXTRA_CONFIGURE_ARGS="--disable-gtk --enable-lightweight --cache-file=termux_configure.cache"
# transmission already puts timestamps in the info printed to stdout so no need for svlogd -tt,
# therefore we override the transmission/log run script
TERMUX_PKG_SERVICE_SCRIPT=(
	"transmission" 'mkdir -p ~/torrent/torrent-files\nmkdir -p ~/torrent/download\nexec transmission-daemon -f -c ~/torrent/torrent-files -w ~/torrent/download 2>&1'
	"transmission/log" 'mkdir -p "$LOGDIR/sv/transmission"\nexec svlogd "$LOGDIR/sv/transmission"'
)

termux_step_pre_configure() {
	./autogen.sh

	echo "ac_cv_func_getmntent=no" >> termux_configure.cache
	echo "ac_cv_search_getmntent=false" >> termux_configure.cache
	chmod a-w termux_configure.cache
}
