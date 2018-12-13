#!/usr/bin/env python
# -*- coding: utf-8 -*-
from picamera import PiCamera
from info import MetaData
from time import sleep
import datetime
import datetime as dt
import time
import json
import base64
import os

camera = PiCamera()
cwd = os.getcwd()

def capture():
	# Taking picture and save file in the folder with current time
    picTime = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    picName = picTime + '.jpg'
    path = cwd + '/PiCameraRecords/' + picName
    #camera.capture(path)
    return path



def goodReport():
	"""
	Taking picture and save file in the folder with current time
	"""
	goodReport = MetaData({"lat":[23.888888],"lng":[4.333333]}, capture(), "Good Feedback", "This road is recommended", {"ultrasonic_sensor":[1,2,3],"accelerometer":[1,2,3],"light_sensor":[1,2,3]})
	goodReport.send()

def badReport():
	"""
	Sending good feedback here
	"""
	badReport = MetaData({"lat":[23.888888],"lng":[4.333333]}, capture(), "Bad Feedback", "This road is not recommended", {"ultrasonic_sensor":[1,2,3],"accelerometer":[1,2,3],"light_sensor":[1,2,3]})

        badReport.send()


def sosSignal():
	"""
	Sending SOS signal here
	"""
	sos = MetaData({"lat":[23.888888],"lng":[4.333333]}, capture(), "SOS Signal", "This is a SOS signal", {"ultrasonic_sensor":[1,2,3],"accelerometer":[1,2,3],"light_sensor":[1,2,3]})
        sos.send()
	print("Calling to 112...")
	sleep(1)
	print("Session started")
	sleep(1)
	print("Talk now!...")
	sleep(60)
	
def main():
	"""
	Main menu to send a feedback [for testing program]
	"""
	print('''
	
eeeee  e  eeeee eeeee eeeee 
8   8  8  8  88   8   8   " 
8eee8e 8e 8   8   8e  8eeee 
88   8 88 8   8   88     88 
88   8 88 8eee8   88  8ee88 
                                       
	       '''
	       

	  )
	
	user = input("[1] - Send good feedback\n[2] - Send bad feedback\n[3] - Send SOS Signal\n ~$ ")
	if user == 1:
		print("Pressed button! the road is good.")
		goodReport()
	elif user == 2:
		print("Pressed button! the road is not good")
		badReport()
	elif user == 3:
		print("Press button! Sent SOS signal")
		sosSignal()
	else:
		print("init 0")


if __name__ == "__main__":
	while True:
		main()
