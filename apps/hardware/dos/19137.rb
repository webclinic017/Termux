        Matta Consulting - Matta Advisory
            https://www.trustmatta.com

F5 BIG-IP remote root authentication bypass Vulnerability

Advisory ID: MATTA-2012-002
CVE reference: CVE-2012-1493
Affected platforms: BIG-IP platforms without SCCP
Version: 11.x 10.x 9.x
Date: 2012-February-16
Security risk: High
Vulnerability: F5 BIG-IP remote root authentication bypass
Researcher: Florent Daigniere
Vendor Status: Notified / Patch available
Vulnerability Disclosure Policy:
 https://www.trustmatta.com/advisories/matta-disclosure-policy-01.txt
Permanent URL:
 https://www.trustmatta.com/advisories/MATTA-2012-002.txt

=====================================================================
Description:

Vulnerable BIG-IP installations allow unauthenticated users to bypass
 authentication and login as the 'root' user on the device. 

The SSH private key corresponding to the following public key is
 public and present on all vulnerable appliances:

ssh-rsa
AAAAB3NzaC1yc2EAAAABIwAAAIEAvIhC5skTzxyHif/7iy3yhxuK6/OB13hjPqrskogkYFrcW8OK4VJT+5+Fx7wd4sQCnVn8rNqahw/x6sfcOMDI/Xvn4yKU4t8TnYf2MpUVr4ndz39L5Ds1n7Si1m2suUNxWbKv58I8+NMhlt2ITraSuTU0NGymWOc8+LNi+MHXdLk=
 SCCP Superuser

Its fingerprint is:
71:3a:b0:18:e2:6c:41:18:4e:56:1e:fd:d2:49:97:66

=====================================================================
Impact

If successful, a malicious third party can get full control of the
 device with little to no effort. The Attacker might reposition and
 launch an attack against other parts of the target infrastructure
 from there.

=====================================================================
Versions affected:

BIG-IP version 11.1.0 build 1943.0 tested. 

The vendor reports that the following versions are patched:
    9.4.8-HF5 and later 
    10.2.4 and later 
    11.0.0-HF2 and later 
    11.1.0-HF3 and later 

http://support.f5.com/kb/en-us/solutions/public/13000/600/sol13600.html

=====================================================================
Credits

This vulnerability was discovered and researched by Florent Daigniere
 from Matta Consulting.

=====================================================================
History

16-02-12 initial discovery
22-02-12 initial attempt to contact the vendor
24-02-12 reply from David Wang, case C1062228 is open
24-02-12 draft of the advisory sent to the vendor
01-03-12 CVE-2012-1493 is assigned
06-04-12 James Affeld starts coordinating the notification effort
23-05-12 F5 notifies us that patches are ready
29-05-12 F5 sends advance notification to some customers
06-06-12 Public disclosure

=====================================================================
About Matta

Matta is a privately held company with Headquarters in London, and a
 European office in Amsterdam.   Established in 2001, Matta operates
 in Europe, Asia, the Middle East and North America using a respected
 team of senior consultants.  Matta is an accredited provider of
 Tiger Scheme training; conducts regular research and is the developer
 behind the webcheck application scanner, and colossus network scanner.

https://www.trustmatta.com
https://www.trustmatta.com/training.html
https://www.trustmatta.com/webapp_va.html
https://www.trustmatta.com/network_va.html

=====================================================================
Disclaimer and Copyright

Copyright (c) 2012 Matta Consulting Limited. All rights reserved.
This advisory may be distributed as long as its distribution is
 free-of-charge and proper credit is given.

The information provided in this advisory is provided "as is" without
 warranty of any kind. Matta Consulting disclaims all warranties, either
 express or implied, including the warranties of merchantability and
 fitness for a particular purpose. In no event shall Matta Consulting or
 its suppliers be liable for any damages whatsoever including direct,
 indirect, incidental, consequential, loss of business profits or
 special damages, even if Matta Consulting or its suppliers have been
 advised of the possibility of such damages.