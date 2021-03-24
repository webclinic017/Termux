

echo "Volume"

#!/data/data/com.termux/files/usr/bin/sh
#am broadcast --user 0 -a net.dinglish.tasker.[task name] -e [variable name] "[value]" > /dev/null
am broadcast --user 0 -a net.dinglish.tasker.volume -e volume "$1" > /dev/null
