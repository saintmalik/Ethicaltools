## smtools.py - useful module of Smtools
# -*- coding: utf-8 -*-
import os
import sys
import time

smtools_banner = """
   ███████╗███╗   ███╗████████╗ ██████╗  ██████╗ ██╗     ███████╗
   ██╔════╝████╗ ████║╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
   ███████╗██╔████╔██║   ██║   ██║   ██║██║   ██║██║     ███████╗
   ╚════██║██║╚██╔╝██║   ██║   ██║   ██║██║   ██║██║     ╚════██║
   ███████║██║ ╚═╝ ██║   ██║   ╚██████╔╝╚██████╔╝███████╗███████║
   ╚══════╝╚═╝     ╚═╝   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝V3
            [*]=====================================[*]
            [*]-------[Coded by SaintMalik ]--------[*]
            [*]-------[Team: KnightMask-Team ]------[*]
            [*]-----[youtube.com/SaintMalik Tech]---[*]
            [*]=====================================[*]
"""
backtomenu_banner = """
  [77] Back to main menu
  [00] Exit the SMTOOLS
"""
def restart_program():
	python = sys.executable
	os.execl(python, python, * sys.argv)
	curdir = os.getcwd()

def backtomenu_option():
	print backtomenu_banner
	backtomenu = raw_input("smts > ")
	
	if backtomenu == "99":
		restart_program()
	elif backtomenu == "00":
		sys.exit()
	else:
		print "\nERROR: Wrong Input"
		time.sleep(2)
		restart_program()

def banner():
	print smtools_banner

def nmap():
	print '\n###### Installing Nmap'
	os.system('apt update && apt upgrade')
	os.system('apt install nmap')
	print '###### Done'
	print "###### Type 'nmap' to start."
	backtomenu_option()

def red_hawk():
	print '\n###### Installing RED HAWK'
	os.system('apt update && apt upgrade')
	os.system('apt install git php')
	os.system('git clone https://github.com/Tuhinshubhra/RED_HAWK')
	os.system('mv RED_HAWK ~')
	print '###### Done'
	backtomenu_option()

def dtect():
	print '\n###### Installing D-Tect'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/shawarkhanethicalhacker/D-TECT')
	os.system('mv D-TECT /$HOME')
	print '###### Done'
	backtomenu_option()

def sqlmap():
	print '\n###### Installing sqlmap'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2')
	os.system('git clone https://github.com/sqlmapproject/sqlmap')
	os.system('mv sqlmap /$HOME')
	print '###### Done'
	backtomenu_option()

def infoga():
	print '\n###### Installing Infoga'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('pip2 install requests urllib3 urlparse')
	os.system('git clone https://github.com/m4ll0k/Infoga')
	os.system('mv Infoga ~')
	print '###### Done'
	backtomenu_option()

def reconDog():
	print '\n###### Installing ReconDog'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/UltimateHackers/ReconDog')
	os.system('mv ReconDog ~')
	print '###### Done'
	backtomenu_option()

def androZenmap():
	print '\n###### Installing AndroZenmap'
	os.system('apt update && apt upgrade')
	os.system('apt install nmap curl')
	os.system('curl -O http://override.waper.co/files/androzenmap.txt')
	os.system('mkdir ~/AndroZenmap')
	os.system('mv androzenmap.txt ~/AndroZenmap/androzenmap.sh')
	print '###### Done'
	backtomenu_option()

def sqlmate():
	print '\n###### Installing sqlmate'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('pip2 install mechanize bs4 HTMLparser argparse requests urlparse2')
	os.system('git clone https://github.com/UltimateHackers/sqlmate')
	os.system('mv sqlmate ~')
	print '###### Done'
	backtomenu_option()

def astraNmap():
	print '\n###### Installing AstraNmap'
	os.system('apt update && apt upgrade')
	os.system('apt install git nmap')
	os.system('git clone https://github.com/Gameye98/AstraNmap')
	os.system('mv AstraNmap ~')
	print '###### Done'
	backtomenu_option()

def wtf():
	print '\n###### Installing WTF'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2')
	os.system('pip2 bs4 requests HTMLParser urlparse mechanize argparse')
	os.system('git clone https://github.com/Xi4u7/wtf')
	os.system('mv wtf ~')
	print '###### Done'
	backtomenu_option()

def easyMap():
	print '\n###### Installing Easymap'
	os.system('apt update && apt upgrade')
	os.system('apt install php git')
	os.system('git clone https://github.com/Cvar1984/Easymap')
	os.system('mv Easymap ~')
	os.system('cd ~/Easymap && sh install.sh')
	print '###### Done'
	backtomenu_option()

def xd3v():
	print '\n###### Installing XD3v'
	os.system('apt update && apt upgrade')
	os.system('apt install curl')
	os.system('curl -k -O https://gist.github.com/Gameye98/92035588bd0228df6fb7fa77a5f26bc2/raw/f8e73cd3d9f2a72bd536087bb6ba7bc8baef7d1d/xd3v.sh')
	os.system('mv xd3v.sh ~/../usr/bin/xd3v && chmod +x ~/../usr/bin/xd3v')
	print '###### Done'
	print "###### Type 'xd3v' to start."
	backtomenu_option()

def crips():
	print '\n###### Installing Crips'
	os.system("apt update && apt upgrade")
	os.system("apt install git python2 openssl curl libcurl wget")
	os.system("git clone https://github.com/Manisso/Crips")
	os.system("mv Crips ~")
	print '###### Done'
	backtomenu_option()

def sir():
	print '\n###### Installing SIR'
	os.system("apt update && apt upgrade")
	os.system("apt install python2 git")
	os.system("pip2 install bs4 urllib2")
	os.system("git clone https://github.com/AeonDave/sir.git")
	os.system("mv sir ~")
	print '###### Done'
	backtomenu_option()

def xshell():
	print '\n###### Installing Xshell'
	os.system("apt update && apt upgrade")
	os.system("apt install lynx python2 figlet ruby php nano w3m")
	os.system("git clone https://github.com/Ubaii/Xshell")
	os.system("mv Xshell ~")
	print '###### Done'
	backtomenu_option()

