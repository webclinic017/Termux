#!/data/data/com.termux/files/usr/bin/sh

# OpenSSH Install

echo "OpenSSH Install"

pkg install -y openssh

apt update -y && apt upgrade -y

passwd
