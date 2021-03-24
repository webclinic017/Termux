#!/data/data/com.termux/files/usr/bin/sh

# AutoPixie WPS Scan Tool Install

echo "AutoPixie WPS Scan Tool Install"

cd /sdcard/apps

pip3 install requests

echo "How to use AutoPixie Wps Scan Tool in Termux"

git clone https://github.com/nxxxu/AutoPixieWps.git

cd AutoPixieWps

rm -rf .git/

chmod +x autopixie.py

python3 autopixie.py
