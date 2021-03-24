#!/data/data/com.termux/files/usr/bin/sh

# Caddy Install

echo "deb [trusted=yes] https://apt.fury.io/caddy/ /" \ | tee -a /etc/apt/sources.list.d/caddy-fury.list

echo "deb [trusted=yes] https://apt.fury.io/caddy/ /" \ | su tee -a /etc/apt/sources.list.d/caddy-fury.list

echo "deb [trusted=yes] https://apt.fury.io/caddy/ /" \ | sudo tee -a /etc/apt/sources.list.d/caddy-fury.list

apt install caddy