def evilURL():
	print '\n###### Installing EvilURL'
	os.system("apt update && apt upgrade")
	os.system("apt install git python2 python3")
	os.system("git clone https://github.com/UndeadSec/EvilURL")
	os.system("mv EvilURL ~")
	print '###### Done'
	backtomenu_option()

def striker():
	print '\n###### Installing Striker'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2')
	os.system('git clone https://github.com/UltimateHackers/Striker')
	os.system('mv Striker ~')
	os.system('cd ~/Striker && pip2 install -r requirements.txt')
	print '###### Done'
	backtomenu_option()

def dsss():
	print '\n###### Installing DSSS'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/stamparm/DSSS')
	os.system('mv DSSS ~')
	print '###### Done'
	backtomenu_option()

def sqliv():
	print '\n###### Installing SQLiv'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/Hadesy2k/sqliv')
	os.system('mv sqliv ~')
	print '###### Done'
	backtomenu_option()

def sqlscan():
	print '\n###### Installing sqlscan'
	os.system('apt update && apt upgrade')
	os.system('apt install git php')
	os.system('git clone http://www.github.com/Cvar1984/sqlscan')
	os.system('mv sqlscan ~')
	print '###### Done'
	backtomenu_option()

def wordpreSScan():
	print '\n###### Installing Wordpresscan'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 python2-dev clang libxml2-dev libxml2-utils libxslt-dev')
	os.system('git clone https://github.com/swisskyrepo/Wordpresscan')
	os.system('mv Wordpresscan ~')
	os.system('cd ~/Wordpresscan && pip2 install -r requirements.txt')
	print '###### Done'
	backtomenu_option()

def wpscan():
	print '\n###### Installing WPScan'
	os.system('apt update && apt upgrade')
	os.system('apt install git ruby curl')
	os.system('git clone https://github.com/wpscanteam/wpscan')
	os.system('mv wpscan ~ && cd ~/wpscan')
	os.system('gem install bundle && bundle config build.nokogiri --use-system-libraries && bundle install && ruby wpscan.rb --update')
	print '###### Done'
	backtomenu_option()

def wordpresscan():
	print '\n###### Installing wordpresscan(2)'
	os.system('apt update && apt upgrade')
	os.system('apt install nmap figlet git')
	os.system('git clone https://github.com/silverhat007/termux-wordpresscan')
	os.system('cd termux-wordpresscan && chmod +x * && sh install.sh')
	os.system('mv termux-wordpresscan ~')
	print '###### Done'
	print "###### Type 'wordpresscan' to start."
	backtomenu_option()

def routersploit():
	print '\n###### Installing Routersploit'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('pip2 install requests')
	os.system('git clone https://github.com/reverse-shell/routersploit')
	os.system('mv routersploit ~;cd ~/routersploit;pip2 install -r requirements.txt;termux-fix-shebang rsf.py')
	print '###### Done'
	backtomenu_option()

def torshammer():
	print '\n###### Installing Torshammer'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/dotfighter/torshammer')
	os.system('mv torshammer /$HOME')
	print '###### Done'
	backtomenu_option()

def slowloris():
	print '\n###### Installing Slowloris'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/gkbrk/slowloris')
	os.system('mv slowloris /$HOME')
	print '###### Done'
	backtomenu_option()

def fl00d12():
	print '\n###### Installing Fl00d & Fl00d2'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 wget')
	os.system('mkdir ~/fl00d')
	os.system('wget http://override.waper.co/files/fl00d.apk')
	os.system('wget http://override.waper.co/files/fl00d2.apk')
	os.system('mv fl00d.apk ~/fl00d/fl00d.py;mv fl00d2.apk ~/fl00d/fl00d2.py')
	print '###### Done'
	backtomenu_option()

def goldeneye():
	print '\n###### Installing GoldenEye'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2')
	os.system('git clone https://github.com/jseidl/GoldenEye')
	os.system('mv GoldenEye /$HOME')
	print '###### Done'
	backtomenu_option()

def xerxes():
	print '\n###### Installing Xerxes'
	os.system('apt update && apt upgrade')
	os.system('apt install git')
	os.system('apt install clang')
	os.system('git clone https://github.com/zanyarjamal/xerxes')
	os.system('mv xerxes /$HOME')
	os.system('cd ~/xerxes && clang xerxes.c -o xerxes')
	print '###### Done'
	backtomenu_option()

def planetwork_ddos():
	print '\n###### Installing Planetwork-DDOS'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2')
	os.system('git clone https://github.com/Hydra7/Planetwork-DDOS')
	os.system('mv Planetwork-DDOS /$HOME')
	print '###### Done'
	backtomenu_option()

def hydra():
	print '\n###### Installing Hydra'
	os.system('apt update && apt upgrade')
	os.system('apt install hydra /$HOME')
	print '###### Done'
	backtomenu_option()

def black_hydra():
	print '\n###### Installing Black Hydra'
	os.system('apt update && apt upgrade')
	os.system('apt install hydra git python2')
	os.system('git clone https://github.com/Gameye98/Black-Hydra')
	os.system('mv Black-Hydra /$HOME')
	print '###### Done'
	backtomenu_option()

def cupp():
	print '\n###### Installing Cupp'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/Mebus/cupp')
	os.system('mv cupp /$HOME')
	print '###### Done'
	backtomenu_option()

def leethash():
	print '\n###### Installing 1337Hash'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2')
	os.system('git clone https://github.com/Gameye98/1337Hash')
	os.system('mv 1337Hash ~')
	print '###### Done'
	backtomenu_option()

def hash_buster():
	print '\n###### Installing Hash-Buster'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/UltimateHackers/Hash-Buster')
	os.system('mv Hash-Buster /$HOME')
	print '###### Done'
	backtomenu_option()

