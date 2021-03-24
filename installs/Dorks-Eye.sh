#!/data/data/com.termux/files/usr/bin/sh

# Dorks Eye Install

echo "Dorks Eye Install"

git clone https://github.com/BullsEye0/dorks-eye.git

mv -v dorks-eye /sdcard/python/

cd /sdcard/python/dorks-eye

python3 -m pip install -r requirements.txt

rm -rf .git LICENSE Img/
