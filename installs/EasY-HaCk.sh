#!/data/data/com.termux/files/usr/bin/sh

echo "EasY-HaCk Install"

cd /data/data/com.termux/files/home

git clone https://github.com/sabri-zaki/EasY_HaCk

cd EasY_HaCk/

chmod +x install.sh

sh install.sh

mv -v .git/ DOTgit

mv -v .github/ DOTgithub

rm -rf CONTRIBUTING.md LICENSE
