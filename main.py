#!/usr/bin/env python
# -*- coding: utf-8 -*-

from info import MetaData
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
def main():
  first_photo = MetaData("23.888888,4.333333", "test.jpg", "GOOD","This road is not recommended", [12.00, 3.04, 6.205])
  first_photo.send()

if __name__ == "__main__":
  main()