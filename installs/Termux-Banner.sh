#!/data/data/com.termux/files/usr/bin/sh

echo "Termux Banner Install"

git clone https://github.com/Bhai4You/Termux-Banner

mv -v Termux-Banner /sdcard/scripts/

cd /sdcard/scripts/Termux-Banner

chmod +x requirement.sh

chmod +x t-ban.sh

sh requirement.sh

sh t-ban.sh

rm -rf .git/ .github/ SECURITY.md

echo "Uninstallation Step : (Remove Logo From Termux)"

echo "sh remove.sh"

echo "Done !!!"
