#!/data/data/com.termux/files/usr/bin/sh

echo "SocialFish Install"

cd /sdcard/github/Termux/python/

apt update -y

apt upgrade -y

apt install git -y

apt install python -y

apt install python2 -y

git clone https://github.com/UndeadSec/SocialFish.git

cd SocialFish

chmod +x *

python3 -m pip install -r requirements.txt

echo "usage :"

python3 SocialFish.py

echo "Now select your target and it will generate an url using Ngrok"

sleep 5s

mv -v .git DOTgit 

mv -v .github DOTgithub

rm -rf CODE_OF_CONDUCT.md CONTRIBUTING.md LICENSE