def instaHack():
	print '\n###### Installing InstaHack'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('pip2 install requests')
	os.system('git clone https://github.com/avramit/instahack')
	os.system('mv instahack /$HOME')
	print '###### Done'
	backtomenu_option()

def webdav():
	print '\n###### Installing Webdav'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 openssl curl libcurl')
	os.system('pip2 install urllib3 chardet certifi idna requests')
	os.system('mkdir ~/webdav')
	os.system('curl -k -O http://override.waper.co/files/webdav.txt;mv webdav.txt ~/webdav/webdav.py')
	print '###### Done'
	backtomenu_option()

def xGans():
	print '\n###### Installing xGans'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 curl')
	os.system('mkdir ~/xGans')
	os.system('curl -O http://override.waper.co/files/xgans.txt')
	os.system('mv xgans.txt ~/xGans/xgans.py')
	print '###### Done'
	backtomenu_option()

def wpsploit():
	print '\n###### Installing WPSploit'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('git clone git clone https://github.com/m4ll0k/wpsploit')
	os.system('mv wpsploit /$HOME')
	print '###### Done'
	backtomenu_option()

def sqldump():
	print '\n###### Installing sqldump'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 curl')
	os.system('pip2 install google')
	os.system('curl -k -O https://gist.githubusercontent.com/Gameye98/76076c9a282a6f32749894d5368024a6/raw/6f9e754f2f81ab2b8efda30603dc8306c65bd651/sqldump.py')
	os.system('mkdir ~/sqldump && chmod +x sqldump.py && mv sqldump.py ~/sqldump')
	print '###### Done'
	backtomenu_option()

def websploit():
	print '\n###### Installing Websploit'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2')
	os.system('pip2 install scapy')
	os.system('git clone https://github.com/The404Hacking/websploit')
	os.system('mv websploit /$HOME')
	print '###### Done'
	backtomenu_option()

def sqlokmed():
	print '\n###### Installing sqlokmed'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('pip2 install urllib2')
	os.system('git clone https://github.com/Anb3rSecID/sqlokmed')
	os.system('mv sqlokmed ~')
	print '###### Done'
	backtomenu_option()

def zones():
	print '\n###### Installing zones'
	os.system("apt update && apt upgrade")
	os.system("apt install git php")
	os.system("git clone https://github.com/Cvar1984/zones")
	os.system("mv zones /$HOME")
	print '######'
	backtomenu_option()

def metasploit():
	print '\n###### Installing Metasploit'
	os.system("apt update && apt upgrade")
	os.system("apt install wget")
	os.system("wget https://Auxilus.github.io/metasploit.sh")
	os.system("mv metasploit.sh /$HOME ~;cd ~;bash metasploit.sh")
	print '###### Done'
	print "###### Type './msfconsole or msfconsole' to start."
	backtomenu_option()

def commix():
	print '\n###### Installing Commix'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/commixproject/commix')
	os.system('mv commix /$HOME')
	print '###### Done'
	backtomenu_option()

def brutal():
	print '\n###### Installing Brutal'
	os.system('apt update && apt upgrade')
	os.system('apt install git')
	os.system('git clone https://github.com/Screetsec/Brutal')
	os.system('mv Brutal /$HOME')
	print '###### Done'
	backtomenu_option()

def a_rat():
	print '\n###### Installing A-Rat'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/Xi4u7/A-Rat')
	os.system('mv A-Rat /$HOME')
	print '###### Done'
	backtomenu_option()

def knockmail():
	print '\n###### Installing KnockMail'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('pip2 install validate_email pyDNS')
	os.system('git clone https://github.com/4w4k3/KnockMail')
	os.system('mv KnockMail /$HOME')
	print '###### Done'
	backtomenu_option()

def spammer_grab():
	print '\n###### Installing Spammer-Grab'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git && pip2 install requests')
	os.system('git clone https://github.com/p4kl0nc4t/spammer-grab')
	os.system('mv spammer-grab /$HOME')
	print '###### Done'
	backtomenu_option()

def hac():
	print '\n###### Installing Hac'
	os.system('apt update && apt upgrade')
	os.system('apt install php git')
	os.system('git clone https://github.com/Cvar1984/Hac')
	os.system('mv Hac /$HOME')
	print '###### Done'
	backtomenu_option()

def spammer_email():
	print '\n###### Installing Spammer-Email'
	os.system("apt update && apt upgrade")
	os.system("apt install git python2 && pip2 install argparse requests")
	os.system("git clone https://github.com/p4kl0nc4t/Spammer-Email")
	os.system("mv Spammer-Email /$HOME")
	print '###### Done'
	backtomenu_option()

def rang3r():
	print '\n###### Installing Rang3r'
	os.system("apt update && apt upgrade")
	os.system("apt install git python2 && pip2 install optparse termcolor")
	os.system("git clone https://github.com/floriankunushevci/rang3r")
	os.system("mv rang3r /$HOME")
	print '###### Done'
	backtomenu_option()

def sh33ll():
	print '\n###### Installing SH33LL'
	os.system("apt update && apt upgrade")
	os.system("apt install git python2")
	os.system("git clone https://github.com/LOoLzeC/SH33LL")
	os.system("mv SH33LL /$HOME")
	print '###### Done'
	backtomenu_option()

def spiderbot():
	print '\n###### Installing SpiderBot'
	os.system("apt update && apt upgrade")
	os.system("apt install git php")
	os.system("git clone https://github.com/Cvar1984/SpiderBot")
	os.system("mv SpiderBot /$HOME")
	print '###### Done'
	backtomenu_option()

def ngrok():
	print '\n###### Installing Ngrok'
	os.system('apt update && apt upgrade')
	os.system('apt install git')
	os.system('git clone https://github.com/themastersunil/ngrok')
	os.system('mv ngrok /$HOME')
	print '###### Done'
	backtomenu_option()

