#!/data/data/com.termux/files/usr/bin/bash

echo "Termux Fresh Install"

echo -e "\nGrant Storage Permission"

termux-setup-storage

echo -e "\nUpdating Everything"

apt update -y

apt upgrade -y

pkg update -y

pkg upgrade -y

clear

echo -e "\nMaking Directories"

mkdir -p /sdcard/github/

mkdir -p /sdcard/github/Termux/

mkdir -p /sdcard/github/Termux/apps/

mkdir -p /sdcard/github/Termux/python/

mkdir -p /sdcard/github/Termux/Ruby/

mkdir -p /sdcard/github/Termux/installs/

mkdir -p /sdcard/github/Termux/scripts/

mkdir -p /sdcard/github/Termux/Ruby/Ruby/

mkdir -p /sdcard/github/Termux/Ruby/Perl/

mkdir -p /sdcard/github/Termux/installs/

clear

echo -e "\nInstalling All Packages"

pkg install -y x11-repo 

pkg install -y unstable-repo 

pkg install -y root-repo 

pkg install -y termux-api 

pkg install -y nano 

pkg install -y git 

pkg install -y curl 

pkg install -y dpkg 

pkg install -y wget 

pkg install -y clang 

pkg install -y gitea 

pkg install -y zsh 

pkg install -y gnupg 

pkg install -y python 

pkg install -y python2 

pkg install -y vim 

pkg install -y figlet 

pkg install -y vim-python 

pkg install -y mc 

pkg install -y sox 

pkg install -y pulseaudio 

pkg install -y ffmpeg 

pkg install -y tmux 

pkg install -y libcurl 

pkg install -y coreutils 

pkg install -y termux-tools 

pkg install -y proot 

pkg install -y util-linux 

pkg install -y net-tools 

pkg install -y openssh 

pkg install -y tigervnc 

pkg install -y openbox 

pkg install -y obconf 

pkg install -y xorg-xsetroot 

pkg install -y xcompmgr 

pkg install -y xterm 

pkg install -y polybar 

pkg install -y st 

pkg install -y libnl 

pkg install -y geany 

pkg install -y pcmanfm 

pkg install -y rofi 

pkg install -y feh 

pkg install -y neofetch 

pkg install -y htop 

pkg install -y elinks 

pkg install -y mutt 

pkg install -y xfce4-settings 

pkg install -y fish 

pkg install -y tsu 

pkg install -y termux-tools 

pkg install -y duf 

pkg install -y 

pkg install -y 

pkg install -y 

pkg install -y 

pkg install -y  proj

pkg install -y  wireless-tools

pkg install -y  renameutils

pkg install -y  git-gitk

pkg install -y  coreutils                       >

pkg install -y  jupp

pkg install -y  ocrad

pkg install -y  termux-api

pkg install -y  sleuthkit

pkg install -y  tshark

pkg install -y  libusbmuxd

pkg install -y nmh 

pkg install -y cmatrix

clear

echo -e "\nInstalling All Applications"

apt install -y zip 

apt install -y unzip 

apt install -y rsync 

apt install -y nudoku 

apt install -y caddy

apt update > /dev/null 2>&1

apt --assumees install wget > /dev/null 2>&1

clear

cd /sdcard/github/Termux/installs/

curl -LO https://its-pointless.github.io/setup-pointless-repo.sh | bash

clear

echo -e "\nCaddy Install"

echo "deb [trusted=yes] https://apt.fury.io/caddy/ /" \ | sudo tee -a /etc/apt/sources.list.d>

wget https://github.com/MasterDevX/Termux-ADB/raw/master/InstallTools.sh -q | bash

wget https://raw.githubusercontent.com/nmilosev/termux-fedora/master/termux-fedora.sh | bash

clear

git clone https://github.com/rajkumardusad/MyServer.git

cd MyServer

chmod +x install

sh install

wget -q https://raw.githubusercontent.com/sp4rkie/debian-on-termux/master/debian_on_termux_10.sh

sh debian_on_termux_10.sh

wget -q https://raw.githubusercontent.com/NateWeiler/Termux/master/config/home/aliases

cd $HOME

git clone https://github.com/adi1090x/termux-style

cd termux-style

./install

cd $HOME

install-mh

clear

bash -c "$(curl -fsSL https://git.io/oh-my-termux)"

exit
