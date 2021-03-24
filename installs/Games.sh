#!/data/data/com.termux/files/usr/bin/sh

# Termux Games Install

echo "Termux Games Install"

mkdir -p /sdcard/apps/games

cd /sdcard/apps/games

clear

echo "play Games in Termux by-LearnTermux.tech"

echo -e "\e[032m"

apt install -y ruby

gem install lolcat

pkg install -y figlet

figlet bastet | lolcat && echo Installing..................... | lolcat
echo -e "\e[032m"
pkg install -y bastet

figlet Pacman | lolcat && echo Installing..................... | lolcat
echo -e "\e[032m"
pkg install pacman4console

figlet M-buggy | lolcat && echo Installing..................... | lolcat
echo -e "\e[032m"
pkg install -y moon-buggy

figlet invaders | lolcat && echo Installing..................... | lolcat
echo -e "\e[032m"
pkg install -y ninvaders

figlet snake | lolcat && echo Installing..................... | lolcat
echo -e "\e[032m"
pkg install nsnake

figlet Greed | lolcat && echo Installing..................... | lolcat
echo -e "\e[032m"
pkg install -y greed

figlet Nethack | lolcat && echo Installing..................... | lolcat
echo -e "\e[032m"
pkg install -y nethack

figlet Sudoku | lolcat && echo Installing..................... | lolcat
echo -e "\e[032m"
pkg install -y nudoku && apt install nudoku

figlet Hangman | lolcat && echo Installing..................... | lolcat
echo -e "\e[032m"
pkg install -y git && echo -e "\e[032m" && git clone https://github.com/khansaad1275/HangmanPy.git

figlet Python | lolcat && echo Installing..................... | lolcat
echo -e "\e[032m"
pkg install -y python

figlet "2048" | lolcat && echo Installing..................... | lolcat
echo -e "\e[032m"
pkg install -y wget
pkg install -y clang

wget https://raw.githubusercontent.com/mevdschee/2048.c/master/2048.c

sleep 2

gcc -o 2048 2048.c

echo -e '\033[1mType ./game.sh to start the Termux-Games\033[0m' | lolcat -a
