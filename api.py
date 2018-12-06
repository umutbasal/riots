import json
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
#HowManyRecords = input("How many records would you like to see? ex[1-100] ")
with open('data.json', 'r') as f:
    r107sData = json.load(f)

for r107s in r107sData:

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
    goodfeedback = len(r107s['feedback']['goodfeedback'][0])
    badfeedback = len(r107s['feedback']['badfeedback'][0])
    sos = len(r107s['feedback']['sos_signal'][0])
'''
jsonData = json.dumps(data_item, sort_keys=True, indent=5)
    JSON CODE FORMATTER
    #print json.dumps(data_item, sort_keys=True, indent=5)
    data = json.loads(jsonData)
    '''
print (sos)

# Fake dataset
height = [1,10,2]
bars = ('BAD FEEDBACK','GOOD FEEDBACK','SOS SIGNAL')
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
plt.show()
