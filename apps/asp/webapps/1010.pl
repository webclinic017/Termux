source: https://www.securityfocus.com/bid/17964/info
 
WhatsUp Professional is prone to multiple input-validation vulnerabilities. The issues include remote file-include, information-disclosure, source-code disclosure, cross-site scripting, and input-validation vulnerabilities. These issues are due to a failure in the application to properly sanitize user-supplied input. 
 
Successful exploits of these vulnerabilities could allow an attacker to access or modify data, steal cookie-based authentication credentials, perform username-enumeration, access sensitive information, and gain unauthorized access to script source code. Other attacks are also possible.
 
http://www.example.com:8022/NmConsole/utility/RenderMap.asp?nDeviceGroupID=2