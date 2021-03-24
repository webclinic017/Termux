#!/data/data/com.termux/files/usr/bin/sh

echo "Termux Sudo Install"

pkg install ncurses-utils

git clone https://gitlab.com/st42/termux-sudo

cat termux-sudo/sudo > /data/data/com.termux/files/usr/bin/sudo

chmod 700 /data/data/com.termux/files/usr/bin/sudo

rm -rf termux-sudo/
