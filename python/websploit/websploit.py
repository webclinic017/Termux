#!/usr/bin/env python
# 
#            --------------------------------------------------
#                            WebSploit Framework          
#            --------------------------------------------------
#        Copyright (C) <2012>  <0x0ptim0us (Fardin Allahverdinazhand)>
#
#        This program is free software: you can redistribute it and/or modify
#        it under the terms of the GNU General Public License as published by
#        the Free Software Foundation, either version 3 of the License, or
#        any later version.
#
#        This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#        You should have received a copy of the GNU General Public License
#        along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
#
#    WebSploit Advanced MITM Framework
#    
#    
#    About Author :
#    
#    Founder : 0x0ptim0us (Fardin Allahverdinazhand)
#    Location : Iran - Azarbaycan
#    Email : 0x0ptim0us@Gmail.com
#    Project In SourceForge : https://sourceforge.net/p/websploit/wiki/Home/
#    Blog : www.websploit.ir
#
import os
import readline, rlcompleter
from time import sleep
from core import wcolors
from core import menu
from core import header
from core import modules_database
from core import help
from core import upgrade
from core import update
from core import about
from modules import apache_users
from modules import wmap
from modules import directory_scanner
from modules import phpmyadmin
from modules import cloudflare_resolver
from modules import arp_dos
from modules import autopwn
from modules import mitm
from modules import mlitm
from modules import mfod
from modules import arp_poisoner
from modules import webkiller
from modules import brow_autopwn
from modules import java_applet
from modules import wifi_jammer
from modules import wifi_dos
from modules import wifi_honeypot
from modules import mass_deauth
from modules import bluetooth_pod
from modules.fakeupdate import fakeupdate

def main():
    try:
        line_1 = wcolors.color.UNDERL + wcolors.color.BLUE + "wsf" + wcolors.color.ENDC
        line_1 += " > "
        terminal = raw_input(line_1)
        if terminal[0:3] =='use':
            if terminal[4:20] =='web/apache_users':
                apache_users.apache_users()
                main()
            if terminal[4:27] =='web/cloudflare_resolver':
                cloudflare_resolver.cloudflare_resolver()
                main()
            elif terminal[4:20] =='network/arp_dos':
                arp_dos.arp_dos()
                main()
            elif terminal[4:20] =='exploit/autopwn':
                autopwn.autopwn()
                main()
            elif terminal[4:27] =='exploit/browser_autopwn':
                brow_autopwn.brow_autopwn()
                main()
            elif terminal[4:19] == 'web/dir_scanner':
                directory_scanner.directory_scanner()
                main()
            elif terminal[4:12] =='web/wmap':
                wmap.wmap()
                main()
            elif terminal[4:11] =='web/pma':
                phpmyadmin.phpmyadmin()
                main()
            elif terminal[4:23] =='exploit/java_applet':
                java_applet.java_applet()
                main()
            elif terminal[4:16] =='network/mfod':
                mfod.mfod()
                main()
            elif terminal[4:16] =='network/mitm':
                mitm.mitm()
                main()
            elif terminal[4:17] =='network/mlitm':
                mlitm.mlitm()
                main()
            elif terminal[4:21] =='network/webkiller':
                webkiller.webkiller()
                main()
            elif terminal[4:24] =='network/arp_poisoner':
                arp_poisoner.arp_poisoner()
                main()
            elif terminal[4:22] =='network/fakeupdate':
                fakeupdate.fakeupdate()
                main()
            elif terminal[4:20] =='wifi/wifi_jammer':
                wifi_jammer.wifi_jammer()
                main()
            elif terminal[4:17] =='wifi/wifi_dos':
                wifi_dos.wifi_dos()
                main()
            elif terminal[4:22] =='wifi/wifi_honeypot':
                wifi_honeypot.wifi_honeypot()
                main()
            elif terminal[4:20] =='wifi/mass_deauth':
                mass_deauth.mass_deauth()
                main()
            elif terminal[4:27] =='bluetooth/bluetooth_pod':
                bluetooth_pod.bluetooth_pod()
                main()
        elif terminal[0:12] == 'show modules':
            modules_database.modules_database()
            main()
        elif terminal[0:4] =='help':
            help.help()
            main()
        elif terminal[0:2] =='os':
            os.system(terminal[3:])
            main()
        elif terminal[0:7] =='upgrade':
            upgrade.upgrade()
            main()
        elif terminal[0:6] =='update':
            update.update()
        elif terminal[0:5] =='about':
            about.about()
            main()
        elif terminal[0:4] =='exit':
            exit()
        else:
            print "Wrong Command => ", terminal
            main()
    except(KeyboardInterrupt):
        print(wcolors.color.RED + "\n[*] (Ctrl + C ) Detected, Trying To Exit ..." + wcolors.color.ENDC)
        print(wcolors.color.YELLOW + "[*] Thank You For Using Websploit Framework =)" + wcolors.color.ENDC)
def start():
    header.main_header()
    menu.main_info()
    main()
if __name__=='__main__':
    start()
