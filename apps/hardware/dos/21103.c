source: https://www.securityfocus.com/bid/3236/info


CBOS is the Cisco Broadband Operating System, firmware designed for use on Cisco 600 series routers. It is maintained and distributed by Cisco Systems.

CBOS becomes unstable when it receives multiple TCP connections on one of the two administrative ports; 21 via telnet, or 80 via HTTP. Upon receiving multiple connections on one of these two ports, the 600 series router becomes incapable of configuration, requiring reboot to resume normal operation.

This problem affects the following Cisco 600 series routers: 627, 633, 673, 675, 675E, 677, 677i and 678. 

https://github.com/offensive-security/exploitdb-bin-sploits/raw/master/bin-sploits/21092.mrc