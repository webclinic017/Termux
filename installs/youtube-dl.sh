#!system/bin/bash

# Install youtube-dl
# ==================

echo "Download Youtube videos on your Android device by using Termux.it's very to install & download the youtube videos & audio From the Command Line with youtube-dl."

echo 'Storage permission'
termux-setup-storage

echo 'cURL'
pkg install curl

echo 'Install Python'
pkg install python

echo 'ffmpeg - For Audio Conversion'
pkg install ffmpeg

echo 'Install youtube-dl via cURL'
curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /data/data/com.termux/files/usr/bin/youtube-dl

echo 'Give Permission to Execute the Script'
chmod a+rx /data/data/com.termux/files/usr/bin/youtube-dl

echo 'Verify your Installation'

echo 'which youtube-dl'

echo 'Learn More about youtube-dl Command Line tool'

echo 'youtube-dl --help'

echo 'Update Youtube-dl'
chmod a+rx /data/data/com.termux/files/usr/bin/youtube-dl youtube-dl -U

echo 'Download and Install via cURL Command'
curl -sL https://gist.githubusercontent.com/mskian/6ea9c2b32d5f41867e7cafc88d1b26d5/raw/youtube-dl.sh | bash

echo 'Usage'

echo 'Youtube Video and Audio Downloader for Android.'

echo 'youtube-dl YOUTUBE VIDEO URL'

echo 'List the Video Formats'

echo 'youtube-dl --list-formats YOUTUBEVIDEOURL'

echo 'Download youtube video by using Format code'
sleep 20

echo 'youtube-dl -f FORMATCODE YOUTUBEVIDEOURL'

echo 'Download as MP3'

echo 'youtube-dl --extract-audio --audio-format mp3 YOUTUBE VIDEO URL'

echo 'Uninstall youtube-dl from Termux'

echo 'Installed Location - /data/data/com.termux/files/usr/bin/'

echo 'Goto youtube-dl installed location'

echo 'cd /data/data/com.termux/files/usr/bin/'

echo 'Remove/uninstall youtube-dl Software'

echo 'rm youtube-dl'
sleep 20