def sudo():
	print '\n###### Installing sudo'
	os.system('apt update && apt upgrade')
	os.system('apt install ncurses-utils git')
	os.system('git clone https://github.com/st42/termux-sudo')
	os.system('mv termux-sudo /$HOME ~ && cd ~/termux-sudo && chmod 777 *')
	os.system('cat sudo > /data/data/com.termux/files/usr/bin/sudo')
	os.system('chmod 700 /data/data/com.termux/files/usr/bin/sudo')
	print '###### Done'
	backtomenu_option()

def ubuntu():
	print '\n###### Installing Ubuntu'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/Neo-Oli/termux-ubuntu')
	os.system('mv termux-ubuntu /$HOME ~ && cd ~/termux-ubuntu && bash ubuntu.sh')
	print '###### Done'
	backtomenu_option()

def fedora():
	print '\n###### Installing Fedora'
	os.system('apt update && apt upgrade')
	os.system('apt install wget git')
	os.system('wget https://raw.githubusercontent.com/nmilosev/termux-fedora/master/termux-fedora.sh')
	os.system('mv termux-fedora.sh /$HOME')
	print '###### Done'
	backtomenu_option()

def nethunter():
	print '\n###### Installing Kali NetHunter'
	os.system('apt update && apt upgrade')
	os.system('apt install git')
	os.system('git clone https://github.com/Hax4us/Nethunter-In-Termux')
	os.system('mv Nethunter-In-Termux /$HOME')
	print '###### Done'
	backtomenu_option()

def blackbox():
	print '\n###### Installing BlackBox'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git && pip2 install optparse passlib')
	os.system('git clone https://github.com/jothatron/blackbox')
	os.system('mv blackbox /$HOME')
	print '###### Done'
	backtomenu_option()

def xattacker():
	print '\n###### Installing XAttacker'
	os.system('apt update && apt upgrade')
	os.system('apt install git perl')
	os.system('cpnm install HTTP::Request')
	os.system('cpnm install LWP::Useragent')
	os.system('git clone https://github.com/Moham3dRiahi/XAttacker')
	os.system('mv XAttacker /$HOME')
	print '###### Done'
	backtomenu_option()

def vcrt():
	print '\n###### Installing VCRT'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/LOoLzeC/Evil-create-framework')
	os.system('mv Evil-create-framework /$HOME')
	print '###### Done'
	backtomenu_option()

def socfish():
	print '\n###### Installing SocialFish'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git && pip2 install wget')
	os.system('git clone https://github.com/UndeadSec/SocialFish')
	os.system('mv SocialFish /$HOME')
	print '###### Done'
	backtomenu_option()

def ecode():
	print '\n###### Installing ECode'
	os.system('apt update && apt upgrade')
	os.system('apt install php git')
	os.system('git clone https://github.com/Cvar1984/Ecode')
	os.system('mv Ecode /$HOME')
	print '###### Done'
	backtomenu_option()

def hashzer():
	print '\n###### Installing Hashzer'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2')
	os.system('pip2 install requests')
	os.system('git clone https://github.com/Anb3rSecID/Hashzer')
	os.system('mv Hashzer ~')
	print '###### Done'
	backtomenu_option()

def xsstrike():
	print '\n###### Installing XSStrike'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2')
	os.system('pip2 install fuzzywuzzy prettytable mechanize HTMLParser')
	os.system('git clone https://github.com/UltimateHackers/XSStrike')
	os.system('mv XSStrike /$HOME')
	print '###### Done'
	backtomenu_option()

def breacher():
	print '\n###### Installing Breacher'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2')
	os.system('pip2 install requests argparse')
	os.system('git clone https://github.com/UltimateHackers/Breacher')
	os.system('mv Breacher ~')
	print '###### Done'
	backtomenu_option()

def stylemux():
	print '\n###### Installing Termux-Styling'
	os.system('apt update && apt upgrade')
	os.system('apt install git')
	os.system('git clone https://github.com/BagazMukti/Termux-Styling-Shell-Script')
	os.system('mv Termux-Styling-Shell-Script /$HOME')
	print '###### Done'
	backtomenu_option()

def txtool():
	print '\n###### Installing TXTool'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2 nmap php curl')
	os.system('pip2 install requests')
	os.system('git clone https://github.com/kuburan/txtool')
	os.system('mv txtool /$HOME')
	print '###### Done'
	backtomenu_option()

def passgencvar():
	print '\n###### Installing PassGen'
	os.system('apt update && apt upgrade')
	os.system('apt install git php')
	os.system('git clone https://github.com/Cvar1984/PassGen')
	os.system('mv PassGen ,/$HOME')
	print '###### Done'
	backtomenu_option()

def sanlen():
	print '\n###### Installing santet-online'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2 && pip2 install requests')
	os.system('git clone https://github.com/Gameye98/santet-online')
	os.system('mv santet-online /$HOME')
	print '###### Done'
	backtomenu_option()

def spazsms():
	print '\n###### Installing SpazSMS'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2 && pip2 install requests')
	os.system('git clone https://github.com/Gameye98/SpazSMS')
	os.system('mv SpazSMS /$HOME')
	print '###### Done'
	backtomenu_option()

def hasher():
	print '\n###### Installing Hasher'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2 && pip2 install passlib binascii progressbar')
	os.system('git clone https://github.com/ciku370/hasher')
	os.system('mv hasher ~')
	print '###### Done'
	backtomenu_option()

def hashgenerator():
	print '\n###### Installing Hash-Generator'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2 && pip2 install passlib progressbar')
	os.system('git clone https://github.com/ciku370/hash-generator')
	os.system('mv hash-generator ~')
	print '###### Done'
	backtomenu_option()

def kodork():
	print '\n###### Installing ko-dork'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2 && pip2 install urllib2')
	os.system('git clone https://github.com/ciku370/ko-dork')
	os.system('mv ko-dork ~')
	print '###### Done'
	backtomenu_option()

def snitch():
	print '\n###### Installing snitch'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2')
	os.system('git clone https://github.com/Smaash/snitch')
	os.system('mv snitch ~')
	print '###### Done'
	backtomenu_option()

