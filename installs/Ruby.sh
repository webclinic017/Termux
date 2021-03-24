#!/data/data/com.termux/files/usr/bin/sh

echo "Ruby Install"

pkg install ruby

echo "After installing ruby, gem package manager will be available. Here is a quick tutorial about its usage."

echo "Installing a new gem"

gem install {package_name}

echo "Uninstalling gem"

echo "gem uninstall {package name}"

echo "Listing installed gems"

gem list --local

echo "Launching a local documentation and gem repository server"

gem server

echo "When installing Ruby gems, it is highly recommended to have a package build-essential to be installed - some gems compile native extensions during their installation."
