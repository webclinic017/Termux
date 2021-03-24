source: https://www.securityfocus.com/bid/549/info

A denial of service condition exists in some implementations of Firewall-1 by Checkpoint Software. This denial of service attack is possible due to the way Firewall-1 handles TCP connections.

Typically to initiate a TCP connection, a SYN packet is sent to the destination host. On systems where Firewall-1 is installed, this packet is first passed through an internal stack maintained by the Firewall before it is passed onto the operating system's native stack. When Firewall-1 filters this packet, it checks it against the rule base. If the session is allowed where it's rulebase is concerned, it is added to the connections table with a timeout of 60 seconds. When the remote host responds with an ACK (Acknowledge) packet, the session is bumped up to a 3600 second timeout.

However, if you initiate a connection with an ACK packet, Firewall-1 compares it against the rule base, if allowed it is added to the connections table. However, the timeout is set to 3600 seconds and does not care if a remote system responds. You now have a session with a 1 hour timeout, even though no system responded. If this is done with a large amount of ACK packets, it will result in a full connections table. This results in your Firewall-1 refusing subsequent connections from any source effectively rendering the Firewall-1 useless in a 'failed closed' state. 

Most companies allow http outbound. Run this command as root from an internal system, I give your FW about 10 to 15 minutes. If your internal network is a 10.x.x.x, try 172.16.*.*

nmap -sP 10.*.*.*

nmap is a very powerful port scanner. With this command it does only a PING and TCP sweep (default port 80), but uses an ACK instead of a SYN.

To verify that your connections table is quickly growing, try "fw tab -t connections -s" at 10 second intervals.

Tested on ver 4.0 SP3 on Solaris x86 2.6.