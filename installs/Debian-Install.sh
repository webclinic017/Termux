#!/data/data/com.termux/files/usr/bin/sh

# Debian Install

echo "Debian Install"

pkg install debootstrap proot wget

uname -m

debootstrap --arch=ARCH stable debian-stable http://ftp.debian.org/debian/ 

echo "ARCH is arm64 for aarch64, etc."

echo "Then setup proot to mount the container."

echo "A sample proot start.sh includes:"

#!/data/data/com.termux/files/usr/bin/sh proot \ -0 \ --link2symlink \ -r ~/debian-stable \ -b /dev/ \ -b /sys/ \ -b /proc/ \ -b /data/data/com.termux/files/home \ /usr/bin/env \ -i \ HOME=/root \ TERM="xterm-256color" \ PATH=/bin:/usr/bin:/sbin:/usr/sbin \ /bin/bash --login

sh start.sh

echo "Or you can install with"

echo "wget -q https://raw.githubusercontent.com/sp4rkie/debian-on-termux/master/debian_on_termux_10.sh && sh debian_on_termux_10.sh"
sleep 10s

echo "DONE"
