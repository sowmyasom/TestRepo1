import time
import serial
import urllib.request as urllib2
ser = serial.Serial('COM3', 9600)
while True:
	message = str(ser.readline())
	if len(message.split(": "))>1:
		distance = message.split(": ")[1].replace(" cm", "").replace("\\r\\n\'", "")
		print("distance: "+distance)
		print(">>Sending Write request to Thingspeak...")
		response = urllib2.urlopen(
		'https://api.thingspeak.com/update?api_key=XI5ZVSAPPCCKWUTG&field1='+message.split(": ")[1][:-2])
		html = response.read()
		time.sleep(20)