source: https://www.securityfocus.com/bid/53355/info

iGuard Security Access Control is prone to a cross-site scripting vulnerability because it fails to properly sanitize user-supplied input in the embedded web server.

An attacker may leverage this issue to execute arbitrary script code in the browser of an unsuspecting user in the context of the affected site. This may allow the attacker to steal cookie-based authentication credentials and launch other attacks. 

http://www.example.com/></font><IFRAME SRC="JAVASCRIPT:alert('XSS Found by Usman Saeed , Xc0re Security Research Group');">.asp