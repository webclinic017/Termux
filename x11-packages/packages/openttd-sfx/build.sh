TERMUX_PKG_HOMEPAGE=https://bundles.openttdcoop.org/opensfx
TERMUX_PKG_DESCRIPTION="Free sound set for openttd"

# Here should be CCSP, but unfortunately Bintray doesn't allow
# such license as well as other Creative Commons licenses except
# the CC0.
TERMUX_PKG_LICENSE="CC0-1.0"

TERMUX_PKG_MAINTAINER="Leonid Pliushch <leonid.pliushch@gmail.com>"
TERMUX_PKG_VERSION=0.2.3
TERMUX_PKG_REVISION=21
TERMUX_PKG_SRCURL=https://cdn.openttd.org/opensfx-releases/$TERMUX_PKG_VERSION/opensfx-$TERMUX_PKG_VERSION-all.zip
TERMUX_PKG_SHA256=6831b651b3dc8b494026f7277989a1d757961b67c17b75d3c2e097451f75af02
TERMUX_PKG_BUILD_IN_SRC=true
TERMUX_PKG_PLATFORM_INDEPENDENT=true

termux_step_make_install() {
	install -d "$TERMUX_PREFIX"/share/openttd/data
	install -m600 opensfx.* "$TERMUX_PREFIX"/share/openttd/data
}
