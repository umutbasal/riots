import json, ast
from pprint import pprint
import numpy as np
import matplotlib.pyplot as plt
import pprint
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
       # JSON DATA

  )

def find(key, dictionary):
    for k, v in dictionary.iteritems():
        if k == key:
            yield v
        elif isinstance(v, dict):
            for result in find(key, v):
                yield result
        elif isinstance(v, list):
            for d in v:
                for result in find(key, d):
                    yield result

#HowManyRecords = input("How many records would you like to see? ex[1-100] ")
with open('data.json', 'r') as f:

    r107sData = json.load(f)
    CleanData = ast.literal_eval(json.dumps(r107sData))
  


for r107s in CleanData:
    
    print("User Id" , r107s['user_id'])
    print("FeedBack", r107s['feedback'])
    print("Location", r107s['location'])
    print("Sensors", r107s['sensors'])
    print("Time", r107s['time'])
    print("UltraSonic Sensor", r107s['sensors']['ultrasonic_sensor'])
    print("Accelerometer", r107s['sensors']['accelerometer'])
    print("Light Sensor", r107s['sensors']['light_sensor'])
    ultrasonic = len(r107s['sensors']['ultrasonic_sensor'])
    acce = len(r107s['sensors']['accelerometer'])
    light = len(r107s['sensors']['light_sensor'])
    

    #print(r107s['feedback'][0])
    

    print("\n")
    #print(r107s['sensors']['ultrasonic_sensor'][0])
    #print(r107s['feedback'][0])




# Fake dataset
height = [r107s['sensors']['ultrasonic_sensor'][0],r107s['sensors']['ultrasonic_sensor'][1],r107s['sensors']['ultrasonic_sensor'][2]]
bars = ('VALUE1','VALUE2','VALUE3')
y_pos = np.arange(len(bars))
 
# Create bars and choose color
plt.bar(y_pos, height, color = (0.5,0.1,0.5,0.6))
 
# Add title and axis names
plt.title('DATA ANALYSIS')
plt.xlabel('SIGNALS')
plt.ylabel('COUNT')
 
# Limits for the Y axis
plt.ylim(0,60)
 
# Create names
plt.xticks(y_pos, bars)
 
# Show graphic
#plt.show()
