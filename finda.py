#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import cfscrape #against cloudflare
import sys
from threading import Thread
import os
import time

os.system('clear')

numline = 1
isproxy = {"http":"0",
"https":"0",
}

def helpmenu():
	print('''

 mmmmmmmm   mmmmmm   mmm   mm  mmmmm        mm
 ##""""""   ""##""   ###   ##  ##"""##     ####
 ##           ##     ##"#  ##  ##    ##    ####
 #######      ##     ## ## ##  ##    ##   ##  ##
 ##           ##     ##  #m##  ##    ##   ######
 ##         mm##mm   ##   ###  ##mmm##   m##  ##m
 ""         """"""   ""   """  """""     ""    ""

                                      	by https://github.com/blesswood
''')
	print("This is the active scanning, which may be forbidden in your country, please, use it to scan only your own server(s)\n")
	print("Usage:")
	print("finda.py -h[elp] -> this help")
	print("finda.py -w[izard] -> wizard mode")
	print("finda.py URL [-s][ilent] [-f][ast] [-p][roxy] [ip:port] [-l] [custom_wordlist]-> scan options\n")
	print("I want your feedback here:\n     Telegram: @kennnies \n     Jabber: explo1t@xmpp.jp\n")
	print("Thanks!")
	sys.exit()

try:
	sitename = sys.argv[1]
except IndexError:
	helpmenu() #if no arguments given

ifresult = False #sys.exit() if found result(if True)

file = open('/usr/local/bin/findadb.py')

class th(Thread):
	def __init__(self, Val, num, timeleft):
		Thread.__init__(self)
		self.Val = Val
		self.num = num
		self.timeleft = timeleft
	
	def run(self):
		try:
			if self.Val==True:
				ifsilent(self.num)
			else:
				checktime(self.timeleft)
		except KeyboardInterrupt:
			time.sleep(1)
			sys.exit()
		
def checktime(timeleft):
	numpop = 450 #number of popular admin pages in db
	if(numpop-countline<=0):
		numpop = 7339 #if first 450 pages isn't available
	sys.stdout.flush()
	res = '\r			time left: %s s' % round((time.time()-timeleft)*(numpop-countline)) #write time left
	time.sleep(0.6)
	sys.stdout.write(res)
	

def ifsilent(num): #scrollbar
	sys.stdout.flush()
	res = '\r%i/max' % num # num of string in wordlist
	sys.stdout.write(res)

countline = 0

def getpage(file, sitename, header, timestart): #active scan
	page = file.readline()
	global countline
	countline += 1
	if not page: #if file isn't readable
		sys.exit()
	global ifresult
	siteresult = sitename + '/' + page #configure page address
	if (isproxy["http"]!="0"):
		try:
			scraper = cfscrape.create_scraper()
			response = scraper.get(siteresult[:-1], headers=header, proxies=isproxy)
		except ConnectionResetError:
			print("Cannot connect to proxy ", isproxy["http"])
			sys.exit()
		except TimeoutError:
			print("Cannot connect to proxy ", isproxy["http"])
			sys.exit()
	else:
		scraper = cfscrape.create_scraper()
		response = scraper.get(siteresult[:-1], headers=header)
	if not response:
		global numline
		if(ifresult==False):
			
			if con == False:
				dat = response.url + ' is wrong!' #check all links(idk who wants to see it...)
				print(dat)
				
			else:
				numline+=1
				th(True, numline, 0).start()#number of current line in silent mode	
	else:
		print()
		dat = str(response.url) + ' IS OK'
		print(dat)
		timespent = 'Time spent: ' + str(round(time.time()-timestart)) + 's\n'
		sys.stdout.write(timespent)
		sys.stdout.flush()
		ifresult = True

con = False #if silent mode is enabled, become True
isfast = False #if fast mode is enabled, become True
ifcustom = False

def mode(): #check for mode
	for i in range(1,7):
		try:
			if ('-s' in sys.argv[i]): # check for '-s' option (silentmode)
				global con
				con = True
			elif('-p' in sys.argv[i]): # check for '-p' option (proxy)
				global isproxy
				isproxy["http"] = "http://" + str(sys.argv[i+1]) #write proxy(next option after '-p') to isproxy
				isproxy["https"] = "https://" + str(sys.argv[i+1])
			elif('-f' in sys.argv[i]): #check for '-f' option (fastmode)
				global isfast
				isfast = True
			elif('-l' in sys.argv[i]): #check for '-l' option (custom wordlist)
				global file
				file = open(sys.argv[i+1])
				global ifcustom
				ifcustom = True
		except IndexError: # if no options given
			pass

