TERMUX_PKG_HOMEPAGE=https://www.tcpdump.org/
TERMUX_PKG_DESCRIPTION="A powerful command-line packet analyzer"
TERMUX_PKG_LICENSE="BSD 3-Clause"
TERMUX_PKG_VERSION=4.9.3
TERMUX_PKG_SRCURL=https://www.tcpdump.org/release/tcpdump-${TERMUX_PKG_VERSION}.tar.gz
TERMUX_PKG_SHA256=2cd47cb3d460b6ff75f4a9940f594317ad456cfbf2bd2c8e5151e16559db6410
TERMUX_PKG_EXTRA_CONFIGURE_ARGS="ac_cv_linux_vers=3.4"
TERMUX_PKG_RM_AFTER_INSTALL="bin/tcpdump.${TERMUX_PKG_VERSION}"
TERMUX_PKG_DEPENDS="openssl, libpcap"