def osif():
	print '\n###### Installing OSIF'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2')
	os.system('pip2 install requests')
	os.system('git clone https://github.com/ciku370/OSIF')
	os.system('mv OSIF ~')
	print '###### Done'
	backtomenu_option()

def smfb():
        print '\n###### Installing Facebook_Bruteforce'
        os.system('apt update && apt upgrade')
        os.system('apt install git python2')
        os.system('git clone https://github.com/saintmalik/SMfbcrack')
        os.system('mv SMfbcrack /$HOME')
        print '###### Done'
        backtomenu_option()
def optiva():
        print '\n###### Installing Optiva_Framework'
        os.system('apt update && apt upgrade')
        os.system('apt install git python2')
        os.system('git clone https://github.com/joker25000/Optiva-Framework')
        os.system('mv Optiva-Framework /$HOME')
        print '###### Done'
        backtomenu_option()

def lite():
        print '\n###### Installing LITEOTP'
        os.system('apt update && apt upgrade')
        os.system('apt install git php')
        os.system('git clone https://github.com/Cvar1984/LiteOTP')
        os.system('mv LiteOTP /$HOME')
        print '###### Done'
        backtomenu_option()

def zoom():
        print '\n###### Installing ZOOM'
        os.system('apt update && apt upgrade')
        os.system('apt install git python2')
        os.system('git clone https://github.com/UltimateLabs/Zoom')
        os.system('mv Zoom /$HOME')
        print '###### Done'
        backtomenu_option()

def infinit():
        print '\n###### Installing Infinity'
        os.system('apt update && apt upgrade')
        os.system('apt install git python2')
        os.system('https://github.com/saintmalik/infini-ty')
        os.system('mv infini-ty /$HOME')
        print '###### Done'
        backtomenu_option()

def cook():
        print '\n###### Installing Cookie-Stealer'
        os.system('apt update && apt upgrade')
        os.system('apt install git php')
        os.system('https://github.com/Xyl2k/Cookie-stealer')
        os.system('mv Cookie-stealer /$HOME')
        print '###### Done'
        backtomenu_option()

def cloak():
        print '\n###### Installing Cloak'
        os.system('apt update && apt upgrade')
        os.system('apt install git python2')
        os.system('git clone https://github.com/s0md3v/Cloak')
        os.system('mv Cloak /$HOME')
        print '###### Done'
        backtomenu_option()

def rat():
        print '\n###### Installing Rat-Hunter'
        os.system('apt update && apt upgrade')
        os.system('apt install git php')
        os.system('git clone https://github.com/Rizee0/Rat-Hunter.git')
        os.system('mv -v Rat-Hunter /$HOME')
        print '###### Done'
        backtomenu_option()

def blazy():
        print '\n###### Installing Blazy'
        os.system('apt update && apt upgrade')
        os.system('apt install git python2')
        os.system('pip install -r requirements.txt')
        os.system('git clone https://github.com/s0md3v/Blazy')
        os.system('mv Blazy /$HOME ~')
        print '###### Done'
        backtomenu_option()

def locky():
        print '\n###### Installing Locky'
        os.system('apt update && apt upgrade')
        os.system('apt install git python')
        os.system('git clone https://github.com/s0md3v/Locky')
        os.system('mv Locky /$HOME')
        print '###### Done'
        backtomenu_option()


def admin():
        print '\n###### Installing Admin-Panel-Finder'
        os.system('apt update && apt upgrade')
        os.system('apt install git python2')
        os.system('git clone https://github.com/bdblackhat/admin-panel-finder')
        os.system('mv admin-panel-finder /$HOME')
        print '###### Done'
        backtomenu_option()

def inurl():
        print '\n###### Installing SCANNER_INURLBR'
        os.system('apt update && apt upgrade')
        os.system('apt install git python2')
        os.system('git clone https://github.com/googleinurl/SCANNER-INURLBR')
        os.system('mv SCANNER-INURLBR /$HOME')
        print '###### Done'
        backtomenu_option()

def shodan():
        print '\n###### Installing SHODANHAT'
        os.system('apt update && apt upgrade')
        os.system('apt install git python')
        os.system('git clone https://github.com/HatBashBR/ShodanHat')
        os.system('mv ShodanHat /$HOME')
        print '###### Done'
        backtomenu_option()

def hatcloud():
        print '\n###### Installing HatCloud'
        os.system('apt update && apt upgrade')
        os.system('apt install git ruby')
        os.system('pip2 install requests')
        os.system('git clone https://github.com/HatBashBR/HatCloud')
        os.system('mv HatCloud /$HOME')
        print '###### Done'
        backtomenu_option()

def droid():
        print '\n###### Installing Droid-Hunter'
        os.system('apt update && apt upgrade')
        os.system('apt install git ruby')
        os.system('git clone https://github.com/hahwul/droid-hunter')
        os.system('mv droid-hunter /$HOME')
        print '###### Done'
        backtomenu_option()

def smbrute():
        print '\n###### Installing SMEmailBrute'
        os.system('apt update && apt upgrade')
        os.system('apt install git python2')
        os.system('git clone https://github.com/saintmalik/SMEmailBrute')
        os.system('mv SMEmailBrute /$HOME')
        print '###### Done'
        backtomenu_option()

def fat():
        print '\n###### Installing TheFatRat'
        os.system('apt update && apt upgrade')
        os.system('apt install git 2')
        os.system('git clone https://github.com/Screetsec/TheFatRat.git')
        os.system('mv TheFatRat /$HOME')
        print '###### Done'
        backtomenu_option()

def info():
        print '\n###### Installing InfoSploit'
        os.system('apt update && apt upgrade')
        os.system('apt install git ')
        os.system('git clone https://github.com/CybernetiX-S3C/InfoSploit')
        os.system('mv InfoSploit /$HOME')
        print '###### Done'
        backtomenu_option()

def get():
        print '\n###### Installing getdroid'
        os.system('apt update && apt upgrade')
        os.system('apt install git ')
        os.system('git clone https://github.com/thelinuxchoice/getdroid')
        os.system('mv getdroid /$HOME')
        print '###### Done'
        backtomenu_option()

