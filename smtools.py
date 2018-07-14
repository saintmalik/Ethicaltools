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
        print "    [29] Xshell"
        print "    [30] santet-online"
        print "    [31] SMfbBrute"
        print "    [32] Metasploit"
        print "    [33] commix"
        print "    [34] sqlmap"
        print "    [35] Brutal"
        print "    [36] A-Rat"
        print "    [37] WPSploit"
        print "    [38] Websploit"
        print "    [39] Routersploit"
        print "    [40] BlackBox"
        print "    [41] XAttacker"
        print "    [42] TXTool"
        print "    [43] KnockMail"
        print "    [44] Spammer-Grab"
        print "    [45] Hac"
        print "    [46] Spammer-Email"
        print "    [47] SocialFish"
        print "    [48] SMEmailBrute"
        print "    [49] SpazSMS"
        print "    [50] SpiderBot"
        print "    [51] Ngrok"
        print "    [52] Sudo"
        print "    [53] Ubuntu"
        print "    [54] Fedora"
        print "    [55] Kali Nethunter"
        print "    [56] VCRT"
        print "    [57] E-Code"
        print "    [58] Termux-Styling"
        print "    [60] PassGen"
        print "    [61] Cookie-Stealer"
        print "    [62] AngryFuzzer"
        print "    [63] Cloak"
        print "    [64] LITEOTP"
        print "    [65] Opitva-Framework"
        print "    [66] Zoom"
        print "    [67] SCANNER-INURLBR"
        print "    [68] Zones"
        print "    [69] admin-panel-finder"
        print "    [70] Infinity"
        print "    [71] Exit from smtools\n" 
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
                        wtf()
        elif smtool == "22":
                        easyMap()
        elif smtool == "23":
                        blackbox()
        elif smtool == "24":
                        xd3v()
        elif smtool == "25":
                        crips()
        elif smtool == "26":
                        sir()
        elif smtool == "27":
                        evilURL()
        elif smtool == "28":
                        striker()
        elif smtool == "29":
                        xshell()
        elif smtool == "30":
                        owscan()
        elif smtool == "31":
                        osif()
        elif smtool == "32":
                        wtf()
        elif smtool == "33":
                        easyMap()
        elif smtool == "34":
                        blackbox()
        elif smtool == "35":
                        xd3v()
        elif smtool == "36":
                        crips()
        elif smtool == "37":
                        sir()
        elif smtool == "38":
                        evilURL()
        elif smtool == "39":
                        striker()
        elif smtool == "40":
                        xshell()
        elif smtool == "41":
                        owscan()
        elif smtool == "42":
                        osif()
        elif smtool == "43":
                        wtf()
        elif smtool == "44":
                        easyMap()
        elif smtool == "45":
                        blackbox()
        elif smtool == "46":
                        xd3v()
        elif smtool == "47":
                        crips()
        elif smtool == "48":
                        sir()
        elif smtool == "49":
                        evilURL()
        elif smtool == "50":
                        striker()
        elif smtool == "51":
                        xshell()
        elif smtool == "52":
                        owscan()
        elif smtool == "53":
                        osif()
        elif smtool == "54":
                        wtf()
        elif smtool == "55":
                        easyMap()
        elif smtool == "56":
                        blackbox()
        elif smtool == "57":
                        xd3v()
        elif smtool == "58":
                        crips()
        elif smtool == "59":
                        sir()
        elif smtool == "60":
                        evilURL()
        elif smtool == "61":
                        striker()
        elif smtool == "62":
                        xshell()
        elif smtool == "63":
                        owscan()
        elif smtool == "64":
                        osif()
        elif smtool == "65":
                        wtf()
        elif smtool == "66":
                        easyMap()
        elif smtool == "67":
                        blackbox()
        elif smtool == "68":
                        xd3v()
        elif smtool == "69":
                        crips()
        elif smtool == "70":
                        sir()
	
	elif smtool == "71":
		sys.exit()
	
	else:
		print "\nERROR: Wrong Input"
		timeout(2)
		restart_program()

if __name__ == "__main__":
	main()
