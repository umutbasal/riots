import json, ast
from pprint import pprint
import numpy as np
import matplotlib.pyplot as plt
import pprint
print('''


       '''
       # JSON DATA

  )
def count(list, feedback):
  with open(list, "r") as file:
    decodeJson = json.loads(file.read())
    result = 0
    for data in decodeJson:
      if (data["feedback"] == feedback):
        result +=1
    return result

print("How many SOS: ", count("data.json", "SOS"),"\n")
print("How many GOOD FEEDBACK: ", count("data.json", "GOOD"),"\n")
print("How many BAD FEEDBACK: ", count("data.json", "BAD"),"\n")
sos = count("data.json", "SOS")
good = count("data.json", "GOOD")
bad = count("data.json", "BAD")


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
    #str = 'Number of users = {0}'.format(len(r107s))
    print("\n")




def graphicMaker(value1,value2,value3,graphicName):
    height = value1,value2,value3
    bars = (str(value1),str(value2),str(value3))
    y_pos = np.arange(len(bars))
    plt.bar(y_pos,height, color = (0.5,0.1,0.5,0.6))
    plt.title('DATA ANALYSIS')
    plt.xlabel('VALUES')
    plt.ylabel('COUNT')
    plt.ylim(0,60)
    plt.xticks(y_pos,bars)
    plt.savefig(graphicName)


graphicMaker(sos,good,bad,'test.png')

'''
# Fake dataset

# Sensors values stats
#height = [r107s['sensors']['ultrasonic_sensor'][0],r107s['sensors']['ultrasonic_sensor'][1],r107s['sensors']['ultrasonic_sensor'][2]]

# feedback stats
height = sos,good,bad

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
plt.savefig('stats.png')
# Show graphic


'''