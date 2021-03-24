#!/data/data/com.termux/files/usr/bin/sh

echo "Homebrew on Linux Installation"

pkg install -y git

pkg install -y ruby

pkg install -y curl

pkg install -y clang

pkg install -y proot

pkg install -y make

echo "Get a copy of linuxbrew:"

git clone https://github.com/Linuxbrew/brew.git ~/prefix/brew

cd ~/prefix/brew

alias brew="termux-chroot $PWD/bin/brew"
