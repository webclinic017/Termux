#!/data/data/com.termux/files/usr/bin/sh

# FTP Install

echo "FTP Install"

source $PREFIX/profile.d/start-services

sv-enable ftpd

sv up ftpd
