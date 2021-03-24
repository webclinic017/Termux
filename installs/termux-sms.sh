#!/data/data/com.termux/files/usr/bin/sh

echo "Termux SMS Install"

echo "Send text message in termux."

pkg install git -y

git clone https://github.com/ZechBron/Termux-SMS

cd Termux-SMS

chmod +x setup.sh

echo "It is recommended to run setup.sh first`"

sh setup.sh

sh TermuxSMS.sh

mv -v .git DOTgit
