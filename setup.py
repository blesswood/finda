#!usr/bin/env python3

import os

r = "Do you really want to install this software? (y/n)"
print(r, end=" ")
if('y' in input()):
	import os
	pwd = str(os.popen('pwd').read().split())[2:-2]
	try:
		symlink = "sudo ln -s " + pwd +"/finda.py"+" /usr/local/bin"
		os.system('sudo chmod +x finda.py')
		os.popen(symlink)
		symlink = "sudo ln -s " + pwd +"/findadb.py"+" /usr/local/bin"
		os.popen(symlink)
#		if('failed' in res):
#			os.system('sudo rm /usr/local/bin/cyth.py')
#		os.system(symlink)
		print('Success! Try: finda.py -h')
	except SystemError:
		print("Oops, try with sudo!")
