#!/usr/bin/env python
# -*- coding: utf-8 -*-

from info import MetaData
from time import sleep
def goodReport():
	goodReport = MetaData("23.888888,4.333333", "IntecBrussel.jpg", {"goodfeedback":"Good feedback"},"This road is recommended", {"ultrasonic_sensor":[1,2,3],"accelerometer":[1,2,3],"light_sensor":[1,2,3]})
	goodReport.send()

def badReport():
	badReport = MetaData("23.888888,4.333333", "IntecBrussel.jpg", {"badfeedback":"Bad feedback"},"This road is not recommended", {"ultrasonic_sensor":[1,2,3],"accelerometer":[1,2,3],"light_sensor":[1,2,3]})
	badReport.send()


def sosSignal():
	sos = MetaData("23.888888,4.333333", "IntecBrussel.jpg", {"sos_signal":"S0s Signal"},"911 SIGNAL", {"ultrasonic_sensor":[1,2,3],"accelerometer":[1,2,3],"light_sensor":[1,2,3]})
	sos.send()
	print("Calling to 112...")
	sleep(1)
	print("Session started")
	sleep(1)
	print("Talk now!...☏")
	sleep(60)
	'''
	need to call hospital or police here by [press button(sos)] [session started]
	and then hang up the phone call by press button[sos]
	'''


def main():
	print('''
	 (   (       )        (     
	 )\ ))\ ) ( /(   *   ))\ )  
	(()/(()/( )\())` )  /(()/(  
	 /(_))(_)|(_)\  ( )(_))(_)) 
	(_))(_))   ((_)(_(_()|_))   
	| _ \_ _| / _ \|_   _/ __|  
	|   /| | | (_) | | | \__ \  
	|_|_\___| \___/  |_| |___/  
	                                                        
	       '''
	       # Data Sender

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

  #first_photo = MetaData("23.888888,4.333333", "IntecBrussel.jpg", "BAD[fordrink]","This road is not recommended", [12.00, 3.04, 6.205])
  #first_photo.send()

if __name__ == "__main__":
	while True:
		main()