def shell():
        print '\n###### Installing ShellPhish'
        os.system('apt update && apt upgrade')
        os.system('apt install git ')
        os.system('git clone https://github.com/thelinuxchoice/shellphish')
        os.system('mv shellphish /$HOME')
        print '###### Done'
        backtomenu_option()

def blk():
        print '\n###### Installing BlackEye'
        os.system('apt update && apt upgrade')
        os.system('apt install git ')
        os.system('git clone https://github.com/thelinuxchoice/blackeye')
        os.system('mv blackeye /$HOME')
        print '###### Done'
        backtomenu_option()

def ohm():
        print '\n###### Installing OhMyQr'
        os.system('apt update && apt upgrade')
        os.system('apt install git ')
        os.system('git clone https://github.com/thelinuxchoice/ohmyqr')
        os.system('mv ohmyqr /$HOME')
        print '###### Done'
        backtomenu_option()

def lct():
        print '\n###### Installing Locator'
        os.system('apt update && apt upgrade')
        os.system('apt install git ')
        os.system('git clone https://github.com/thelinuxchoice/locator')
        os.system('mv locator /$HOME')
        print '###### Done'
        backtomenu_option()

def fap():
        print '\n###### Installing FakeAp'
        os.system('apt update && apt upgrade')
        os.system('apt install git ')
        os.system('git clone https://github.com/thelinuxchoice/fakeap')
        os.system('mv fakeap /$HOME')
        print '###### Done'
        backtomenu_option()

def fab():
        print '\n###### Installing FaceBash'
        os.system('apt update && apt upgrade')
        os.system('apt install git ')
        os.system('git clone https://github.com/thelinuxchoice/facebash')
        os.system('mv facebash /$HOME')
        print '###### Done'
        backtomenu_option()

def dot():
        print '\n###### Installing Ddostor'
        os.system('apt update && apt upgrade')
        os.system('apt install git ')
        os.system('git clone https://github.com/thelinuxchoice/ddostor')
        os.system('mv ddostor /$HOME')
        print '###### Done'
        backtomenu_option()

def gew():
        print '\n###### Installing GetWin'
        os.system('apt update && apt upgrade')
        os.system('apt install git ')
        os.system('git clone https://github.com/thelinuxchoice/getwin')
        os.system('mv getwin /$HOME')
        print '###### Done'
        backtomenu_option()

def cmsb():
        print '\n###### Installing BruteCms'
        os.system('apt update && apt upgrade')
        os.system('apt install git ')
        os.system('git clone https://github.com/thelinuxchoice/brutecms')
        os.system('mv brutecms /$HOME')
        print '###### Done'
        backtomenu_option()

def sant():
        print '\n###### Installing InstaInsane'
        os.system('apt update && apt upgrade')
        os.system('apt install git ')
        os.system('git clone https://github.com/thelinuxchoice/instainsane')
        os.system('mv instainsane /$HOME')
        print '###### Done'
        backtomenu_option()

def sht():
        print '\n###### Installing InstaShell'
        os.system('apt update && apt upgrade')
        os.system('apt install git ')
        os.system('git clone https://github.com/thelinuxchoice/instashell')
        os.system('mv instashell /$HOME')
        print '###### Done'
        backtomenu_option()

def chb():
        print '\n###### Installing ChoiceBot'
        os.system('apt update && apt upgrade')
        os.system('apt install git ')
        os.system('git clone https://github.com/thelinuxchoice/choicebot')
        os.system('mv choicebot /$HOME')
        print '###### Done'
        backtomenu_option()

def tch():
        print '\n###### Installing Thechoice'
        os.system('apt update && apt upgrade')
        os.system('apt install git ')
        os.system('git clone https://github.com/thelinuxchoice/thechoice')
        os.system('mv thechoice /$HOME')
        print '###### Done'
        backtomenu_option()


def fsh():
        print '\n###### Installing FastSsh'
        os.system('apt update && apt upgrade')
        os.system('apt install git ')
        os.system('git clone https://github.com/thelinuxchoice/fastssh')
        os.system('mv fastssh /$HOME')
        print '###### Done'
        backtomenu_option()

def vnm():
        print '\n###### Installing Venomgen'
        os.system('apt update && apt upgrade')
        os.system('apt install git ')
        os.system('git clone https://github.com/thelinuxchoice/venomgen')
        os.system('mv venomgen /$HOME')
        print '###### Done'
        backtomenu_option()

def sqsc():
        print '\n###### Installing SqliScanner'
        os.system('apt update && apt upgrade')
        os.system('apt install git ')
        os.system('git clone https://github.com/thelinuxchoice/sqliscan')
        os.system('mv sqliscan /$HOME')
        print '###### Done'
        backtomenu_option()

def getip():
        print '\n###### Installing GetIp'
        os.system('apt update && apt upgrade')
        os.system('apt install git ')
        os.system('git clone https://github.com/thelinuxchoice/getip')
        os.system('mv getip /$HOME')
        print '###### Done'
        backtomenu_option()

def duck():
        print '\n###### Installing Duckshell'
        os.system('apt update && apt upgrade')
        os.system('apt install git ')
        os.system('git clone https://github.com/thelinuxchoice/duckshell')
        os.system('mv duckshell /$HOME')
        print '###### Done'
        backtomenu_option()

def wlc():
        print '\n###### Installing Wlcreator'
        os.system('apt update && apt upgrade')
        os.system('apt install git ')
        os.system('git clone https://github.com/thelinuxchoice/wlcreator')
        os.system('mv wlcreator /$HOME')
        print '###### Done'
        backtomenu_option()

def mut():
        print '\n###### Installing MultiTor'
        os.system('apt update && apt upgrade')
        os.system('apt install git ')
        os.system('git clone https://github.com/thelinuxchoice/multitor')
        os.system('mv multitor /$HOME')
        print '###### Done'
        backtomenu_option()

