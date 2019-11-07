import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

 
while 1:
	GPIO.setup(17, GPIO.OUT)
	
	GPIO.output(17, GPIO.HIGH)
	print 1
	time.sleep(5)

	GPIO.output(17, GPIO.LOW)
	print 0
	time.sleep(5)
