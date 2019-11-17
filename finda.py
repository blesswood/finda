#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import requests
import sys
from threading import Thread
import os

numline = 1

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
	print('finda.py -h[elp] -> this help')
	print("finda.py URL [-s][ilent] [-f][ast] -> start scan")
	print("\nI strongly recommend to use silent mode with '-f' option, because without it after successfull result may appear some extra wrong strings\n")
	print("I want your feedback here:\n     Telegram: @kennnies \n     Jabber: explo1t@xmpp.jp")
	print("\nThanks!")
	sys.exit()

sitename=''
try:
	sitename = sys.argv[1]
except IndexError:
	helpmenu()

option = ''
try:
	option = sys.argv[2]
except IndexError:
	pass

fast = ''
try:
	fast = sys.argv[3]
except IndexError:
	pass

t = False #sys.exit() if found result

def ifsilent(num): #scrollbar
    res = '\r%i/7339' % num
    sys.stdout.write(res)
    sys.stdout.flush()

def getpage(file, sitename, header): #main func(active scan)
	page = file.readline()
	if not page: #if file isn't readable
		print("Sorry, i couldn't read line from file findadb.py")
		sys.exit()
	siteresult = sitename + '/' + page #get page addres
	response = requests.get(siteresult[:-1], headers=header)
	if not response:
		dat = response.url + ' is wrong!' #check all links(idk who wants it...)
		if con == False:
			print(dat)
		else:
			global numline
			ifsilent(numline)#count number of current line in silent mode
			numline+=1
	else:
		print()
		dat = str(response.url) + ' IS OK'
		print(dat)
		global t
		t = True

con = False

def silentmode(): #check for silent mode
	if ('-s' in option) or ('-s' in fast):
		global con
		con = True

sitename = str(sitename)
if "-h" in sitename:
		helpmenu() #show help menu
else:
		sitename = 'http://' + sitename
		file = open('/usr/local/bin/findadb.py')
		header = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'}
		silentmode()
		with file as f:
			while True: #start scanning
				try:
					if('-f' in option) or ('-f' in fast): #check for fast mode and create 5 threads if so
						th1 = Thread(target=getpage, args=(file,sitename,header,))
						th2 = Thread(target=getpage, args=(file,sitename,header,))
						th3 = Thread(target=getpage, args=(file,sitename,header,))
						th4 = Thread(target=getpage, args=(file,sitename,header,))
						th5 = Thread(target=getpage, args=(file,sitename,header,))
						th1.start()
						th2.start()
						th3.start()
						th4.start()
						th5.start()
						th1.join()
						th2.join()
						th3.join()
						th4.join()
						th5.join()
					else: #else start 1 thread
						th1 = Thread(target=getpage, args=(file,sitename,header,))
						th1.start()
						th1.join()
				except KeyboardInterrupt: #in case of cancelling program
					print('\nexiting')
					sys.exit()
				if t==True: #if success
					sys.exit()
			file.close()
