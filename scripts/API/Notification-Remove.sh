#!/data/data/com.termux/files/usr/bin/sh
set -e -u

SCRIPTNAME=termux-notification-remove
show_usage () {
    echo "Usage: $SCRIPTNAME notification-id"
    echo "Remove a notification previously shown with termux-notification --id."
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

if [ $# != 1 ]; then echo "$SCRIPTNAME: no notification id specified"; exit 1; fi

/data/data/com.termux/files/usr/libexec/termux-api NotificationRemove --es id "$1"
