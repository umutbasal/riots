#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://github.com/Twilliamson90/Marker-Filtering-Google-Maps
import json
import time
print('''
 (    (        )         (     
 )\ ) )\ )  ( /(   *   ) )\ )  
(()/((()/(  )\())` )  /((()/(  
 /(_))/(_))((_)\  ( )(_))/(_)) 
(_)) (_))    ((_)(_(_())(_))   
| _ \|_ _|  / _ \|_   _|/ __|  
|   / | |  | (_) | | |  \__ \  
|_|_\|___|  \___/  |_|  |___/  
                               
       '''
       # UML Schema

  )
class MetaData:
  def __init__(self, location, photo, feedback,description, sensors):
    self.location = location
    self.photo = photo
    self.feedback = feedback
    self.description = description
    self.sensors = sensors
    self.db = "data.json"
  def dataFile(self, data):
    with open(self.db, 'r') as file:
      decodedFile = json.loads(file.read())
      data['user_id'] = decodedFile[-1]['user_id'] + 1 if len(decodedFile) else 0
      decodedFile.append(data)
      file.close()
      with open(self.db, 'w') as file:
        encodedFile = json.dumps(decodedFile)
        file.write(encodedFile)
        file.close()
      
  def send(self):
    self.dataFile({ "time": time.time(), "location": self.location, "photo": self.photo, "feedback": self.feedback, "description": self.description, "sensors": self.sensors })

