source: https://www.securityfocus.com/bid/28902/info

F5 Networks FirePass 4100 SSL VPN devices are prone to a cross-site scripting vulnerability because they fail to properly sanitize user-supplied input.

An attacker may leverage this issue to execute arbitrary script code in the browser of an unsuspecting user in the context of the affected site. This may help the attacker to steal cookie-based authentication credentials and to launch other attacks.

FirePass 4100 SSL VPN Firmware 5.4.2-5.5.2 and 6.0-6.2 are vulnerable. 

http://www.example.com/installControl.php3?1&%22%3E%3C/script%3E%3Ctextarea%3EHtml%20injection%3C/textarea%3E%3C!--= http://www.example.com/installControl.php3?>'"><script>alert(514)</script>