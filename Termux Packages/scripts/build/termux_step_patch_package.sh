termux_step_patch_package() {
	[ "$TERMUX_PKG_METAPACKAGE" = "true" ] && return

	cd "$TERMUX_PKG_SRCDIR"
	local DEBUG_PATCHES=""
	if [ "$TERMUX_DEBUG" = "true" ]; then
		DEBUG_PATCHES=$(find $TERMUX_PKG_BUILDER_DIR -mindepth 1 -maxdepth 1 -name \*.patch.debug)
	fi
	if [ "$TERMUX_PKG_QUICK_REBUILD" = "false" ]; then
		# Suffix patch with ".patch32" or ".patch64" to only apply for these bitnesses:
		shopt -s nullglob
		for patch in $TERMUX_PKG_BUILDER_DIR/*.patch{$TERMUX_ARCH_BITS,} $DEBUG_PATCHES; do
			test -f "$patch" && sed "s%\@TERMUX_PREFIX\@%${TERMUX_PREFIX}%g" "$patch" | \
				sed "s%\@TERMUX_HOME\@%${TERMUX_ANDROID_HOME}%g" | \
				patch --silent -p1
		done
		shopt -u nullglob
	fi
}
