#!/data/data/com.termux/files/usr/bin/sh

echo "Rclone Install"

curl -s https://rclone.org/install.sh |  bash > /dev/null 2>&1

curl -s https://rclone.org/install.sh | bash -s beta > /dev/null 2>&1

go get github.com/rclone/rclone

go get github.com/rclone/rclone@master

curl -O https://downloads.rclone.org/rclone-current-linux-amd64.zip

unzip rclone-current-linux-amd64.zip

cd -R rclone-current-linux-amd64

cp -R rclone-current-linux-amd64 /data/data/com.termux/files/usr/bin/rclone

rm -rf rclone-current-linux-amd64

cd /data/data/com.termux/files/usr/bin/rclone/

chown root:root /usr/bin/rclone

chmod 755 /usr/bin/rclone
