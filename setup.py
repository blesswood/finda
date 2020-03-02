#!usr/bin/env python3

#install cfscrape before setup
#pip install cfscrape

import os

r = "Do you really want to install this software? (y/n)"
print(r, end=" ")
if('y' in input()):
	pwd = str(os.popen('pwd').read().split())[2:-2] #get current directory
	try:
		symlink = "sudo ln -s " + pwd +"/finda.py"+" /usr/local/bin" #symlink finda.py to /usr/local/bin
		os.popen('sudo chmod +x finda.py') #give permission to be executable
		os.popen(symlink)
		symlink = "sudo ln -s " + pwd +"/findadb.py"+" /usr/local/bin" #symlink db
		os.popen(symlink)
		r = 'sudo cp findaman /usr/share/man/man1/finda.py.1' #copy manpage to man1
		os.popen(r)
		r = 'sudo gzip /usr/share/man/man1/finda.py.1'
		os.popen(r)
		print('Success! Try: finda.py -h or man finda.py\n')
		print('If you decide to uninstall: sudo python3 uninstall.py\n')
	except SystemError:
		print("Oops, try with sudo!")
	except KeyboardInterrupt:
		sys.exit()
