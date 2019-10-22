tempfile1 = open("/sys/bus/w1/devices/10-000801d2ca71/w1_slave")
thetext1 = tempfile1.read()
tempfile1.close()
tempdata1 = thetext1.split("\n")[1].split(" ")[9]
temperature1 = float(tempdata1[2:])
temperatureTxt = temperature1 / 1000
print (temperatureTxt)

tempfile2 = open("/sys/bus/w1/devices/28-000005bbd1d1/w1_slave")
thetext2 = tempfile2.read()
tempfile2.close()
tempdata2 = thetext2.split("\n")[1].split(" ")[9]
temperature2 = float(tempdata2[2:])
temperatureTxt = temperature2 / 1000
print (temperatureTxt)

tempfile = open("/sys/bus/w1/devices/28-000005aa4abf/w1_slave")
thetext1 = tempfile1.read()
tempfile.close()
tempdata1 = thetext1.split("\n")[1].split(" ")[9]
temperature1 = float(tempdata1[2:])
temperatureTxt = temperature1 / 1000
print (temperatureTxt)

tempfile = open("/sys/bus/w1/devices/28-01161da94dee/w1_slave")
thetext1 = tempfile1.read()
tempfile.close()
tempdata1 = thetext1.split("\n")[1].split(" ")[9]
temperature1 = float(tempdata1[2:])
temperatureTxt = temperature1 / 1000
print (temperatureTxt)