#!/data/data/com.termux/files/usr/bin/sh

# Copy $HOME to Termux Git Repo

echo "Copy Documents to Termux Git Repo"
cp -R ~/Documents/ /sdcard/github/Termux/

echo "Copy apps to Termux Git Repo"
cp -R ~/apps/ /sdcard/github/Termux/

echo "Copy installs to Termux Git Repo"
cp -R ~/installs/ /sdcard/github/Termux/

echo "Copy links to Termux Git Repo"
cp -R ~/links/ /sdcard/github/Termux/

echo "Copy python to Termux Git Repo"
cp -R ~/python/ /sdcard/github/Termux/

echo "Copy scripts to Termux Git Repo"
cp -R ~/scripts/ /sdcard/github/Termux/
