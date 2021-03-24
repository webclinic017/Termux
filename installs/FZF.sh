#!/data/data/com.termux/files/usr/bin/sh

# FZF Install

echo "FZF Install"

git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf

cd ~/.fzf

rm -rf .git/ .github/ .gitignore  CHANGELOG.md LICENSE Dockerfile

sh install
