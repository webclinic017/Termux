TERMUX_PKG_HOMEPAGE=https://proj.org
TERMUX_PKG_DESCRIPTION="Generic coordinate transformation software"
TERMUX_PKG_LICENSE="MIT"
TERMUX_PKG_MAINTAINER="Henrik Grimler @Grimler91"
TERMUX_PKG_VERSION=7.2.0
TERMUX_PKG_SRCURL=https://github.com/OSGeo/proj.4/archive/${TERMUX_PKG_VERSION}.tar.gz
TERMUX_PKG_SHA256=a2cc85dc3a9a32284fddb6fe240431819324f21df538773a83a90d4352189912
TERMUX_PKG_DEPENDS="libc++, libsqlite, sqlite, libtiff, libcurl"
TERMUX_PKG_BREAKS="proj-dev"
TERMUX_PKG_REPLACES="proj-dev"
