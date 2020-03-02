import os
print('\nAre you sure want to uninstall this software?(y/N): ', end = " ")
if 'y' in input():
    os.popen('sudo rm /usr/local/bin/finda*')
    os.popen('sudo rm /usr/share/man/man1/finda.py*')
    print('Success, see you later!\n')
else:
    print('Aborted\n')
