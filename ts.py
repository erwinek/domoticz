import sys 
from time import sleep 
import urllib2 
a = 40 
baseURL = 'http://api.thingspeak.com/update?api_key=7MK6L089WHKG1FB1&field1=' 
while(a < 60):
	print a 
	f = urllib2.urlopen(baseURL +str(a)) 
	f.read() 
	f.close() 
	sleep(5) 
	a = a+1
print "Program has ended"
