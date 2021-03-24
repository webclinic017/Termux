#!/data/data/com.termux/files/usr/bin/sh

# Termux API Install

echo "Termux API Install"

pkg install termux-api

apt update -y && apt upgrade -y

pkg update -y && pkg upgrade -y
