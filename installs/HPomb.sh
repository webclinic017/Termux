#!/data/data/com.termux/files/usr/bin/sh

echo "HPomb Install"

pkg install git

pkg install python

git clone https://github.com/HoneyPots0/HPomb.git

cd HPomb

chmod +x hpomb.py

python3 -m pip install -r requirements.txt

python3 hpomb.py

mv -v .git DOTgit

rm -rf LICENSE
