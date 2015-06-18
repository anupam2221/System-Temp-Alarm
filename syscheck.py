# (c) anupamkumar08--->https://github.com/anupamkumar08
# this file when run prints the core temp and acts accordingly....Make sure u have sensors command package available 
# TO MAKE THIS PROCESS AUTOMATIC go to /etc/init.d and copy this and turn it into executable and run update rc.d syscheck.py defaults
# Here is the small code
import time 
import urllib2
import sensors
import subprocess
import linecache
v=1
while v<2 :
	f=1
	file = open('temp.txt','a')
	beat=subprocess.Popen('sensors', shell=True, stdout=subprocess.PIPE,)
	t=beat.communicate()[0]	
	#print t	
	file.write(str(t))
	file.close()
	file = open('temp.txt','r')
	#print linecache.getline('temp.txt','1')	
	with open('temp.txt')as f:
		i=1
		for line in f:
			if i==8:
				break
			i=i+1
		i=1
	parts=line.split(' ')
	x=parts[4]
	z=list(x)
	y = [z[1],z[2]]
	l=''.join(y)
	lol=int(l)
	print lol
	if lol>=80 and lol<=85:
		print "\a"
	elif lol>85:
		print "\a\a\a"	
	file.close()
	open('temp.txt','w').close()
	#v+=1
	time.sleep(8)
   
