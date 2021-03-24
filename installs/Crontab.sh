#!/data/data/com.termux/files/usr/bin/sh

# Crontab Install

echo "Crontab Install"

pkg install -y cronie

pkg install -y termux-services

sv-enable crond

crontab -e

mkdir -p ~/crontab-testing
