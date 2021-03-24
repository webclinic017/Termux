#!/data/data/com.termux/files/usr/bin/sh
set -e -u

SCRIPTNAME=termux-location
show_usage () {
    echo "usage: $SCRIPTNAME [-p provider] [-r request]"
    echo "Get the device location."
    echo "  -p provider  location provider [gps/network/passive] (default: gps)"
    echo "  -r request   kind of request to make [once/last/updates] (default: once)"
    exit 0
}

validate_provider () {
    PROVIDER=$1
    case "$PROVIDER" in
        gps) ;;
        network) ;;
        passive) ;;
        *) echo "$SCRIPTNAME: Unsupported provider: '$PROVIDER'"; exit 1;;
    esac
}

validate_request () {
    REQUEST=$1
    case "$REQUEST" in
        once) ;;
        last) ;;
        updates) ;;
        *) echo "$SCRIPTNAME: Unsupported request: '$REQUEST'"; exit 1;;
    esac
}

PARAMS=""

while getopts :hr:p: option
do
    case "$option" in
        h) show_usage;;
        r) validate_request "$OPTARG"; PARAMS="$PARAMS --es request $OPTARG";;
        p) validate_provider "$OPTARG"; PARAMS="$PARAMS --es provider $OPTARG";;
        ?) echo "$SCRIPTNAME: illegal option -$OPTARG"; exit 1;
    esac
done
shift $((OPTIND-1))

if [ $# != 0 ]; then echo "$SCRIPTNAME: too many arguments"; exit 1; fi

/data/data/com.termux/files/usr/libexec/termux-api Location $PARAMS
