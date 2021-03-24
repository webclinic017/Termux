#!/data/data/com.termux/files/usr/bin/sh
set -e -u

SCRIPTNAME=termux-wifi-enable

show_usage () {
        echo "Usage: $SCRIPTNAME [true | false]"
        echo "Toggle Wi-Fi On/Off"
        exit 1
}

if [ "$#" -ne 1 ]; then
        show_usage
fi

case $1 in
        true|false);;
        *) show_usage;;
esac

/data/data/com.termux/files/usr/libexec/termux-api WifiEnable --ez enabled "$1"
