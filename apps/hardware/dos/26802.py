source: https://www.securityfocus.com/bid/15757/info

VPN-1 SecureClient is reported prone to a policy bypass vulnerability. This issue is due to a failure of the application to securely implement remote administrator-provided policies on affected computers.

This issue allows remote VPN users to bypass the administratively-defined security policies. Specific issues arising from this vulnerability depend on the intended policies defined by administrators. Some examples of the consequences are: unauthorized computers may connect, scripts may not execute, or insecure network configurations may be possible. 

:Loop
copy x.scv local.scv
goto Loop