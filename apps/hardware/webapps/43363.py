# Exploit Title: ZTE ZXDSL 831 Unauthorized Configuration Access
# Date: 27/11/2017
# Exploit Author: Ibad Shah
# Vendor Homepage: zte.com.cn
# Software Link: -
# Version: - ZXDSL - 831CII
# Tested on: Windows 10
# CVE :- 2017-16953

======================================= 
The Router usually servers html files & are protected with HTTP Basic
Authentication. However, the CGI files does not protect this file from
getting exposed to public. A Simple GET request would be needed to
made to router that would give a remote attacker an opportunity to
modify router PPPoE configurations, setup malicious configurations
which later could lead to disrupt network & its activities.


Proof Of Concept
================
http://192.168.1.1/connoppp.cgi