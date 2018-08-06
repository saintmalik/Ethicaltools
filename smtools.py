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
        print "    [81] GetDroid"
        print "    [82] OhMyQR"
        print "    [83] ShellPhish"
        print "    [84] BlackEye"
        print "    [85] Locator"
        print "    [86] FakeAp"
        print "    [87] FaceBash"
        print "    [88] DdosTor"
        print "    [89] GetWin"
        print "    [90] BruteCMS"
        print "    [91] InstaInsane"
        print "    [92] InstaShell"
        print "    [93] ChoiceBot"
        print "    [94] TheChoice"
        print "    [95] FashSSH"
        print "    [96] VenomGen"
        print "    [97] SqlScan"
        print "    [98] GetIp"
        print "    [99] DorkShell"
        print "    [100] WordlistCreator"
        print "    [101] MultiTor"
        print "    [102] Infog"
        print "    [103] BruteHTTP"
        print "    [104] Clickjacting Tester"
        print "    [105] PyDDOS"
        print "    [106] Xnmap"
        print "    [107] TorAttack"
        print "    [108] TweetShell"
        print "    [109] YouBot"
        print "    [110] BotSql"
        print "    [111] DebianTools"
        print "    [112] SwitchTor"
        print "    [113] NetScanP"
        print "    [114] InstaPost"
        print "    [115] AntiFlood"
        print "    [116] BlockTor"
        print "    [117] HackWin"
        print "    [118] SHHScan"
        print "    [119] SynFlood"
        print "    [120] TelnetScan"
        print "    [121] Tmux-Config-Reset"
        print "    [122] Fluxion"
        print "    [123] Hasherdotid"
        print "    [124] Namechk"
        print "    [125] MSF-pg"
        print "    [126] BeanShell"
        print "    [127] xl-py"
        print "    [128] Lolz_RAT"
        print "    [129] CrewBot"
        print "    [130] Green-Reaper"
        print "    [131] Ipmux"
        print "    [132] Termux-Api"
        print "    [133] MultiSpam"
        print "    [134] JoomScan"
        print "    [135] TouchURL"
        print "    [136] WebConn"
        print "    [137] Binary Exploitation"
        print "    [138] Apache2"
        print "    [139] SSH"
        print "    [140] FileLocker"
        print "    [141] Fish"
        print "    [142] Httrack"
        print "    [143] Exit from smtools\n" 
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
                        planetwork_ddos()
        elif smtool == "27":
                        hydra()
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
                        spammer_email()
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
                        get()
        elif smtool == "82":
                        ohm()
        elif smtool == "83":
                        shell()
        elif smtool == "84":
                        blk()
        elif smtool == "85":
                        lct()
        elif smtool == "86":
                        fap()
        elif smtool == "87":
                        fab()
        elif smtool == "88":
                        dot()
        elif smtool == "89":
                        gew()
        elif smtool == "90":
                        cmsb()
        elif smtool == "91":
                        sant()
        elif smtool == "92":
                        sht()
        elif smtool == "93":
                        chb()
        elif smtool == "94":
                        tch()
        elif smtool == "95":
                        fsh()
        elif smtool == "96":
                        vnm()
        elif smtool == "97":
                        sqsc()
        elif smtool == "98":
                        getip()
        elif smtool == "99":
                        duck()
        elif smtool == "100":
                        wlc()
        elif smtool == "101":
                        mut()
        elif smtool == "102":
                        fog()
        elif smtool == "103":
                        httpb()
        elif smtool == "104":
                        cljt()
        elif smtool == "105":
                        pydos()
        elif smtool == "106":
                        xnmap()
        elif smtool == "107":
                        rot()
        elif smtool == "108":
                        tweet()
        elif smtool == "109":
                        ybot()
        elif smtool == "110":
                        sbot()
        elif smtool == "111":
                        debtool()
        elif smtool == "112":
                        switor()
        elif smtool == "113":
                        netsp()
        elif smtool == "114":
                        instapost()
        elif smtool == "115":
                        antiflood()
        elif smtool == "116":
                        blckt()
        elif smtool == "117":
                        hckw()
        elif smtool == "118":
                        sshs()
        elif smtool == "119":
                        synf()
        elif smtool == "120":
                        telscan()
        elif smtool == "121":
                        reset()
        elif smtool == "122":
                        flux()
        elif smtool == "123":
                        hasherdotid()
        elif smtool == "124":
                        namechk()
        elif smtool == "125":
                        msfpg()
        elif smtool == "126":
                        beanshell()
        elif smtool == "127":
                        xlPy()
        elif smtool == "128":
                        lolrat()
        elif smtool == "129":
                        crewbot()
        elif smtool == "130":
                        greap()
        elif smtool == "131":
                        ipu()
        elif smtool == "132":
                        tapi()
        elif smtool == "133":
                        mspam()
        elif smtool == "134":
                        jmscan()
        elif smtool == "135":
                        tochurl()
        elif smtool == "136":
                        webconn()
        elif smtool == "137":
                        binploit()
        elif smtool == "138":
                        apache()
        elif smtool == "139":
                        openssh()
        elif smtool == "140":
                        fileloc()
        elif smtool == "141":
                        fsh()
        elif smtool == "142":
                        httrack()
	
	elif smtool == "143":
		sys.exit()
	        print "\nBYE!!!!!"
	else:
		print "\nERROR: Wrong Input"
		timeout(2)
		restart_program()

if __name__ == "__main__":
	main()