def fog():
        print '\n###### Installing Infog'
        os.system('apt update && apt upgrade')
        os.system('apt install git ')
        os.system('git clone https://github.com/thelinuxchoice/infog')
        os.system('mv infog /$HOME')
        print '###### Done'
        backtomenu_option()

def httpb():
        print '\n###### Installing BruteHttp'
        os.system('apt update && apt upgrade')
        os.system('apt install git ')
        os.system('git clone https://github.com/thelinuxchoice/brutehttp')
        os.system('mv brutehttp /$HOME')
        print '###### Done'
        backtomenu_option()

def rot():
        print '\n###### Installing TorAttack'
        os.system('apt update && apt upgrade')
        os.system('apt install git ')
        os.system('git clone https://github.com/thelinuxchoice/torattack')
        os.system('mv torattack /$HOME')
        print '###### Done'
        backtomenu_option()

def tweet():
        print '\n###### Installing Tweetshell'
        os.system('apt update && apt upgrade')
        os.system('apt install git ')
        os.system('git clone https://github.com/thelinuxchoice/tweetshell')
        os.system('mv tweetshell /$HOME')
        print '###### Done'
        backtomenu_option()

def ybot():
        print '\n###### Installing YouBot'
        os.system('apt update && apt upgrade')
        os.system('apt install git ')
        os.system('git clone https://github.com/thelinuxchoice/youbot')
        os.system('mv youbot /$HOME')
        print '###### Done'
        backtomenu_option()

def sbot():
        print '\n###### Installing BotSql'
        os.system('apt update && apt upgrade')
        os.system('apt install git ')
        os.system('git clone https://github.com/thelinuxchoice/botsql')
        os.system('mv BotSql /$HOME')
        print '###### Done'
        backtomenu_option()

def debtool():
        print '\n###### Installing Debiantool'
        os.system('apt update && apt upgrade')
        os.system('apt install git ')
        os.system('git clone https://github.com/thelinuxchoice/debiantools')
        os.system('mv debiantools /$HOME')
        print '###### Done'
        backtomenu_option()

def switor():
        print '\n###### Installing Switchtor'
        os.system('apt update && apt upgrade')
        os.system('apt install git')
        os.system('git clone https://github.com/thelinuxchoice/switchtor')
        os.system('mv switchtor /$HOME')
        print '###### Done'
        backtomenu_option()

def netsp():
        print '\n###### Installing Netscanp'
        os.system('apt update && apt upgrade')
        os.system('apt install git ')
        os.system('git clone https://github.com/thelinuxchoice/netscanp')
        os.system('mv netscanp /$HOME')
        print '###### Done'
        backtomenu_option()

def instapost():
        print '\n###### Installing InstaPost'
        os.system('apt update && apt upgrade')
        os.system('apt install git ')
        os.system('git clone https://github.com/thelinuxchoice/instapost')
        os.system('mv instapost /$HOME')
        print '###### Done'
        backtomenu_option()

def antiflood():
        print '\n###### Installing Antiflood'
        os.system('apt update && apt upgrade')
        os.system('apt install git ')
        os.system('git clone https://github.com/thelinuxchoice/antiflood')
        os.system('mv antiflood /$HOME')
        print '###### Done'
        backtomenu_option()


def blckt():
        print '\n###### Installing Blocktor'
        os.system('apt update && apt upgrade')
        os.system('apt install git ')
        os.system('git clone https://github.com/thelinuxchoice/blocktor')
        os.system('mv blocktor /$HOME')
        print '###### Done'
        backtomenu_option()

def hckw():
        print '\n###### Installing Hackwin'
        os.system('apt update && apt upgrade')
        os.system('apt install git ')
        os.system('git clone https://github.com/thelinuxchoice/hackwin')
        os.system('mv hackwin /$HOME')
        print '###### Done'
        backtomenu_option()

def sshs():
        print '\n###### Installing ShhScan'
        os.system('apt update && apt upgrade')
        os.system('apt install git ')
        os.system('git clone https://github.com/thelinuxchoice/sshscan')
        os.system('mv sshscan /$HOME')
        print '###### Done'
        backtomenu_option()

def synf():
        print '\n###### Installing SynFlood'
        os.system('apt update && apt upgrade')
        os.system('apt install git ')
        os.system('git clone https://github.com/thelinuxchoice/synflood')
        os.system('mv InfoSploit /$HOME')
        print '###### Done'
        backtomenu_option()

def telscan():
        print '\n###### Installing TelnetScan'
        os.system('apt update && apt upgrade')
        os.system('apt install git ')
        os.system('git clone https://github.com/thelinuxchoice/telnetscan')
        os.system('mv telnetscan /$HOME')
        print '###### Done'
        backtomenu_option()

def reset():
        print '\n###### Installing Termux-Reset'
        os.system('apt update && apt upgrade')
        os.system('apt install git ')
        os.system('git clone https://github.com/saintmalik/termux-reset')
        os.system('mv termux-reset /$HOME')
        print '###### Done'
        backtomenu_option()

def pydos():
        print '\n###### Installing PyDdos'
        os.system('apt update && apt upgrade')
        os.system('apt install git ')
        os.system('git clone https://github.com/saintmalik/Pydos')
        os.system('mv Pydos /$HOME')
        print '###### Done'
        backtomenu_option()

def cljt():
        print '\n###### Installing Clickjacking-Tester'
        os.system('apt update && apt upgrade')
        os.system('apt install git ')
        os.system('git clone https://github.com/D4Vinci/Clickjacking-Tester')
        os.system('mv Clickjacking-Tester /$HOME')
        print '###### Done'
        backtomenu_option()

def xnmap():
        print '\n###### Installing Xnmap'
        os.system('apt update && apt upgrade')
        os.system('apt install git ')
        os.system('git clone https://github.com/Ranginang67/Xnmap')
        os.system('mv Xnmap /$HOME')
        print '###### Done'
        backtomenu_option()

