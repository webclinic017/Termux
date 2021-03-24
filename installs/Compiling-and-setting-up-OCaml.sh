#!/data/data/com.termux/files/usr/bin/sh

echo "Compiling and setting up OCaml"

echo "1. Install OPAM"

echo "deb [arch=all,aarch64] http://ygrek.org.ua/files/debian/termux ./" >> data/data/com.termux/files/usr/etc/apt/sources.list apt-get update # repository is not signed for now :] pkg install opam

echo "2. Install OCaml"

opam init --comp=4.03.0+termux termux https://github.com/camlunity/opam-repository.git#termux

echo "Build OCaml to build OPAM to build OCaml"

echo "1. Prepare proper build environment."

pkg install build-essential diffutils m4 patch

echo "2. NB termux lacks /bin/sh (and all other standard unix file paths for that matter), so the main problem during builds is hardcoded shell path in https://github.com/termux/termux-packages/issues/98."

echo "To overcome it - use sh ./script instead of just ./script."

sh ./script

echo "3. Build OCaml"

mkdir ~/tmp export TMPDIR=$HOME/tmp # add to ~/.profile git clone https://github.com/ygrek/ocaml.git -b termux-4.03.0 cd ocaml sh ./configure -prefix $PREFIX make world.opt install

echo "4. Build OPAM""

curl -LO https://github.com/ocaml/opam/releases/download/1.2.2/opam-full- 1.2.2.tar.gz tar -xzf opam-full-1.2.2.tar.gz cd opam-full-1.2.2/ sed -i 's|/bin/sh|sh|' src/core/opamSystem.ml OCamlMakefile CONFIG_SHELL=sh sh ./configure -prefix "$PREFIX" OCAMLPARAM="safe-string=0,_" make lib-ext all install

echo "5. Add OPAM remote with Termux patches"

opam remote add termux https://github.com/camlunity/opam-repository.git#termux

echo "6. Install OCaml via OPAM and remove system OCaml (built in step 3) to avoid confusion with OPAM switches"

opam sw 4.03.0+termux # 4.02.3+termux 4.04.0+termux rm /data/data/com.termux/files/usr/man/man1/ocaml* rm /data/data/com.termux/files/usr/bin/ocaml* rm -rf /data/data/com.termux/files/usr/lib/ocaml opam sw remove system
