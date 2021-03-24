#!/data/data/com.termux/files/usr/bin/sh

# ChromeOS qemu Install

echo "ChromeOS qemu Install"

echo "Update and Upgrade Packages"

pkg update -y && pkg upgrade -y

echo "Setup storage"

termux-setup-storage

echo "Install termux-tools

pkg install -y termux-tools

echo "Install git"

pkg install -y git

echo "Install wget"

pkg install -y wget

echo "Install proot"

pkg install -y proot

echo "Install coreutils"

pkg install -y coreutils

echo "Install util-linux"

pkg install -y util-linux

echo "Install net-tools"

pkg install -y net-tools

echo "Install openssh"

pkg install -y openssh

echo "Add the X/GUI Repos"

wget https://raw.githubusercontent.com/xeffyr/termux-x-repository/master/enablerepo.sh

bash enablerepo.sh

echo "Install QEMU"

pkg install -y qemu-system

echo "Clone ChromeOS qemu Repo"

git clone https://github.com/pwdonald/chromeos-qemu-docker.git
