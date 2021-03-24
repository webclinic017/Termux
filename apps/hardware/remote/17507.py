# Exploit Title: [title]
# Date: [date]
# Author: [ShellVision]
# Version: [dm800 <= 1.6rc3]
# Tested on: [dm800 Release 4.6.0 2009-12-24]



DreamBox DM800 Arbitrary File Download Vulnerability
 
 
Vendor: Dream Multimedia GmbH
Product web page: http://www.dream-multimedia-tv.de
Affected version: DM800 (may affect others version)
 
Summary: The Dreambox is a series of Linux-powered
DVB satellite, terrestrial and cable digital television
receivers (set-top box).
 
Desc: Dreambox suffers from a file download vulnerability
thru directory traversal with appending the '/' character
in the HTTP GET method of the affected host address. The
attacker can get to sensitive information like paid channel
keys, usernames, passwords, config and plug-ins info, etc.

By default, web application is running by root, so catch shadow is
very easy
 
Tested on: 

Devicename:	dm800
Enigma Version:	2009-12-24-master
Image Version:	Release 4.6.0 2009-12-24
Frontprozessor Version:	VNone
Webinterface Version:	1.6rc3

 
Vulnerability discovered by: ShellVision Designer@ShellVision.com
ShellVision - www.shellvision.com
 
 20 Jun 2011
 
 
--------------------------------------------------------------------
 
http://target.com/file?file=/etc/shadow