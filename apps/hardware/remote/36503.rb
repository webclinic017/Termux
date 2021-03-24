source: https://www.securityfocus.com/bid/51156/info

Barracuda Control Center 620 is prone to an HTML injection vulnerability and multiple cross-site scripting vulnerabilities because it fails to properly sanitize user-supplied input.

Successful exploits will allow attacker-supplied HTML and script code to run in the context of the affected browser, potentially allowing the attacker to steal cookie-based authentication credentials or control how the site is rendered to the user. Other attacks are also possible. 

https://www.example.com/bcc/editdevices.jsp?device-type=spyware&selected-node=1&containerid=[IVE]
https://www.example.com/bcc/main.jsp?device-type=[IVE]