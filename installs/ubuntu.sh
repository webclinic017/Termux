#!/data/data/com.termux/files/usr/bin//env bash

# Ubuntu Install

echo "Ubuntu Install"

USER=$(whoami)
export DEBIAN_FRONTEND=noninteractive
export PATH="$HOME/.local/bin:$PATH"
sudo rm -rf /var/lib/dpkg/lock
sudo rm -rf /var/cache/debconf/*.*

# colors
NORMAL=`tput sgr0`
RED=`tput setaf 1`
GREEN=`tput setaf 2`
Done="${GREEN}Done ✓${NORMAL}"

clear
echo "${RED}Disclaimer:${NORMAL} This script is shit and bloated"
sleep 5

echo "${RED}Do you want to change server password?${NORMAL}"
read -p "y/n:
" prompt
if [[ $prompt == "y" || $prompt == "Y" || $prompt == "yes" || $prompt == "Yes" ]]
then
  sudo passwd $USER
else
  echo "${GREEN}Password wasn't Changed.${NORMAL}"
fi


echo "${RED}Enabling Universe, Multiverse and Restricted repositories${NORMAL}"
sleep 1
sudo add-apt-repository universe > /dev/null
sudo add-apt-repository multiverse > /dev/null
sudo add-apt-repository restricted > /dev/null
echo $Done

echo "${RED}Checking for updates.${NORMAL}"
sleep 1
sudo apt-get -y update > /dev/null
sudo apt-get -y upgrade > /dev/null 2>&1
sudo apt-get -y autoremove  > /dev/null
echo $Done

echo "${RED}Setting UTF8${NORMAL}"
sleep 1
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
sudo apt-get install -qq language-pack-en-base > /dev/null
sudo apt-get install -qq software-properties-common > /dev/null
echo $Done

echo "${RED}Adding a auto updater to crontab${NORMAL}"
sleep 1
sudo crontab -l > updater
sudo echo "0 0 * * *    sudo apt-get update && sudo apt-get upgrade -y && sudo apt autoremove && echo updated@SUCCESS >> ~/.update.log" >> updater
sudo crontab updater
sudo rm updater
echo $Done

echo "${RED}Installing Apt-fast${NORMAL}"
sudo add-apt-repository -y ppa:apt-fast/stable > /dev/null
sudo apt-get -qq update > /dev/null && sudo DEBIAN_FRONTEND=noninteractive apt-get -y install apt-fast > /dev/null 
echo $Done

echo "${RED}Installing day2day packages${NORMAL}"
sudo apt-get install -qq ncdu tmux irssi tree rar unrar zip unzip htop atop p7zip-full neovim vnstati > /dev/null 2>&1
echo $Done

echo "${RED}Now installing some python essential packages${NORMAL}"
sudo apt-get install -qq python3-pip python3-dev python3-utmp python3-virtualenv > /dev/null 2>&1
pip3 install virtualenvwrapper wheel gallery-dl youtube-dl requests bs4 lxml -q > /dev/null 2>&1
echo $Done

echo "${RED}Installing rclone${NORMAL}"
sleep 1
curl -s https://rclone.org/install.sh | sudo bash > /dev/null 2>&1
echo $Done

echo "${RED}Installing vsftpd${NORMAL}"
sudo apt-get install -qq vsftpd  > /dev/null
sudo systemctl start vsftpd  > /dev/null 2>&1
sudo systemctl enable vsftpd > /dev/null 2>&1
sudo tee -a /etc/vsftpduserlist.conf >> /dev/null <<'user'
ubuntu
towha
root
user
sudo systemctl restart vsftpd  > /dev/null 2>&1
echo $Done

echo "${RED}Installing some compiling packages${NORMAL}"
sudo apt-get install -qq build-essential libssl-dev autoconf automake cmake ccache libicu-dev git-core libass-dev zlib1g-dev yasm texinfo pkg-config libtool > /dev/null 2>&1
echo $Done

echo "${RED}Installing ffmpeg, please refer to https://trac.ffmpeg.org/wiki/CompilationGuide/Ubuntu for extra codecs${NORMAL}"
sleep 5
sudo apt-get install -qq ffmpeg > /dev/null 2>&1
echo $Done

echo "${RED}Installing Language packages${NORMAL}"
sudo add-apt-repository -y ppa:openjdk-r/ppa > /dev/null
sudo add-apt-repository -y ppa:linuxuprising/libpng12 > /dev/null # I am skipping php due to reasons and only adding its repo in case there is a need to install it.
sudo apt-get install -qq nginx golang docker.io perl openjdk-15-jre > /dev/null 2>&1 && curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash - > /dev/null && sudo apt-get -y install nodejs > /dev/null 
echo $Done # sudo apt-get install -qq curl debconf-utils php-pear php7.4-curl php7.4-dev php7.4-gd php7.4-mbstring php7.4-zip php7.4-mysql php7.4-xml php7.4-fpm php7.4-intl php7.4-bcmath > /dev/null 
 
echo "${RED}Installing aria2 & transmission${NORMAL}"
sudo apt-get install -qq aria2 > /dev/null
sudo apt-get install -qq transmission-cli transmission-daemon > /dev/null && sudo /etc/init.d/transmission-daemon stop > /dev/null && mkdir ~/downloads && sudo chown ubuntu:debian-transmission ~/downloads && sudo chmod g+w ~/downloads && clear && sudo sed -i 's|"/var/lib/transmission-daemon/downloads"|"~/downloads"|g' /etc/transmission-daemon/settings.json && sudo sed -i 's|"rpc-whitelist-enabled": true|"rpc-whitelist-enabled": false|g' /etc/transmission-daemon/settings.json && sudo sed -i 's|"rpc-authentication-required": true|"rpc-authentication-required": false|g' /etc/transmission-daemon/settings.json > /dev/null
echo $Done


echo "${RED}changing MOTD${NORMAL}" # "touch .hushlogin" to "remove" the motd instead of deleting it.
sudo apt-get install -qq update-motd > /dev/null
sudo rm -rf /etc/update-motd.d/*
sudo apt-get install -qq inxi screenfetch > /dev/null
sudo touch /etc/update-motd.d/01-custom 
sudo chmod +x /etc/update-motd.d/01-custom

sudo tee /etc/update-motd.d/01-custom > /dev/null <<'MOTD'
#!/bin/bash
echo GENERAL SYSTEM INFORMATION
/usr/bin/screenfetch
echo
echo SYSTEM DISK USAGE
export TERM=xterm; inxi -D
echo
MOTD
echo $Done

echo "${RED}Now installing oh-my-tmux${NORMAL}"
cd && git clone --quiet https://github.com/gpakosz/.tmux.git > /dev/null && ln -s -f .tmux/.tmux.conf > /dev/null && cp .tmux/.tmux.conf.local . 
echo $Done

echo "${RED}Now installing ZSH${NORMAL}"
sleep 1
sudo apt-get update -qq && sudo apt-get install -qq zsh > /dev/null 2>&1 && \
git clone --quiet https://github.com/ohmyzsh/ohmyzsh.git ~/.oh-my-zsh > /dev/null  && cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc 
echo -e "${GREEN}Making Oh My Zsh hawt...${NORMAL}"
    git clone --quiet https://github.com/zsh-users/zsh-syntax-highlighting $HOME/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting > /dev/null 
    git clone --quiet https://github.com/zsh-users/zsh-autosuggestions $HOME/.oh-my-zsh/custom/plugins/zsh-autosuggestions > /dev/null 
    git clone --quiet https://github.com/zsh-users/zsh-completions $HOME/.oh-my-zsh/custom/plugins/zsh-completions > /dev/null 
	wget https://raw.githubusercontent.com/rupa/z/master/z.sh -q -O ~/.z > /dev/null 2>&1
    git clone --quiet --depth=1 https://github.com/romkatv/powerlevel10k.git $HOME/.oh-my-zsh/custom/themes/powerlevel10k > /dev/null
    [[ -z $(grep "autoload -U compinit && compinit" $HOME/.zshrc) ]] && echo "autoload -U compinit && compinit" >> $HOME/.zshrc
	
    sed -i '/^ZSH_THEME=/c\ZSH_THEME="random"' $HOME/.zshrc
	sed -i '/^plugins=*=/c\plugins=(git systemd command-not-found heroku pip tmux tmuxinator jump z zsh-syntax-highlighting zsh-autosuggestions zsh-completions)' $HOME/.zshrc
	
	sudo tee -a $HOME/.zshrc >> /dev/null <<'ALIAS'
##############
#  A L I A S #
##############
alias .='cd ../; l'
alias ..='cd ../../; l'
alias ...='cd ../../../; l'
alias cd-='cd -; l'
alias ~='cd; l'
alias h='cd; l'
alias scr='cd /sdcard/scripts; l'
alias sd='cd /sdcard/; l'
alias ins='cd /sdcard/installs/; l'
alias pyt='cd /sdcard/python/; l'
alias ven='cd /sdcard/python/venv/; l'
alias app='cd /sdcard/apps/; l'
alias d='cd /sdcard/Download/; l'
alias doc='cd /sdcard/Documents/; l'
alias gh='cd /sdcard/github/; l'
alias ter='cd /sdcard/github/Termux/; l'
alias res='cd /sdcard/github/Resources/; l'
alias sdcard='cd /storage/4932-72CF/; l'
alias music='/storage/4932-72CF/Music; l'
alias g='git clone'
alias gpl='git pull'
alias gp='git push'
alias gco='git checkout'
alias gcm='git checkout master'
alias gr='git remote -v'
alias gb='git branch -a'
alias gl='git log --pretty -n 2 --stat'
alias gs='git status -u'
alias ga='git add . && git add -A'
alias gf='git ls-files | grep'
alias gk='gitk --all --branches'
alias gl='git log --pretty -n 2 --stat --decorate --all'
alias gc='git commit -m'
alias gi='git init'
alias pb='phpcs'
alias pbf='phpcbf'
alias hist='history'
alias n='nano -Lc'
alias less='less -SR'
alias x='exit'
alias py='python3'
alias p2='python2'
alias p3='python3'
alias python='python3'
alias pip='python3 -m pip'
alias webserver='python3 -m http.server 8080'
alias ve='virtualenv venv -p python3'
alias va='source venv/bin/activate'
alias yt='youtube-dl'
alias mp4='youtube-dl -f bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'
alias mp3='youtube-dl -x --audio-format "mp3" --audio-quality 0 --embed-thumbnail $*'
alias docker_start='systemctl start docker'
alias docker_debian='docker run -it debian /bin/bash'
alias ip='curl ifconfig.me'
alias ifc='ifconfig wlan0'
alias zshconfig="mate ~/.zshrc"
alias ohmyzsh="mate ~/.oh-my-zsh"
alias chcolor='/data/data/com.termux/files/home/.termux/colors.sh'
alias chfont='/data/data/com.termux/files/home/.termux/fonts.sh'
alias l='ls -AFph --color=auto --show-control-chars'
alias lall='ls -AFRph --color=auto --show-control-chars'
alias mv='mv -v'
alias mvt='mv -t'
alias mk='mkdir -p'
alias cp='cp -R'
alias c='cat'
alias ch='chmod +x'
alias to='termux-open'
alias pad='n ~/pad.txt'
alias mocp="mocp; mocp -x"
alias clear_cache="paccache -rk0"
alias gpfw="python ~/GitHub/gopro_fw_dl/gopro-fw-dl.py"
alias inotify_increase="echo fs.inotify.max_user_watches=524288 | tee /etc/sysctl.d/40-max-user-watches.conf && sysctl --system"
alias fixadb="adb kill-server && adb devices"
alias dmenu_fixed="dmenu_run -fn '-xos4-terminus-medium-r-*-*-14-*' -h 26"
alias cleanphoto="exiftool -all= $*"
alias tree='tree -C'
alias ip='ip -c'
alias brew="termux-chroot ~/.linuxbrew/Homebrew/bin/brew'
alias fedora='startfedora'
alias arch='startarch'alias s="sudo"
alias install="sudo apt-get -y install"
alias reboot="sudo reboot"
alias cls="clear"
alias mount="rclone mount"
alias r="sudo rm -rf"
alias pu='pkg update -y && pkg upgrade -y'
alias au='sudo apt-get -y update -y && sudo apt-get -y upgrade -y'
alias uu='au && pu'
alias gdl="gallery-dl"
alias aria2="aria2c"
alias refresh="source ~/.zshrc"
ALIAS


sudo chsh -s /bin/zsh $USER
sudo echo "bash -c zsh" >> .bashrc # This is used since for some cloud service changing the shell isn't permitted so a work around for it.
echo $Done

echo "${GREEN}ALL DONE!${NORMAL}"
echo "${GREEN}It is recommended to ${RED}reboot${NORMAL}${GREEN} your server now!${NORMAL}"