def flux():
        print '\n###### Installing Fluxion'
        os.system('apt update && apt upgrade')
        os.system('apt install git ')
        os.system('git clone https://github.com/thehackingsage/Fluxion')
        os.system('mv Fluxion /$HOME')
        print '###### Done'
        backtomenu_option()

def hasherdotid():
        print '\n###### Installing Hasherdotid'
        os.system('apt update && apt upgrade')
        os.system('apt install python2 git')
        os.system('git clone https://github.com/galauerscrew/hasherdotid')
        os.system('mv hasherdotid ~')
        print '###### Done'
        backtomenu_option()

def namechk():
        print '\n###### Installing Namechk'
        os.system('apt update && apt upgrade')
        os.system('apt install git')
        os.system('git clone https://github.com/HA71/Namechk')
        os.system('mv Namechk ~')
        print '###### Done'
        backtomenu_option()

def xlPy():
        print '\n###### Installing xl-py'
        os.system('apt update && apt upgrade')
        os.system('apt install python git')
        os.system('git clone https://github.com/albertoanggi/xl-py')
        os.system('mv xl-py ~')
        print '###### Done'
        backtomenu_option()

def beanshell():
        print '\n###### Installing Beanshell'
        os.system('apt update && apt upgrade')
        os.system('apt install dpkg wget')
        os.system('wget https://github.com/amsitlab/amsitlab.github.io/blob/master/dists/termux/amsitlab/binary-all/beanshell_2.04_all.deb')
        os.system('dpkg -i beanshell_2.04_all.deb')
        os.system('rm beanshell_2.04_all.deb')
        print '###### Done'
        print "###### Type 'bsh' to start."
        backtomenu_option()

def msfpg():
        print '\n###### Installing MSF-Pg'
        os.system('apt update && apt upgrade')
        os.system('apt install git')
        os.system('git clone https://github.com/haxzsadik/MSF-Pg')
        os.system('mv MSF-Pg ~')
        print "###### Done"
        backtomenu_option()

def lolrat():
        print '\n###### Installing Lolz_RAT'
        os.system('apt update && apt upgrade')
        os.system('apt install wget ')
        os.system('wget https://github.com/mrcakil/Lolz_RAT/blob/master/Lolz_RAT')
        os.system('mv Lolz_RAT /$HOME')
        print '###### Done'
        backtomenu_option()

def crewbot():
        print '\n###### Installing Crewbot'
        os.system('apt update && apt upgrade')
        os.system('apt install git ')
        os.system('git clone https://github.com/marklarr/crewbot')
        os.system('mv crewbot /$HOME')
        print '###### Done'
        backtomenu_option()

def greap():
        print '\n###### Installing green-Reaper'
        os.system('apt update && apt upgrade')
        os.system('apt install git ')
        os.system('git clone https://github.com/Amriez/GreenReaper')
        os.system('mv GreenReaper /$HOME')
        print '###### Done'
        backtomenu_option()

def ipu():
        print '\n###### Installing Ipmux'
        os.system('apt update && apt upgrade')
        os.system('apt install git ')
        os.system('git clone https://github.com/Amriez/ipmux')
        os.system('mv ipmux /$HOME')
        print '###### Done'
        backtomenu_option()
def tapi():
        print '\n###### Installing termux-api'
        os.system('apt update && apt upgrade')
        os.system('apt install git ')
        os.system('git clone https://github.com/Amriez/termux-api')
        os.system('mv termux-api /$HOME')
        print '###### Done'
        backtomenu_option()

def mspam():
        print '\n###### Installing MultiSpam'
        os.system('apt update && apt upgrade')
        os.system('apt install git ')
        os.system('git clone https://github.com/tdencker/multi-SpaM')
        os.system('mv multi-SpaM /$HOME')
        print '###### Done'
        backtomenu_option()

def jmscan():
        print '\n###### Installing Joomscan'
        os.system('apt update && apt upgrade')
        os.system('apt install git ')
        os.system('git clone https://github.com/rezasp/joomscan')
        os.system('mv joomscan /$HOME')
        print '###### Done'
        backtomenu_option()

def touchurl():
        print '\n###### Installing TouchURL'
        os.system('apt update && apt upgrade')
        os.system('apt install python git && pip install parse colorama')
        os.system('git clone https://github.com/SkyKnight-Team/TouchUrl')
        os.system('mv TouchUrl ~')
        print "###### Done"
        backtomenu_option()

def webconn():
        print '\n###### Installing WebConn'
        os.system('apt update && apt upgrade')
        os.system('apt install python git')
        os.system('git clone https://github.com/SkyKnight-Team/WebConn')
        os.system('mv WebConn ~')
        print "###### Done"
        backtomenu_option()

def binploit():
        print '\n###### Installing Binary Exploitation'
        os.system('apt update && apt upgrade')
        os.system('apt install gdb radare2 ired ddrescue bin-utils yasm strace ltrace cdb hexcurse memcached llvmdb')
        print "###### Done"
        print "###### Tutorial: https://youtu.be/3NTXFUxcKPc"
        backtomenu_option()

def apache():
        print '\n###### Installing Apache2'
        os.system('apt update && apt upgrade')
        os.system('apt install apache2')
        print "###### Done"
        backtomenu_option()

def fileloc():
        print '\n###### Installing File Locker'
        os.system('apt update && apt upgrade')
        os.system('apt install gnupg')
        print "###### Done"
        backtomenu_option()

def openssh():
        print '\n###### Installing SSH'
        os.system('apt update && apt upgrade')
        os.system('pkg install openssh')
        print "###### Done"
        backtomenu_option()

def fsh():
        print '\n###### Installing FISH'
        os.system('apt update && apt upgrade')
        os.system('pkg install fish')
        print "###### Done"
        backtomenu_option()

def httrack():
        print '\n###### Installing Httrack'
        os.system('apt update && apt upgrade')
        os.system('pkg install fish')
        os.system('curl -LO https://raw.githubusercontent.com/Hax4us/httrack_In_termux/master/httrack')
        os.system('sh httrack')
        print "###### Done"
        backtomenu_option()
