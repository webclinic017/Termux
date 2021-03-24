#!/data/data/com.termux/files/usr/bin/sh

echo "Heroku Install"

cd

pkg install -y wget nano tar gzip nodejs

wget http://cli-assets.heroku.com/heroku-linux-arm.tar.gz -O heroku.tar.gz

tar -xvzf heroku.tar.gz

rm -rf heroku.tar.gz

mkdir -p /data/data/com.termux/files/usr/lib/

mv -v heroku/ /data/data/com.termux/files/usr/lib/

ln -s /data/data/com.termux/files/usr/lib/heroku/bin/heroku /data/data/com.termux/files/usr/bin/heroku

echo "Heroku will not work as its script is pointing to /usr/bin/env whereas our path on Termux differs."

echo "To direct Heroku to the right path, first install nano (or your own favourite editor), then edit Heroku’s script:"

cd /data/data/com.termux/files/usr/lib/heroku/bin/

#!/data/data/com.termux/files/usr/bin/env bash

echo "Change this line to:"

echo "#!/data/data/com.termux/files/usr/bin/env bash"
sleep 20s

echo "Now Heroku is not yet working, one more fix and we’ll be done."

echo "The tarball file does contain a necessary node.js binary but it does not work in Termux. you will have to install it with the Linux environment and point Heroku to its path."

touch heroku
sleep 20s

nano heroku

cd /data/data/com.termux/files/usr/lib/heroku/bin

mv node node.old

ln -s ../../../bin/node node

echo "When asked, press any key (expect ‘q’) to open a web browser and login your Heroku account."

echo "Done"
