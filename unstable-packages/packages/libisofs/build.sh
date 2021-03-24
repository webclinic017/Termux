TERMUX_PKG_HOMEPAGE=https://dev.lovelyhq.com/libburnia
TERMUX_PKG_DESCRIPTION="Library to pack up hard disk files and directories into a ISO 9660 disk image"
TERMUX_PKG_LICENSE="GPL-2.0"
TERMUX_PKG_MAINTAINER="Leonid Pliushch <leonid.pliushch@gmail.com>"
TERMUX_PKG_VERSION=1.5.2
TERMUX_PKG_REVISION=2
TERMUX_PKG_SRCURL=http://files.libburnia-project.org/releases/libisofs-$TERMUX_PKG_VERSION.tar.gz
TERMUX_PKG_SHA256=ef5a139600b3e688357450e52381e40ec26a447d35eb8d21524598c7b1675500
TERMUX_PKG_DEPENDS="libiconv, zlib"
TERMUX_PKG_BREAKS="libisofs-dev"
TERMUX_PKG_REPLACES="libisofs-dev"
TERMUX_PKG_BUILD_IN_SRC=true