TERMUX_PKG_HOMEPAGE=https://www.gnu.org/software/mtools/
TERMUX_PKG_DESCRIPTION="Tool for manipulating FAT images."
TERMUX_PKG_LICENSE="GPL-2.0"
TERMUX_PKG_VERSION=4.0.24
TERMUX_PKG_SRCURL=https://mirrors.kernel.org/gnu/mtools/mtools-${TERMUX_PKG_VERSION}.tar.bz2
TERMUX_PKG_SHA256=24f4a2da9219f98498eb1b340cd96db7ef9b684c067d1bdeb6e85efdd13b2fb9
TERMUX_PKG_DEPENDS="libandroid-support, libiconv"

TERMUX_PKG_EXTRA_CONFIGURE_ARGS="
--disable-floppyd
ac_cv_lib_bsd_main=no
"

termux_step_pre_configure() {
	export LIBS="-liconv"
}
