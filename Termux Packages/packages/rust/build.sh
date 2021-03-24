TERMUX_PKG_HOMEPAGE=https://www.rust-lang.org/
TERMUX_PKG_DESCRIPTION="Systems programming language focused on safety, speed and concurrency"
TERMUX_PKG_LICENSE="MIT"
TERMUX_PKG_MAINTAINER="Kevin Cotugno @kcotugno"
TERMUX_PKG_VERSION=1.42.0
TERMUX_PKG_SRCURL=https://static.rust-lang.org/dist/rustc-$TERMUX_PKG_VERSION-src.tar.xz
TERMUX_PKG_SHA256=aa5b4c0f2bac33cc26a11523fce9b0f120d2eff510ed148ae7c586501481ed04
TERMUX_PKG_DEPENDS="libc++, clang, openssl, lld, zlib, libllvm"
termux_step_configure() {
	termux_setup_cmake
	termux_setup_rust

	# it breaks building rust tools without doing this because it tries to find
	# ../lib from bin location:
	# this is about to get ugly but i have to make sure a rustc in a proper bin lib
	# configuration is used otherwise it fails a long time into the build...
	# like 30 to 40 + minutes ... so lets get it right

	# upstream only tests build ver one version behind $TERMUX_PKG_VERSION
	rustup install 1.41.1
	rustup default 1.41.1-x86_64-unknown-linux-gnu
	export PATH=$HOME/.rustup/toolchains/1.41.1-x86_64-unknown-linux-gnu/bin:$PATH
	local RUSTC=$(which rustc)
	local CARGO=$(which cargo)

	sed "s%\\@TERMUX_PREFIX\\@%$TERMUX_PREFIX%g" \
		$TERMUX_PKG_BUILDER_DIR/config.toml \
		| sed "s%\\@TERMUX_STANDALONE_TOOLCHAIN\\@%$TERMUX_STANDALONE_TOOLCHAIN%g" \
		| sed "s%\\@triple\\@%$CARGO_TARGET_NAME%g" \
		| sed "s%\\@RUSTC\\@%$RUSTC%g" \
		| sed "s%\\@CARGO\\@%$CARGO%g" \
		> config.toml

	local env_host=$(printf $CARGO_TARGET_NAME | tr a-z A-Z | sed s/-/_/g)
	export LD_LIBRARY_PATH=$TERMUX_PKG_BUILDDIR/build/x86_64-unknown-linux-gnu/stage2/lib
	export ${env_host}_OPENSSL_DIR=$TERMUX_PREFIX
	export X86_64_UNKNOWN_LINUX_GNU_OPENSSL_LIB_DIR=/usr/lib/x86_64-linux-gnu
	export X86_64_UNKNOWN_LINUX_GNU_OPENSSL_INCLUDE_DIR=/usr/include
	export PKG_CONFIG_ALLOW_CROSS=1
	# for backtrace-sys
	export CC_x86_64_unknown_linux_gnu=gcc
	export CFLAGS_x86_64_unknown_linux_gnu="-O2"
	unset CC CXX CPP LD CFLAGS CXXFLAGS CPPFLAGS LDFLAGS PKG_CONFIG AR RANLIB
	# we can't use -L$PREFIX/lib since it breaks things but we need to link against libLLVM-9.so
	ln -sf $PREFIX/lib/libLLVM-9.0.1.so $TERMUX_STANDALONE_TOOLCHAIN/sysroot/usr/lib/$TERMUX_HOST_PLATFORM/$TERMUX_PKG_API_LEVEL/

	# rust checks libs in PREFIX/lib because both host and target are x86_64. It then can't find libc.so and libdl.so because rust program doesn't 
	# know where those are. Putting them temporarly in $PREFIX/lib prevents that failure
	
	if [ $TERMUX_ARCH = "x86_64" ]; then
		cp $TERMUX_STANDALONE_TOOLCHAIN/sysroot/usr/lib/x86_64-linux-android/$TERMUX_PKG_API_LEVEL/libc.so $TERMUX_PREFIX/lib/
		cp $TERMUX_STANDALONE_TOOLCHAIN/sysroot/usr/lib/x86_64-linux-android/$TERMUX_PKG_API_LEVEL/libdl.so $TERMUX_PREFIX/lib/
		mv $TERMUX_PREFIX/lib/libtinfo.so.6 $TERMUX_PREFIX/lib/libtinfo.so.6.tmp	
	fi
}

termux_step_make() {
	return 0;
}
termux_step_make_install() {
	$TERMUX_PKG_SRCDIR/x.py dist librustc --host $CARGO_TARGET_NAME --target $CARGO_TARGET_NAME --target wasm32-unknown-unknown  
	$TERMUX_PKG_SRCDIR/x.py dist rustc-dev --host $CARGO_TARGET_NAME --target $CARGO_TARGET_NAME --target wasm32-unknown-unknown
	$TERMUX_PKG_SRCDIR/x.py install --stage 2 --host $CARGO_TARGET_NAME --target $CARGO_TARGET_NAME --target wasm32-unknown-unknown 
	tar xvf build/dist/rustc-dev-$TERMUX_PKG_VERSION-$CARGO_TARGET_NAME.tar.gz
	./rustc-dev-$TERMUX_PKG_VERSION-$CARGO_TARGET_NAME/install.sh --prefix=$TERMUX_PREFIX

	cd "$TERMUX_PREFIX/lib"
	rm -f libc.so libdl.so
	if [ $TERMUX_ARCH = "x86_64" ]; then
		mv $TERMUX_PREFIX/lib/libtinfo.so.6.tmp $TERMUX_PREFIX/lib/libtinfo.so.6
	fi
	
	ln -sf rustlib/$CARGO_TARGET_NAME/lib/*.so .
	ln -sf $TERMUX_PREFIX/bin/lld $TERMUX_PREFIX/bin/rust-lld
	
	cd "$TERMUX_PREFIX/lib/rustlib"
	rm -rf components \
		install.log \
		uninstall.sh \
		rust-installer-version \
		manifest-* \
		x86_64-unknown-linux-gnu
	rm $TERMUX_STANDALONE_TOOLCHAIN/sysroot/usr/lib/$TERMUX_HOST_PLATFORM/$TERMUX_PKG_API_LEVEL/libLLVM-9.0.1.so 

}
termux_step_post_massage() {
	if [ $TERMUX_ARCH = "x86_64" ]; then
		rm lib/libtinfo.so.6
	fi
}

