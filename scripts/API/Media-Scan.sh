#!/data/data/com.termux/files/usr/bin/bash
set -e -u

SCRIPTNAME=termux-media-scan
show_usage () {
	echo "Usage: $SCRIPTNAME [-v] [-r] file [file...]"
	echo "Scan the specified file(s) and add it to the media content provider."
	echo "  -r  scan directories recursively"
	echo "  -v  verbose mode"
	exit 0
}

get_paths() {
	for ARG in "$@"; do
		if [[ -e "$ARG" ]]; then
			realpath "$ARG"
		else 
			if [[ "$ARG" =~ ^/ ]]; then
				echo "$ARG"
			else
				echo "$(pwd)/$ARG"
			fi
		fi
	done
}

PARAMS="--esa paths"
while getopts :hrv option
do
	case "$option" in
		h) show_usage;;
		r) PARAMS="--ez recursive true $PARAMS";;
		v) PARAMS="--ez verbose true $PARAMS";;
		?) echo "$SCRIPTNAME: illegal option -$OPTARG"; exit 1;
	esac
done
shift $((OPTIND-1))

if [ $# = 0 ]; then echo "$SCRIPTNAME: missing file argument"; exit 1; fi

PATHS=`get_paths "$@" | sed ':a;N;$!ba;s/,/\\\\,/g;s/\n/,/g'`
/data/data/com.termux/files/usr/libexec/termux-api MediaScanner $PARAMS "$PATHS"
