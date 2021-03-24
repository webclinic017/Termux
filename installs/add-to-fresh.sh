#!/data/data/com.termux/files/usr/bin/sh

bash <(curl -fsSL https://git.io/JvMD6)

git clone https://github.com/Neo-Oli/chrooted-termux

bash prooted-termux/chrooted-termux

bash chrooted-termux/prooted-termux

git clone https://github.com/matplotlib/matplotlib

cd matplotlib

sed 's@#enable_lto = True@enable_lto = False@g' setup.cfg.template > setup.cfg

pip install .

export CFLAGS="-Wno-deprecated-declarations -Wno-unreachable-code"

wget -q https://raw.githubusercontent.com/sp4rkie/debian-on-termux/master/debian_on_termux_10.sh && sh debian_on_termux_10.sh

bash <(curl -fsSL https://git.io/JTgsU)

cd

git clone https://github.com/Towha/ubuntu.sh .ubuntu && cd .ubuntu && sudo bash ubuntu.sh

curl -LO https://its-pointless.github.io/setup-pointless-repo.sh

bash setup-pointless-repo.sh

pkg install -y termux-exec

pkg install -y termux-fix-shebang

pkg install -y game-repo

pkg install -y science-repo

pkg install -y root-repo

pkg install -y x11-repo

pkg install -y unstable-repo

pkg install -y pacman4console

pkg install -y ruby

pkg install -y ruby-ri

pkg install -y moreutils

pkg install -y task-spooler

pkg install -y yarn

pkg install -y hexcurse

pkg install -y hugo

pkg install -y ired

pkg install -y radare

pkg install -y icu-devtools

pkg install -y ldc

pkg install -y sleuthkit

pkg install -y nodejs

pkg install -y nodejs-lts

pkg install -y yarn

pkg install -y perl

pkg install -y gettext

cpan App::cpanminus

apt install -y texlive-full

apt install -y texlive

termux-install-tl

tlmgr update --all
