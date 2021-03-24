#!/data/data/com.termux/files/usr/bin/sh

echo "wget multiple files"

while read url; do
    wget -q -nH --cut-dirs=5 -r -l0 -c -N -np -R 'index*' -erobots=off --retr-symlinks "$url"
done < urls.txt
