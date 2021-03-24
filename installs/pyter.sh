#!/data/data/com.termux/files/usr/bin/sh

echo "pyter Install"

echo "pyter is a simple Translation Error Rate evaluation command."

/data/data/com.termux/files/usr/bin/python3 -m pip install pyter

cd /sdcard/github/Termux/python/

git clone git://github.com/aflc/pyter.git

cd pyter

/data/data/com.termux/files/usr/bin/python3 -m pip install -e .

/data/data/com.termux/files/usr/bin/python3 setup.py build

/data/data/com.termux/files/usr/bin/python3 setup.py install

rm -rf .hgtags .hgignore

mv -v .git/ DOTgit

pyter --help > 'pyter help.txt'

pyter --help
