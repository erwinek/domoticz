import sys 
from time import sleep 
import urllib2 

tempfile1 = open("/sys/bus/w1/devices/10-000801d2ca71/w1_slave")
thetext1 = tempfile1.read()
tempfile1.close()
tempdata1 = thetext1.split("\n")[1].split(" ")[9]
temperature1 = float(tempdata1[2:])
temperatureTxt1 = temperature1 / 1000
print (temperatureTxt1)

tempfile2 = open("/sys/bus/w1/devices/28-000005bbd1d1/w1_slave")
thetext2 = tempfile2.read()
tempfile2.close()
tempdata2 = thetext2.split("\n")[1].split(" ")[9]
temperature2 = float(tempdata2[2:])
temperatureTxt2 = temperature2 / 1000
print (temperatureTxt2)

tempfile = open("/sys/bus/w1/devices/28-000005aa4abf/w1_slave")
thetext1 = tempfile.read()
tempfile.close()
tempdata1 = thetext1.split("\n")[1].split(" ")[9]
temperature1 = float(tempdata1[2:])
temperatureTxt3 = temperature1 / 1000
print (temperatureTxt3)

tempfile = open("/sys/bus/w1/devices/28-01161da94dee/w1_slave")
thetext1 = tempfile.read()
tempfile.close()
tempdata1 = thetext1.split("\n")[1].split(" ")[9]
temperature1 = float(tempdata1[2:])
temperatureTxt4 = temperature1 / 1000
print (temperatureTxt4)

baseURL = 'http://api.thingspeak.com/update?api_key=7MK6L089WHKG1FB1&field1=' 
f = urllib2.urlopen(baseURL + temperatureTxt1 + '&field2=' + temperatureTxt2 + '&field3=' + temperatureTxt4 + '&field5=' + temperatureTxt5) 
f.read() 
f.close() 
sleep(5) 

print "Program has ended"