source: https://www.securityfocus.com/bid/47390/info

Technicolor THOMSON TG585v7 Wireless Router is prone to a cross-site scripting vulnerability because the application fails to properly sanitize user-supplied input.

Attackers may exploit this issue by enticing victims into visiting a malicious site.

An attacker may leverage this issue to execute arbitrary script code in the browser of an unsuspecting user in the context of the affected device. This may allow the attacker to steal cookie-based authentication credentials and to launch other attacks.

Firmware versions prior to 8.2.7.6 are vulnerable. 

http://www.example.com/cgi/b/ic/connect/?url=[XSS]