source: https://www.securityfocus.com/bid/56156/info

FirePass SSL VPN is prone to a URI-redirection vulnerability because the application fails to properly sanitize user-supplied input.

A successful exploit may aid in phishing attacks; other attacks are possible.

Versions prior to FirePass 7.0.0 HF-70-7 and 6.1.0 HF-610-9 are vulnerable. 

http://www.example.com/my.activation.cns.php3?langchar=&ui_translation=&refreshURL==http://attacker