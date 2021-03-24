#!/data/data/com.termux/files/usr/bin/sh

# Termux Speak Install

echo "Termux Speak Install"

echo "Change Directory to /sdcard/apps/"

cd /sdcard/apps/

git clone https://github.com/TechnicalMujeeb/Termux-speak

cd Termux-speak

chmod +x *

sh install.sh
