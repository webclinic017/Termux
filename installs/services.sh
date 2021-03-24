#!/data/data/com.termux/files/usr/bin/sh

echo "termux-services Install\n"

echo "termux-services contains a set of scripts for controlling services. Instead of putting commands in ~/.bashrc or ~/.bash_profile, they can be started and stopped with termux-services.\n"

echo "Only a few packages so far contain the necessary service scripts, these are\n"

echo "mpd tor transmission sshd ftpd telnetd emacsd\n"

pkg install termux-services

echo "and then restart termux so that the service-daemon is started.\n"

echo "Enable and run a service\n"

sv-enable <service>

echo "If you only want to run it once\n"

sv up <service>

echo "To later stop a service, run\n"

echo "sv down <service>\n"

echo "Or to disable it\n"

echo "sv-disable <service>\n"

echo "A service is disabled if `$PREFIX/var/service/<service>/down` exists, so the `sv-enable` and `sv-disable` scripts touches, or removes, this file.\n"

echo "termux-services uses the programs from runit to control the services. A bunch of example scripts are available from the same site. If you find a script you want to use, or if you write your own, you can use set it up by running\n"

mkdir -p $PREFIX/var/service/<PKG>/log

ln -sf $PREFIX/share/termux-services/svlogger $PREFIX/var/service/<PKG>/log/run

and then put your run script for the package at $PREFIX/var/service/<PKG>/run and make sure that it is runnable.\n"

echo "You can then run\n"

echo "sv up <PKG>\n"

echo "to start it.\n"

echo 'Log files for services are situated in $PREFIX/var/log/sv/<PKG>/ with the active log file named "current".'
