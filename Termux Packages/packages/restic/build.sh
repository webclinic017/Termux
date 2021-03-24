TERMUX_PKG_HOMEPAGE=https://restic.net/
TERMUX_PKG_DESCRIPTION="Fast, secure, efficient backup program"
TERMUX_PKG_LICENSE="BSD"
TERMUX_PKG_MAINTAINER="Leonid Plyushch <leonid.plyushch@gmail.com>"
TERMUX_PKG_VERSION=0.9.6
TERMUX_PKG_REVISION=1
# Use a snapshot to fix building with go 1.13:
#TERMUX_PKG_SRCURL=https://github.com/restic/restic/archive/v$TERMUX_PKG_VERSION.tar.gz
TERMUX_PKG_SRCURL=https://github.com/restic/restic/archive/604b18aa7426148a55f76307ca729e829ff6b61d.zip
TERMUX_PKG_SHA256=e1d8c977c541d9503a6aba643cf10896f0de488a20db96f162a3e91a4e9def70
TERMUX_PKG_SUGGESTS="openssh, rclone"

termux_step_make() {
	termux_setup_golang

	export GOPATH=$TERMUX_PKG_BUILDDIR
	mkdir -p "$GOPATH"/src/github.com/restic

	ln -sf "$TERMUX_PKG_SRCDIR" "$GOPATH"/src/github.com/restic/restic
	cd "$GOPATH"/src/github.com/restic/restic

	(
		# Separately building for host so we can generate manpages.
		unset GOOS GOARCH CGO_LDFLAGS
		unset CC CXX CFLAGS CXXFLAGS LDFLAGS
		go build -ldflags "-X 'main.version=${TERMUX_PKG_VERSION}'" ./cmd/...
		./restic generate --man doc/man
		rm -f ./restic
	)

	go build -ldflags "-X 'main.version=${TERMUX_PKG_VERSION}'" ./cmd/...
}

termux_step_make_install() {
	cd "$GOPATH"/src/github.com/restic/restic
	install -Dm700 restic "$TERMUX_PREFIX"/bin/restic
	install -Dm600 -t "$TERMUX_PREFIX/share/man/man1/" doc/man/*.1
}