sitename = str(sitename)
header = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'}

def start():
	global sitename
	if not 'http' in sitename:
		sitename = 'http://' + sitename
	if '-w' in sitename:
		pass #escape mode checking for wizard
	else:
		mode() #check options
	with file as f:
		if(isfast==True):
			timestart = time.time() #started time for counting timespent
			while True: #start scanning
				try: #check for fast mode and create 5 threads if so
					timeleft = time.time() #timeleft start
					th1 = Thread(target=getpage, args=(f,sitename,header,timestart))
					th1.start() #start thread with 4 args
					time.sleep(0.1)

					if con == True and ifcustom == False:
						th(False, numline, timeleft).start() #timeleft stop and count

					th2 = Thread(target=getpage, args=(f,sitename,header,timestart))
					th2.start()
					time.sleep(0.1)

					th3 = Thread(target=getpage, args=(f,sitename,header,timestart))
					th3.start()
					time.sleep(0.1)

					th4 = Thread(target=getpage, args=(f,sitename,header,timestart))
					th4.start()
					time.sleep(0.1)

					th5 = Thread(target=getpage, args=(f,sitename,header,timestart))
					th5.start()
					time.sleep(0.1)

					if (ifresult==True and ifcustom==False):
						break
						sys.exit() #exit code
				except KeyboardInterrupt: #in case of cancelling work by user
					for i in range(4):
						sys.stdout.flush()
					time.sleep(1)
					sys.stdout.write('\n')
					sys.stdout.flush()
					sys.exit()

		else: #else start 1 thread
			timestart = time.time()
			while True:
				try:
					timeleft = time.time() #timeleft start
					th1 = Thread(target=getpage, args=(f,sitename,header,timestart))
					th1.start() #start thread with 4 args
					time.sleep(0.1)

					if con == True and ifcustom == False:
						th(False, numline, timeleft).start() #timeleft stop and count
						time.sleep(0.1)

					if(ifresult==True and ifcustom==False):
						time.sleep(1)
						sys.exit()
						break

				except KeyboardInterrupt: #in case of cancelling work
					sys.stdout.flush()
					time.sleep(1)
					sys.stdout.write('\n')
					sys.stdout.flush()
					sys.exit()
			if ifresult==True and ifcustom==False: #if success
				sys.exit()
		file.close()

def startWizard():
	print('''

 mmmmmmmm   mmmmmm   mmm   mm  mmmmm        mm
 ##""""""   ""##""   ###   ##  ##"""##     ####
 ##           ##     ##"#  ##  ##    ##    ####
 #######      ##     ## ## ##  ##    ##   ##  ##
 ##           ##     ##  #m##  ##    ##   ######
 ##         mm##mm   ##   ###  ##mmm##   m##  ##m
 ""         """"""   ""   """  """""     ""    ""

                                      	by https://github.com/blesswood
''')
	print("\nThis is the active scanning, which may be forbidden in your country, please, use it to scan only your own server(s)\n")
	print("Enter site URL:", end = " ")
	global sitename
	try:
		sitename = input() #enter link
		print("Do you want fast scan?(y/N):", end = " ")
		if 'y' in input().lower(): #if user enabled fastmode
			global isfast
			isfast = True
		print("Do you want silent mode?(Y/n):", end = " ")
		if 'y' in input().lower(): #if user enabled silentmode
			global con
			con = True
		print("Do you want to use proxy(http(s))?(Y/n):", end = " ")
		if 'y' in input().lower(): #if user want to use proxy
			print('Enter proxy(ip:port)', end = " ")
			proxy = input()
			isproxy["http"] = "http://" + str(proxy) #write inputed proxy to isproxy
			isproxy["https"] = "https://" + str(proxy)
		print("Use custom wordlist?:(y/N)", end = " ")
		if ('y') in input().lower():
			global file
			file = open(input('Enter custom wordlist: '))
		
	except KeyboardInterrupt:
		print()
		sys.exit()
	start()

if "-h" in sitename:
	helpmenu() #show help menu
elif "-w" in sitename: #enable wizard
	startWizard()
else:
	start()
