#!/data/data/com.termux/files/usr/bin/sh

# Copy from $HOME to Termux Git Repo
#		and
# Copy from Termux Git Repo to $HOME

echo "Copy from Documents to Termux Git Repo"
cp -R ~/Documents/ /sdcard/github/Termux/

echo "Copy from apps to Termux Git Repo"
cp -R ~/apps/ /sdcard/github/Termux/

echo "Copy from installs to Termux Git Repo"
cp -R ~/installs/ /sdcard/github/Termux/

echo "Copy from links to Termux Git Repo"
cp -R ~/links/ /sdcard/github/Termux/

echo "Copy from python to Termux Git Repo"
cp -R ~/python/ /sdcard/github/Termux/

echo "Copy from scripts to Termux Git Repo"
cp -R ~/scripts/ /sdcard/github/Termux/

echo "Copy from Termux Git Repo to Documents"
cp -R /sdcard/github/Termux/Documents ~/

echo "Copy from Termux Git Repo to apps"
cp -R /sdcard/github/Termux/apps ~/

echo "Copy from Termux Git Repo to installs"
cp -R /sdcard/github/Termux/installs ~/

echo "Copy from Termux Git Repo to links"
cp -R /sdcard/github/Termux/links ~/

echo "Copy from Termux Git Repo to python"
cp -R /sdcard/github/Termux/python ~/

echo "Copy from Termux Git Repo to scripts"
cp -R /sdcard/github/Termux/scripts ~/
