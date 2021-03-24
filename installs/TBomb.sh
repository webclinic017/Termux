#!/data/data/com.termux/files/usr/bin/sh

echo "TBomb Install"

cd /sdcard/apps/

pkg install git -y

pkg install python -y

git clone https://github.com/TheSpeedX/TBomb.git

cd TBomb

python3 -m pip install -r requirements.txt

chmod +x TBomb.sh

echo "Cleaing Up Repo"

rm -rf LICENSE .gitignore

sh TBomb.sh
