#!/usr/bin/env python
# -*- coding: utf-8 -*-

from info import MetaData
from time import sleep
import datetime
import time
import json
import base64

'''left_button = Button(23)
right_button = Button(24)
camera = PiCamera()
'''

def get_file_name():
    a=  datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S.jpg")
    
    return a

def goodReport():
	goodReport = MetaData({"lat":[23.888888],"lng":[4.333333]}, "fileName", "Good Feedback", "This road is recommended", {"ultrasonic_sensor":[1,2,3],"accelerometer":[1,2,3],"light_sensor":[1,2,3]})
	goodReport.send()

def badReport():
	badReport = MetaData({"lat":[23.888888],"lng":[4.333333]}, "IntecBrussel.jpg", "Bad Feedback","This road is not recommended", {"ultrasonic_sensor":[1,2,3],"accelerometer":[1,2,3],"light_sensor":[1,2,3]})
	badReport.send()


def sosSignal():
	sos = MetaData({"lat":[23.888888],"lng":[4.333333]}, "IntecBrussel.jpg", "Sos Signal","911 SIGNAL", {"ultrasonic_sensor":[1,2,3],"accelerometer":[1,2,3],"light_sensor":[1,2,3]})
	sos.send()
	print("Calling to 112...")
	sleep(1)
	print("Session started")
	sleep(1)
	print("Talk now!...☏")
	sleep(60)
	
def main():
	print('''
	RIOTS
                                       
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
