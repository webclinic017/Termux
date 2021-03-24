#!/data/data/com.termux/files/usr/bin/sh

echo "Restoring Termux\n"

echo "Here will be assumed that you have backed up both home and usr directory into same archive. Please note that all files would be overwritten during the process.\n"

echo "Ensure that storage permission is granted"

termux-setup-storage

echo "Go to Termux base directory\n"

cd /data/data/com.termux/files

echo "Extract home and usr with overwriting everything and deleting stale files\n"

tar -zxf /sdcard/termux-backup.tar.gz --recursive-unlink --preserve-permissions

echo 'Now close Termux with the "exit" button from notification and open it again.'
