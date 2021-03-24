#!/data/data/com.termux/files/usr/bin/sh

echo "Restoring Termux\n"

echo "Go to Termux base directory\n"

cd /data/data/com.termux/files

echo "Extract home and usr with overwriting everything and deleting stale files\n"

tar -zxf /sdcard/termux-backup.tar.gz --recursive-unlink --preserve-permissions

exit
