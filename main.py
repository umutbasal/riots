#!/usr/bin/env python
# -*- coding: utf-8 -*-

from info import MetaData

def goodReport():
	goodReport = MetaData("23.888888,4.333333", "IntecBrussel.jpg", "GOOD ROAD","This road is recommended", "[12.00, 3.04, 6.205]")
	goodReport.send()

def badReport():
	badReport = MetaData("23.888888,4.333333", "IntecBrussel.jpg", "BAD ROAD","This road is not recommended", "[12.00, 3.04, 6.205]")
	badReport.send()


def sosSignal():
	sos = MetaData("23.888888,4.333333", "IntecBrussel.jpg", "SOS","911 SIGNAL", "[12.00, 3.04, 6.205]")
	sos.send()
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
	user = input("[1] - Send good feedback\n[2] - Send bad feedback\n[3] - Send SOS Signal")
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