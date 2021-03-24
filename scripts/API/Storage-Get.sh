#!/data/data/com.termux/files/usr/bin/sh
set -e -u

SCRIPTNAME=termux-storage-get
show_usage () {
    echo "Usage: $SCRIPTNAME output-file"
    echo "Request a file from the system and output it to the specified file."
    exit 0
}


while getopts :h option
do
    case "$option" in
        h) show_usage;;
        ?) echo "$SCRIPTNAME: illegal option -$OPTARG"; exit 1;
    esac
done
shift $((OPTIND-1))

if [ $# -gt 1 ]; then echo "$SCRIPTNAME: too many arguments"; exit 1; fi
if [ $# -lt 1 ]; then echo "$SCRIPTNAME: no output file specified"; exit 1; fi

/data/data/com.termux/files/usr/libexec/termux-api StorageGet --es file "$(realpath "$1")"
