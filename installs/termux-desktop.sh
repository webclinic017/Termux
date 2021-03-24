#!/data/data/com.termux/files/usr/bin/sh

echo "Termux Desktop Install\n"

git clone --depth=1 https://github.com/adi1090x/termux-desktop.git

echo "Warning : I'm assuming that you're doing this on a fresh termux install. If not, I'll suggest you to do so. However the setup.sh script backup every file it replace, It's still recommended that you manually backup your files in order to avoid conflicts.\n"

echo "Change to cloned directory and run setup.sh with --install option\n"

cd termux-desktop

chmod +x setup.sh

sh setup.sh --install

