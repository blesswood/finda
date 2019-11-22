# FINDA
Python script for finding admin pages on web servers  

Installation on Linux:  
>git clone https://github.com/blesswood/finda.git  
>cd finda  
>sudo python3 setup.py  

May require additional libraries:  
>pip3 install threading  
>pip3 install requests  

Usage: finda.py -h or man finda.py  

Log:  
Edited requests lib to cfscrape  
Added man page(see 'man finda.py') and time spent on work
Added timer(at first it counts for 450 popular pages and then last 7k pages)
Added wizard mode, edited output in case of cancelling  
Fixed performance(deleted unnecessary functions), KeyboardInterrupt error and output  
Added scrollbar and comments  
Added proxy
