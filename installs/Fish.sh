#!/data/data/com.termux/files/usr/bin/sh

echo "Fish Install"

cd

pkg install fish

echo "Fisher Install"

#!/data/data/com.termux/files/usr/bin/sh

fish

curl -sL https://git.io/fisher | source && fisher install jorgebucaran/fisher

fisher install ilancosman/tide

fisher install jorgebucaran/nvm.fish@1.1.0
