#!/data/data/com.termux/files/usr/bin/sh

# CMSmap

echo "CMSmap"

git clone https://github.com/Dionach/CMSmap.git

mv -v CMSmap /sdcard/python/

cd /sdcard/python/CMSmap

rm -rf .gitignore DISCLAIMER.txt LICENSE.txt .github/ .git/

chmod +x cmsmap.py

python3 setup.py install

python3 cmsmap.py -h
