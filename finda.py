#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import requests
import sys
from threading import Thread
import os
import time

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
	print("finda.py URL [-s][ilent] [-f][ast] [-p][roxy] [ip:port] -> scan options\n")
	print("I want your feedback here:\n     Telegram: @kennnies \n     Jabber: explo1t@xmpp.jp")
	print("\nThanks!")
	sys.exit()

sitename=''
try:
	sitename = sys.argv[1]
except IndexError:
	helpmenu()

t = False #sys.exit() if found result(if True)

def ifsilent(num): #scrollbar
	res = '\r%i/7339' % num #7339 - num of string in findadb
	sys.stdout.flush()
	sys.stdout.write(res)

def getpage(file, sitename, header): #main func(active scan)
	page = file.readline()
	if not page: #if file isn't readable
		print("Sorry, i couldn't read line from file findadb.py")
		sys.exit()
	global t
	siteresult = sitename + '/' + page #get page address
	if (isproxy["http"]!="0"):
		try:
			response = requests.get(siteresult[:-1], headers=header, proxies=isproxy)
		except ConnectionResetError:
			print("Cannot connect to proxy ", isproxy["http"])
			sys.exit()
		except TimeoutError:
			print("Cannot connect to proxy ", isproxy["http"])
			sys.exit()
	else:
		response = requests.get(siteresult[:-1], headers=header)
	if not response:
		if(t==False):
			dat = response.url + ' is wrong!' #check all links(idk who wants to see it...)
			if con == False:
				print(dat)
			else:
				global numline
				ifsilent(numline)#number of current line in silent mode
				numline+=1
	else:
		print()
		dat = str(response.url) + ' IS OK'
		print(dat)
		t = True

con = False
isfast = False

def mode(): #check for silent mode
	for i in range(2,5):
		try:
			if ('-s' in sys.argv[i]):
				global con
				con = True
			elif('-p' in sys.argv[i]):
				global isproxy
				isproxy["http"] = "http://" + str(sys.argv[i+1])
				isproxy["https"] = "https://" + str(sys.argv[i+1])
			elif('-f' in sys.argv[i]):
				global isfast
				isfast = True
		except IndexError:
			pass

sitename = str(sitename)
header = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'}

def start():
	global sitename
	sitename = 'http://' + sitename
	file = open('/usr/local/bin/findadb.py')
	if '-w' in sitename:
		pass
	else:
		mode()
	with file as f:
		if(isfast==True):
			while True: #start scanning
				try: #check for fast mode and create 5 threads if so
					th1 = Thread(target=getpage, args=(file,sitename,header,))
					th1.start()
					time.sleep(0.05)

					th2 = Thread(target=getpage, args=(file,sitename,header,))
					th2.start()
					time.sleep(0.05)

					th3 = Thread(target=getpage, args=(file,sitename,header,))
					th3.start()
					time.sleep(0.05)

					th4 = Thread(target=getpage, args=(file,sitename,header,))
					th4.start()
					time.sleep(0.05)

					th5 = Thread(target=getpage, args=(file,sitename,header,))
					th5.start()
					time.sleep(0.05)

					th1.join()
					th2.join()
					th3.join()
					th4.join()
					th5.join()
					if (t==True):
						sys.exit()
				except KeyboardInterrupt: #in case of cancelling program
					for i in range(4):
						sys.stdout.flush()
					time.sleep(1)
					sys.stdout.write('\n')
					sys.stdout.flush()
					sys.exit()
		else: #else start 1 thread
			while True:
				try:
					th1 = Thread(target=getpage, args=(file,sitename,header,))
					th1.start()
					th1.join()
					if(t==True):
						sys.exit()
				except KeyboardInterrupt: #in case of cancelling program
					sys.stdout.flush()
					time.sleep(1)
					sys.stdout.write('\n')
					sys.stdout.flush()
					sys.exit()
			if t==True: #if success
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
		sitename = input()
		print("Do you want fast scan?(y/N):", end = " ")
		if 'y' in input():
			global isfast
			isfast = True
			print("Do you want silent mode?(Y/n):", end = " ")
			if 'y' in input():
				global con
			con = True
			print("Do you want to use proxy?(Y/n):", end = " ")
		if 'y' in input():
			print('Enter proxy(ip:port)', end = " ")
			proxy = input()
			isproxy["http"] = "http://" + str(proxy)
			isproxy["https"] = "https://" + str(proxy)
	except KeyboardInterrupt:
		print()
		sys.exit()
	start()

if "-h" in sitename:
	helpmenu() #show help menu
elif "-w" in sitename:
	startWizard()
else:
	start()
