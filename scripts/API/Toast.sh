#!/data/data/com.termux/files/usr/bin/bash
set -e -u

SCRIPTNAME=termux-toast
show_usage () {
    echo "Usage: termux-toast [-b bgcolor] [-c color] [-g gravity] [-s] [text]"
    echo "Show text in a Toast (a transient popup). The text to show is either supplied as arguments or read from stdin if no arguments are given."
    echo " -h  show this help"
    echo " -b  set background color (default: gray)"
    echo " -c  set text color (default: white)"
    echo " -g  set position of toast: [top, middle, or bottom] (default: middle)"
    echo " -s  only show the toast for a short while"
    echo "NOTE: color can be a standard name (i.e. red) or 6 / 8 digit hex value (i.e. \"#FF0000\" or \"#FFFF0000\") where order is (AA)RRGGBB. Invalid color will revert to default value"
    exit 0
}

PARAMS=""
while getopts :hsc:b:g: option
do
    case "$option" in
        h) show_usage;;
        s) PARAMS+=" --ez short true";;
        c) PARAMS+=" --es text_color $OPTARG";;
        b) PARAMS+=" --es background $OPTARG";;
        g) PARAMS+=" --es gravity $OPTARG";;
        ?) echo "$SCRIPTNAME: illegal option -$OPTARG"; exit 1;
    esac
done
shift $((OPTIND-1))

CMD="/data/data/com.termux/files/usr/libexec/termux-api Toast $PARAMS"

if [ $# = 0 ]; then
    $CMD
else
    echo "$@" | $CMD
fi
