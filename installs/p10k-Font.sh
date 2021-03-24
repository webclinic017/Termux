#!/data/data/com.termux/files/usr/bin/sh

# Termux p10k Font Install

echo "Termux p10k Font Install"

mkdir -p ~/.termux

curl -fsSL -o ~/.termux/font.ttf 'https://github.com/romkatv/dotfiles-public/raw/master/.local/share/fonts/NerdFonts/MesloLGS%20NF%20Regular.ttf'

termux-reload-settings
