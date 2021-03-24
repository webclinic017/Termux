#!/data/data/com.termux/files/usr/bin/sh

echo "DVR Install

echo "Termux is a DVR (Digital Video Recorder) in the palm of my hand, as well as in my pocket."

pkg install -y python

python3 -m pip install youtube-dl

pkg install play-audio

echo "This will play your favorite song forever. Use ctrl+c to exit this eternal trance loop."

while true; do play-audio favoriteSong.file; done
