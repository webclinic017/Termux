#!/usr/bin/env bash
set -e -u

PACKAGES=""

# For en_US.UTF-8 locale.
PACKAGES+=" locales"

# To provide /usr/bin/python as symlink to /usr/bin/python3
PACKAGES+=" python-is-python3"

# Used by build-package.sh and CI/CD scripts.
PACKAGES+=" curl"
PACKAGES+=" gnupg"
PACKAGES+=" jq"

# Used for fetching package sources from Git repositories.
PACKAGES+=" git"

# Used for extracting package sources.
PACKAGES+=" lzip"
PACKAGES+=" tar"
PACKAGES+=" unzip"

# Used by common build systems.
PACKAGES+=" autoconf"
PACKAGES+=" automake"
PACKAGES+=" autopoint"
PACKAGES+=" bison"
PACKAGES+=" flex"
PACKAGES+=" g++"
PACKAGES+=" g++-multilib"
PACKAGES+=" gawk"
PACKAGES+=" gettext"
PACKAGES+=" gperf"
PACKAGES+=" intltool"
PACKAGES+=" libglib2.0-dev"
PACKAGES+=" libtool-bin"
PACKAGES+=" libltdl-dev"
PACKAGES+=" m4"
PACKAGES+=" pkg-config"
PACKAGES+=" scons"

# Used to generate package documentation.
PACKAGES+=" asciidoc"
PACKAGES+=" asciidoctor"
PACKAGES+=" groff"
PACKAGES+=" help2man"
PACKAGES+=" pandoc"
PACKAGES+=" python3-docutils"
PACKAGES+=" python3-recommonmark"
PACKAGES+=" python3-sphinx"
PACKAGES+=" texinfo"
PACKAGES+=" xmlto"

# Needed by python modules (e.g. asciinema) and some build systems.
PACKAGES+=" python3.7"
PACKAGES+=" python3.8"
PACKAGES+=" python3-setuptools"

# Needed by package bc.
PACKAGES+=" ed"

# Provides utility hexdump which is needed by package bitcoin.
PACKAGES+=" bsdmainutils"

# Needed by package ccnet.
PACKAGES+=" valac"

# Needed by package dbus-glib.
PACKAGES+=" libdbus-1-dev"

# Needed by package ghostscript.
PACKAGES+=" libexpat1-dev"
PACKAGES+=" libjpeg-dev"

# Needed by package luarocks.
PACKAGES+=" lua5.3"

# Used bt host build of package mariadb.
PACKAGES+=" libncurses5-dev"

# Needed by packages mkvtoolnix and ruby.
PACKAGES+=" ruby"

# Needed by host build of package nodejs.
PACKAGES+=" libc-ares-dev"
PACKAGES+=" libicu-dev"

# Needed by php.
PACKAGES+=" re2c"

# Needed by package rust.
PACKAGES+=" libssl-dev" # Needed to build Rust

# Needed for package smalltalk.
PACKAGES+=" libsigsegv-dev"
PACKAGES+=" zip"

# Needed by package swi-prolog.
PACKAGES+=" openssl"
PACKAGES+=" zlib1g-dev"
PACKAGES+=" libssl-dev:i386"
PACKAGES+=" zlib1g-dev:i386"

# So we don't build llvm for build.
PACKAGES+=" llvm-8-tools"

# For swift.
PACKAGES+=" clang-9"
PACKAGES+=" libtinfo5"
PACKAGES+=" lld"

# Needed by gitea.
PACKAGES+=" npm"

# Needed by libduktape (2.5.0 still uses python2 unfortunately)
PACKAGES+=" python-yaml"

# Java.
PACKAGES+=" openjdk-8-jdk"

# Needed by packages in unstable repository.
PACKAGES+=" docbook-to-man"
PACKAGES+=" docbook-utils"
PACKAGES+=" erlang-nox"
PACKAGES+=" libgc-dev"
PACKAGES+=" libgmp-dev"
PACKAGES+=" libunistring-dev"
PACKAGES+=" llvm-9-dev"

# Needed by packages in X11 repository.
PACKAGES+=" docbook-xsl-ns"
PACKAGES+=" gnome-common"
PACKAGES+=" gobject-introspection"
PACKAGES+=" gtk-3-examples"
PACKAGES+=" gtk-doc-tools"
PACKAGES+=" itstool"
PACKAGES+=" libgdk-pixbuf2.0-dev"
PACKAGES+=" python3-xcbgen"
PACKAGES+=" xfonts-utils"

# Do not require sudo if already running as root.
if [ "$(id -u)" = "0" ]; then
	SUDO=""
else
	SUDO="sudo"
fi

# Allow 32-bit packages.
$SUDO dpkg --add-architecture i386
$SUDO apt-get -yq update

$SUDO DEBIAN_FRONTEND=noninteractive \
	apt-get install -yq --no-install-recommends $PACKAGES

$SUDO locale-gen --purge en_US.UTF-8
echo -e 'LANG="en_US.UTF-8"\nLANGUAGE="en_US:en"\n' | $SUDO tee -a /etc/default/locale

$SUDO mkdir -p /data/data/com.termux/files/usr
$SUDO chown -R $(whoami) /data
