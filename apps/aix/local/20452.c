source: https://www.securityfocus.com/bid/1800/info

A vulnerability exists in AIX 3.* versions of bugfiler, a utility which automates the process of reporting an filing system bugs. Bugfiler, installed setuid root, creates files in a directory specified by the user invoking the program (example: $/lib/bugfiler -b <user> directory>). It may be possible for an attacker to create files in arbitrary directories that are owned by attacker-specified users. This may result in an elevation of privileges for the attacker. Further technical details about this vulnerability are not known.

$whoami eviluser 
$/lib/bugfiler -b <user> <directory> creates funny files under the <user>-owned <directory> and that may be used by crackers to increase privileges. See the manpage of bugfiler for more information. (bugfiler does not work for some <user>s)