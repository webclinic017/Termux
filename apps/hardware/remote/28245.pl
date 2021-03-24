During an audit the Mikrotik RouterOS sshd (ROSSSH) has been identified to have a remote previous to authentication heap corruption in its sshd component.

Exploitation of this vulnerability will allow full access to the router device.

This analysis describes the bug and includes a way to get developer access to recent versions of Mikrotik RouterOS
using the /etc/devel-login file. This is done by forging a modified NPK file using a correct signature and logging
into the device with username ‘devel’ and the password of the administrator. This will drop into a busybox shell for
further researching the sshd vulnerability using gdb and strace tools that have been compiled for the Mikrotik busybox
platform.

Shodanhq.com shows >290.000 entries for the ROSSSH search term.

The 50 megs Mikrotik package including the all research items can be downloaded here: 

http://www.farlight.org/mikropackage.zip
https://github.com/offensive-security/exploitdb-bin-sploits/raw/master/bin-sploits/28056.zip