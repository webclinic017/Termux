# Exploit Title: Vulnerability XSS - Dreambox
# Shodan Dork: Dreambox 200 
# Date: 12/10/2017
# Exploit Author: Thiago "THX" Sena
# Vendor Homepage: https://www.dreamboxupdate.com
# Version: 2.0.0
# Tested on: kali linux, windows 7, 8.1, 10
# CVE : CVE-2017-15287

Vulnerabilty: Cross-site scripting (XSS) in plugin BouquetEditor

---------------------------------------------------------------

PoC: 

- First you go to ( http://IP:PORT/bouqueteditor/ )

- Then you go to the Bouquets tab, add a new bouquet

- Then put the script (<script>alert(1)</script>)

- Xss Vulnerability