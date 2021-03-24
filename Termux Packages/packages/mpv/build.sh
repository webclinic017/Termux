TERMUX_PKG_HOMEPAGE=https://mpv.io/
TERMUX_PKG_DESCRIPTION="Command-line media player"
TERMUX_PKG_LICENSE="GPL-3.0"
TERMUX_PKG_VERSION=0.32.0
TERMUX_PKG_SRCURL=https://github.com/mpv-player/mpv/archive/v${TERMUX_PKG_VERSION}.tar.gz
TERMUX_PKG_SHA256=9163f64832226d22e24bbc4874ebd6ac02372cd717bef15c28a0aa858c5fe592
TERMUX_PKG_DEPENDS="ffmpeg, libandroid-glob, libandroid-support, libarchive, libcaca, libiconv, liblua52, pulseaudio, openal-soft, zlib"
TERMUX_PKG_RM_AFTER_INSTALL="share/icons share/applications"

termux_step_pre_configure() {
	LDFLAGS+=" -landroid-glob"
}

termux_step_make_install() {
	cd $TERMUX_PKG_SRCDIR

	./bootstrap.py

	./waf configure \
		--prefix=$TERMUX_PREFIX \
		--disable-gl \
		--disable-jpeg \
		--disable-lcms2 \
		--enable-libarchive \
		--disable-libass \
		--enable-lua \
		--enable-pulse \
		--enable-openal \
		--enable-caca \
		--disable-alsa \
		--disable-x11

	./waf -v install

	# Use opensles audio out be default:
	mkdir -p $TERMUX_PREFIX/etc/mpv
	cp $TERMUX_PKG_BUILDER_DIR/mpv.conf $TERMUX_PREFIX/etc/mpv/mpv.conf
}
