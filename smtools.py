## smtools.py - Smtools v3.0
# -*- coding: utf-8 -*-
import os
import sys
from time import sleep as timeout
from core.smtcore import *

def main():
	banner()
        print "    [01] Nmap"
        print "    [02] Red Hawk"
	print "    [03] D-Tect"
        print "    [04] sqlmap"
	print "    [05] Infoga"
	print "    [06] ReconDog"
	print "    [07] AndroZenmap"
        print "    [08] sqlmate"
        print "    [09] AstraNmap"
	print "    [10] WTF"
	print "    [11] Easymap"
	print "    [12] BlackBox"
	print "    [13] XD3v"
	print "    [14] Crips"
	print "    [15] SIR"
	print "    [16] EvilURL"
	print "    [17] Striker"
	print "    [18] Xshell"
	print "    [19] OWScan"
	print "    [20] OSIF"
        print "    [21] Torshammer"
        print "    [22] Slowloris"
        print "    [23] InfoSploit"
        print "    [24] GoldenEye"
        print "    [25] Xerxes"
        print "    [26] Planetwork-DDOS"
        print "    [27] Hydra"
        print "    [28] Black Hydra"
        print "    [29] Optiva-Framework"
        print "    [30] santet-online"
        print "    [31] SMfbBrute"
        print "    [32] Metasploit"
        print "    [33] commix"
        print "    [34] sqlscan"
        print "    [35] Brutal"
        print "    [36] A-Rat"
        print "    [37] WPSploit"
        print "    [38] Websploit"
        print "    [39] Routersploit"
        print "    [40] BlackBox"
        print "    [41] XAttacker"
        print "    [42] TXTool"
        print "    [43] Cloak"
        print "    [44] Rat_Hunter"
        print "    [45] Locky"
        print "    [46] ShodanHat"
        print "    [47] HatCloud"
        print "    [48] Blazy"
        print "    [49] Droid-Hunter"
        print "    [50] DSSS"
        print "    [51] InstaHack"
        print "    [52] Termux-Styling"
        print "    [53] PassGen"
        print "    [54] Cookie-Stealer"
        print "    [55] Hash_Buster"
        print "    [56] KnockMail"
        print "    [57] Spammer-Grab"
        print "    [58] Hac"
        print "    [59] Spammer-Email"
        print "    [60] SocialFish"
        print "    [61] SMEmailBrute"
        print "    [62] SpazSMS"
        print "    [63] SpiderBot"
        print "    [64] Ngrok"
        print "    [65] Sudo"
        print "    [66] Ubuntu"
        print "    [67] Fedora"
        print "    [68] Kali Nethunter"
        print "    [69] VCRT"
        print "    [70] E-Code"
        print "    [71] Rang3r"
        print "    [72] XSStrike"
        print "    [73] Hash_Buster"
        print "    [74] Cupp"
        print "    [75] LITEOTP"
        print "    [76] Zoom"
        print "    [77] SCANNER-INURLBR"
        print "    [78] Zones"
        print "    [79] admin-panel-finder"
        print "    [80] Infinity"
        print "    [81] Exit from smtools\n" 
        smtool = raw_input("smts > ")
		
	if smtool == "1" or smtool == "01":
			nmap()
	elif smtool == "2" or smtool == "02":
			red_hawk()
	elif smtool == "3" or smtool == "03":
			dtect()
	elif smtool == "4" or smtool == "04":
			sqlmap()
	elif smtool == "5" or smtool == "05":
			infoga()
	elif smtool == "6" or smtool == "06":
			reconDog()
	elif smtool == "7" or smtool == "07":
			androZenmap()
	elif smtool == "8" or smtool == "08":
			sqlmate()
	elif smtool == "9" or smtool == "09":
			astraNmap()
	elif smtool == "10":
         		wtf()
	elif smtool == "11":
			easyMap()
	elif smtool == "12":
			blackbox()
	elif smtool == "13":
			xd3v()
	elif smtool == "14":
			crips()
	elif smtool == "15":
			sir()
	elif smtool == "16":
			evilURL()
	elif smtool == "17":
			striker()
	elif smtool == "18":
			xshell()
	elif smtool == "19":
			owscan()
	elif smtool == "20":
			osif()
        elif smtool == "21":
                        torshammer()
        elif smtool == "22":
                        slowloris()
        elif smtool == "23":
                        info()
        elif smtool == "24":
                        goldeneye()
        elif smtool == "25":
                        xerxes()
        elif smtool == "26":
                        planetwork_ddos
        elif smtool == "27":
                        hydra
        elif smtool == "28":
                        black_hydra()
        elif smtool == "29":
                        optiva()
        elif smtool == "30":
                        sanlen()
        elif smtool == "31":
                        smfb()
        elif smtool == "32":
                        metasploit()
        elif smtool == "33":
                        commix()
        elif smtool == "34":
                        sqlscan()
        elif smtool == "35":
                        brutal()
        elif smtool == "36":
                        a_rat()
        elif smtool == "37":
                        wpsploit()
        elif smtool == "38":
                        websploit()
        elif smtool == "39":
                        routersploit
        elif smtool == "40":
                        blackbox()
        elif smtool == "41":
                        xattacker()
        elif smtool == "42":
                        txtool()
        elif smtool == "43":
                        cloak()
        elif smtool == "44":
                        rat()
        elif smtool == "45":
                        locky()
        elif smtool == "46":
                        shodan()
        elif smtool == "47":
                        hatcloud()
        elif smtool == "48":
                        blazy()
        elif smtool == "49":
                        droid()
        elif smtool == "50":
                        dsss()
        elif smtool == "51":
                        instaHack()
        elif smtool == "52":
                        stylemux()
        elif smtool == "53":
                        passgencvar
        elif smtool == "54":
                        cook()
        elif smtool == "55":
                        hash_buster()
        elif smtool == "56":
                        knockmail()
        elif smtool == "57":
                        spammer_grab
        elif smtool == "58":
                        hac()
        elif smtool == "59":
                        spammer_email
        elif smtool == "60":
                        socfish()
        elif smtool == "61":
                        smbrute()
        elif smtool == "62":
                        spazsms()
        elif smtool == "63":
                        spiderbot()
        elif smtool == "64":
                        ngrok()
        elif smtool == "65":
                        sudo()
        elif smtool == "66":
                        ubuntu()
        elif smtool == "67":
                        fedora()
        elif smtool == "68":
                        nethunter()
        elif smtool == "69":
                        vcrt()
        elif smtool == "70":
                        ecode()
        elif smtool == "71":
                        rang3r()
        elif smtool == "72":
                        xsstrike()
        elif smtool == "73":
                        hasher()
        elif smtool == "74":
                        cupp()
        elif smtool == "75":
                        lite()
        elif smtool == "76":
                        zoom()
        elif smtool == "77":
                        inurl()
        elif smtool == "78":
                        zones()
        elif smtool == "79":
                        admin()
        elif smtool == "80":
                        infinit()
	
	elif smtool == "81":
		sys.exit()
	
	else:
		print "\nERROR: Wrong Input"
		timeout(2)
		restart_program()

if __name__ == "__main__":
	main()
