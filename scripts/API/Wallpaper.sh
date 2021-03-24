#!/data/data/com.termux/files/usr/bin/bash

set -e

SCRIPTNAME=termux-wallpaper
show_usage () {
	echo "Change wallpaper on your device"
	echo
	echo "Usage: $SCRIPTNAME [options]"
	echo "-h         show this help"
	echo "-f <file>  set wallpaper from file"
	echo "-u <url>   set wallpaper from url resource"
	echo "-l         set wallpaper for lockscreen (Nougat and later)"
	exit 1
}

OPT_LS=""
OPT_FILE=""
OPT_URL=""

while getopts :h,:l,f:,u: option
do
	case "$option" in
		h) show_usage ;;
		l) OPT_LS="true" ;;
		f) path="$(realpath "$OPTARG")"
			if [[ ! -f "$path" ]]; then
				echo "$SCRIPTNAME: $path is not a file!"
				exit 1
			fi
			OPT_FILE="$path" ;;
		u) OPT_URL="$OPTARG" ;;
		?) echo "$SCRIPTNAME: illegal option -$OPTARG"; exit 1 ;;
	esac
done

if [[ -z "$OPT_FILE""$OPT_URL" ]]; then
	echo "$SCRIPTNAME: you must specify either -f or -u"
	exit 1
elif [[ -n "$OPT_FILE" ]] && [[ -n "$OPT_URL" ]]; then
	echo "$SCRIPTNAME: you must specify either -f or -u, but not both"
	exit 1
fi

shift $((OPTIND - 1))
if [ $# != 0 ]; then echo "$SCRIPTNAME: too many arguments"; exit 1; fi

set --
[ -n "$OPT_LS" ]   && set -- "$@" --ez lockscreen "$OPT_LS"
[ -n "$OPT_FILE" ] && set -- "$@" --es file "$OPT_FILE"
[ -n "$OPT_URL" ]  && set -- "$@" --es url "$OPT_URL"
/data/data/com.termux/files/usr/libexec/termux-api Wallpaper "$@"
