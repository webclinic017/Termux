-----------------------------------------------------------------------
          Konke Smart Plug Authentication Bypass Vulnerability
-----------------------------------------------------------------------
Author      : gamehacker&zixian
Mail        : gh<gh@waloudong.org>&zixian<me@zixian.org>
Date        : Oct, 17-2014
Vendor      : http://www.kankunit.com/
Link        : http://www.kankunit.com/
Version     : K
CVE         : CVE-2014-7279
 
Exploit & p0c
_____________
 
    “Konke” is a smart Home Furnishing products (http://www.kankunit.com/) in China, the product has a security vulnerability, an attacker could exploit the vulnerability to obtain equipment management authority.


    Konke Smart Plug open 23 port，we can telnet the 23 port，we can get root without password.


    1、Scan Konke. you can use nmap scan the 23 port.
    2、open cmd telnet Konke's 23 port.
    3、now you are the root. it is a openwrt,you can use busybox do everything! you can use "reboot" command to reboot Konke.and so on……


_____________