import sys 
from time import sleep 
import urllib2 
import RPi.GPIO as GPIO
from datetime import datetime

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(27, GPIO.OUT)

temperatureTxt1 = 0
temperatureTxt2 = 0
temperatureTxt3 = 0
temperatureTxt4 = 0
temperatureTxt5 = 0

PumpM1State = -1


#kolektor M1
try:
	tempfile1 = open("/sys/bus/w1/devices/28-020191770a25/w1_slave")
	thetext1 = tempfile1.read()
	tempfile1.close()
	tempdata1 = thetext1.split("\n")[1].split(" ")[9]
	temperature1 = float(tempdata1[2:])
	temperatureTxt1 = temperature1 / 1000
	print (temperatureTxt1)
except:
	print ("sensor error")

#temp pieca
try:
	tempfile2 = open("/sys/bus/w1/devices/28-000005bbd1d1/w1_slave")
	thetext2 = tempfile2.read()
	tempfile2.close()
	tempdata2 = thetext2.split("\n")[1].split(" ")[9]
	temperature2 = float(tempdata2[2:])
	temperatureTxt2 = temperature2 / 1000
	print (temperatureTxt2)
except:
	print("sensor error")

#Kuchnia M1
try:
	tempfile = open("/sys/bus/w1/devices/28-000005aa4abf/w1_slave")
	thetext1 = tempfile.read()
	tempfile.close()
	tempdata1 = thetext1.split("\n")[1].split(" ")[9]
	temperatureM1 = float(tempdata1[2:])
	temperatureTxt3 = temperatureM1 / 1000
	print (temperatureTxt3)
except:
	print("sesn error")

#termostat
current_dateTime = datetime.now()
hourNow = current_dateTime.hour

if int(hourNow) >= 18 and int(hourNow < 23) :
	TempZadana = 22.5
else:
	TempZadana = 22.0

if temperatureTxt2 > 65:
	TempZadana = 22.5

if float(temperatureTxt3) < TempZadana:
	GPIO.output(27, GPIO.HIGH)
	print("\n PUMP_M1_ON")
	PumpM1State = 1
else:
	GPIO.output(27, GPIO.LOW)
	print("PUMP M1 Off")
	PumpM1State = 0



#M2
try:
	tempfile = open("/sys/bus/w1/devices/28-01161da94dee/w1_slave")
	thetext1 = tempfile.read()
	tempfile.close()
	tempdata1 = thetext1.split("\n")[1].split(" ")[9]
	temperature1 = float(tempdata1[2:])
	temperatureTxt4 = temperature1 / 1000
	print (temperatureTxt4)
except:
	print("sensor error")


#Powrot M1
try:
        tempfile1 = open("/sys/bus/w1/devices/28-020b917754ea/w1_slave")
        thetext1 = tempfile1.read()
        tempfile1.close()
        tempdata1 = thetext1.split("\n")[1].split(" ")[9]
        temperature1 = float(tempdata1[2:])
        temperatureTxt5 = temperature1 / 1000
        print (temperatureTxt5)
except:
        print ("sensor error")



baseURL = 'http://api.thingspeak.com/update?api_key=7MK6L089WHKG1FB1&field1=' 
f = urllib2.urlopen(baseURL + str(temperatureTxt2) + '&field2=' + str(temperatureTxt3) + '&field3=' + str(temperatureTxt4) + '&field4=' + str(temperatureTxt1) + '&field5=' + str(temperatureTxt5) + '&field6=' + str(TempZadana) + '&field7=' + str(PumpM1State) ) 
f.read() 
f.close() 
sleep(5) 

print "Program has ended"
