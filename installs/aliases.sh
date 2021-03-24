#!/data/data/com.termux/files/usr/bin/sh

# ALIASES #

# Shortcuts
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

# Git
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

# Python
alias py='python3'
alias p2='python2'
alias p3='python3'
alias python='python3'
alias pip='python3 -m pip'
alias webserver='python3 -m http.server 8080'
alias ve='virtualenv venv -p python3'
alias va='source venv/bin/activate'

# YouTube-dl
alias yt='youtube-dl'
alias mp4='youtube-dl -f bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'
alias mp3='youtube-dl -x --audio-format "mp3" --audio-quality 0 --embed-thumbnail $*'

# Update
alias pu='pkg update -y && pkg upgrade -y'
alias au='apt update -y && apt upgrade -y'
alias uu='au && pu'

# Docker
alias docker_start='systemctl start docker'
alias docker_debian='docker run -it debian /bin/bash'

# Config
alias ip='curl ifconfig.me'
alias ifc='ifconfig wlan0'
alias zshconfig="mate ~/.zshrc"
alias ohmyzsh="mate ~/.oh-my-zsh"
alias chcolor='/data/data/com.termux/files/home/.termux/colors.sh'
alias chfont='/data/data/com.termux/files/home/.termux/fonts.sh'

# ETC
alias l='ls -AFph --color=auto --show-control-chars'
alias lall='ls -AFRph --color=auto --show-control-chars'
alias r='rm -rf'
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
alias arch='startarch'

clear

cat /data/data/com.termux/files/home/etc/motd
