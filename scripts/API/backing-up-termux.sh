#!/data/data/com.termux/files/usr/bin/sh

echo "Backing up Termux\n"

echo "In this example, a backup of both home and sysroot will be shown. The resulting archive will be stored on your shared storage (/sdcard) and compressed with gzip.\n"

echo "Ensure that storage permission is granted"

termux-setup-storage

echo "Go to Termux base directory\n"

cd /data/data/com.termux/files

echo "Backing up files\n"

tar -zcvf /sdcard/github/Termux/home/termux-backup.tar.gz home usr

echo "Backup should be finished without any error. There shouldn't be any permission denials unless the user abused root permissions. Warnings about sockets are okay.\n"

echo "Warning: never store your backups in Termux private directories. Their paths may look like\n"

echo "/data/data/com.termux"

echo "private Termux directory on internal storage\n"

echo "/sdcard/Android/data/com.termux"

echo "private Termux directory on shared storage\n"

echo "/storage/XXXX-XXXX/Android/data/com.termux"

echo "private Termux directory on external storage, XXXX-XXXX is the UUID of your micro-sd card.\n"

echo "${HOME}/storage/external-1\n"

echo "Once you clear Termux data from settings, these directories are erased too."
