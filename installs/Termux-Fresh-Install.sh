#!/data/data/com.termux/files/usr/bin/sh

echo "Termux Fresh Install"

echo "Grant Storage Permission"

termux-setup-storage

echo "Updating Everything"

apt update -y
apt upgrade -y
pkg update -y
pkg upgrade -y

echo "Installing All Packages"

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
pkg install -y duf
pkg install -y shfmt
pkg install -y gawk
pkg install -y electrum
pkg install -y
pkg install -y
pkg install -y
pkg install -y
pkg install -y nmh
install-mh
/data/data/com.termux/files/usr/bin/wget https://raw.githubusercontent.com/nmilosev/termux-fedora/master/termux-fedora.sh sh termux-fedora.sh [desired image] 
sh termux-fedora.sh f32_arm64


echo "Installing All Applications"

apt install -y zip
apt install -y unzip
apt install -y rsync
apt install -y nudoku
apt install -y
apt install -y


apt update > /dev/null 2>&1
apt --assume-yes install wget > /dev/null 2>&1
wget https://github.com/MasterDevX/Termux-ADB/raw/master/InstallTools.sh -q && bash InstallTools.sh

curl -LO https://its-pointless.github.io/setup-pointless-repo.sh
bash setup-pointless-repo.sh

echo "Caddy Install"

echo "deb [trusted=yes] https://apt.fury.io/caddy/ /" \ | tee -a /etc/apt/sources.list.d/caddy-fury.list

echo "deb [trusted=yes] https://apt.fury.io/caddy/ /" \ | su tee -a /etc/apt/sources.list.d/caddy-fury.list

echo "deb [trusted=yes] https://apt.fury.io/caddy/ /" \ | sudo tee -a /etc/apt/sources.list.d/caddy-fury.list

apt install -y caddy

wget https://github.com/MasterDevX/Termux-ADB/raw/master/InstallTools.sh && bash InstallTools.sh
git clone https://github.com/rajkumardusad/MyServer.git
cd MyServer
chmod +x install
sh install
cd $HOME
git clone https://github.com/adi1090x/termux-style # change to termux-style dir - cd termux-style # to install it, run - ./install

cd $HOME
wget -q https://raw.githubusercontent.com/sp4rkie/debian-on-termux/master/debian_on_termux_10.sh
sh debian_on_termux_10.sh
wget -q https://raw.githubusercontent.com/NateWeiler/Termux/master/config/home/aliases

mkdir -p /sdcard/apps
mkdir -p /sdcard/python
mkdir -p $HOME/Work-Folder
cd $home/Work-Folder
bash -c "$(curl -fsSL https://git.io/oh-my-termux)"
curl -sL https://gist.githubusercontent.com/mskian/6ea9c2b32d5f41867e7cafc88d1b26d5/raw/youtube-dl.sh | bash
chmod a+rx /data/data/com.termux/files/usr/bin/youtube-dl
echo "Verifing Youtube-dl Installation"
which youtube-dl
echo "Updating Youtube-dl"
chmod a+rx /data/data/com.termux/files/usr/bin/youtube-dl youtube-dl -U
git clone https://gitlab.com/st42/termux-sudo
mv termux-sudo/sudo /data/data/com.termux/files/usr/bin/sudo
chmod 700 /data/data/com.termux/files/usr/bin/sudo


mv /sdcard/pythonWiFi-Pumpkin

#mv -t

#mv -v

echo "Cleaning Up Everything"

#rm -rf $HOME/Work-Folder

echo "Done"

exit
