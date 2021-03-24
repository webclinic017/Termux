#!/data/data/com.termux/files/usr/bin/sh

echo "KickThemOut Install"

cd /sdcard/apps

git clone https://github.com/roccomuso/kickthemout.git

cd kickthemout

npm install -g --production

echo "Cleaning up Directory"

mv -v .git/ DOTgit

rm -rf .gitignore LICENSE
