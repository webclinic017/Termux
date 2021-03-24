#!/usr/bin/python
"""
SQLdump v1.0
Date: 06-12-2017 (18:19)
Author: DedSecTL
Team: BlackHole Security
Blog: http://droidsec9798-com.mwapblog.com
"""
import os
import sys
from googlesearch import search

#--- color ---#
Y = '\033[1;33m' # Yellow
R = '\033[1;31m' # Red
N = '\033[0m'    # Normal
G = '\033[1;37m' # Grey
#-------------#

if sys.platform == 'linux' or sys.platform == 'linux2':
	os.system("clear")
elif sys.platform == 'win32' or sys.platform == 'win64':
	os.system("cls")
else:
	os.system("clear")
print "%s           _    _                                 %s" % (Y,N)
print "%s ___  ___ | | _| | _ _  _____  ___  %s{%s1.0##version%s} %s" % (Y,G,Y,G,N)
print "%s|_ -|| . || || . || | ||     || . | %s{%ssqldump#lulz%s} %s" % (Y,G,Y,G,N)
print "%s|___||_  ||_||___||___||_|_|_||  _| %s{%sDedSecTL#dev%s} %s" % (Y,G,Y,G,N)
print "%s       |_| %s06-12-2017 (18:19)%s |_|                 %s" % (Y,G,Y,N)
print
sqldump = raw_input("%ssqldump (%sex: credits, sekolah, food%s):%s "  % (Y,G,Y,G))
print(N)
query = 'inurl:%s.php?id=' %sqldump
domain = 'com'

for result in search(query, tld=""+domain+"", num=30, stop=40):
	print(result)
	dumpit=raw_input("%sDump the result? %s[y]es [N]o [q]uit\n" % (Y,G))
	if dumpit == 'y' or dumpit == 'Y':
		dumpitas=raw_input("%ssqldump (%sex: Dump it as example.txt%s): %sDump it as " % (Y,G,Y,G))
		try:
			file = open(""+dumpitas+"", 'w')
			file.write("%s" %result)
			file.close()
			print "[*] Successful."
		except IOError, e:
			print "[!] ERROR:",e
			sys.exit()
	elif dumpit == 'n' or dumpit == 'N':
		pass
	elif dumpit == 'q' or dumpit == 'Q':
		print(N)
		sys.exit()