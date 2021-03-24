#!/bin/bash

# get your local address
echo $(ip -f inet -o addr show enp3s0|cut -d\  -f 7 | cut -d/ -f 1)
ip=$(  ip -f inet -o addr show eth0  |cut -d\  -f 7 | cut -d/ -f 1)


# resolve IP of the news website  RT.com
systemd-resolve   RT.com -t A             | awk '{ print $4 ; exit }'
systemd-resolve   RT.com -t A --legend=no | awk '{ print $4 ; exit }'

resolveip -s      RT.com
dig       +short  RT.com
host              RT.com | awk '/has address/ { print $4 }'
nslookup          RT.com | awk '/^Address: /  { print $2 }'
ping -q -c 1 -t 1 RT.com | grep PING | sed -e "s/).*//" | sed -e "s/.*(//"

ruby     -rresolv -e      ' print    Resolv.getaddress "RT.com" '
python2  -c 'import socket; print socket.gethostbyname("RT.com")'
perl     -MSocket -MNet::hostent -E 'say inet_ntoa((gethost shift)->addr)' RT.com  2>/dev/null
php      -r "echo gethostbyname( 'RT.com' );"
