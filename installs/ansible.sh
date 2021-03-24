#!/data/data/com.termux/files/usr/bin/sh

echo "Ansible Install"

export SODIUM_INSTALL=system
export BIN_SH=$PREFIX/bin/sh
export TMPDIR=/data/data/com.termux/files/tmp
export TMP=$TMPDIR
export TEMP=$TMPDIR
export CONFIG_SHELL=$BIN_SH

mkdir $TMPDIR

apt install -y python2 python2-dev

apt install -y libffi-dev

apt install -y libsodium-dev

apt install -y openssl-dev

apt install -y libgmp-dev

apt install -y libev-dev

EMBED=0 pip2 install gevent

python3 -m pip install gevent

python3 -m pip install pycrypto

echo "only ansible 1.8.x is supported right now (sem_lock errors with >=1.9 and 2.x"

python3 -m pip install 'ansible<1.9.0'
