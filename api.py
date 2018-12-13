import json, ast
from pprint import pprint
import numpy as np
import matplotlib.pyplot as plt
import pprint
print('''


                            
eeeee  e  eeeee eeeee eeeee 
8   8  8  8  88   8   8   " 
8eee8e 8e 8   8   8e  8eeee 
88   8 88 8   8   88     88 
88   8 88 8eee8   88  8ee88 
                            


       '''
       # JSON DATA

  )
def count(list, feedback):

    """
    Parsing json data and counting item.
    """
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


with open('data.json', 'r') as f:
    """
    Json Data is loading
    """
    r107sData = json.load(f)
    CleanData = ast.literal_eval(json.dumps(r107sData))



for r107s in CleanData:
    """
    Getting data from json file
    """
    print("User Id" , r107s['user_id'])
    print("FeedBack", r107s['feedback'])
    print("Location Latitude", r107s['location']['lat'])
    print("Location Longitude", r107s['location']['lng'])
    print("Sensors", r107s['sensors'])
    print("Time", r107s['time'])
    print("UltraSonic Sensor", r107s['sensors']['ultrasonic_sensor'])
    print("Accelerometer", r107s['sensors']['accelerometer'])
    print("Light Sensor", r107s['sensors']['light_sensor'])
    ultrasonic = len(r107s['sensors']['ultrasonic_sensor'])
    acce = len(r107s['sensors']['accelerometer'])
    light = len(r107s['sensors']['light_sensor'])
    print("\n")

def graphicMaker(value1,value2,value3,graphicName):
    """
    Matplotlib stats generator method
    """
    height = value1,value2,value3
    bars = ('ultrasonic','accelerometer','light_sensor')
    y_pos = np.arange(len(bars))
    plt.bar(y_pos,height, color = (0.5,0.1,0.5,0.6))
    plt.title('DATA ANALYSIS')
    plt.xlabel('VALUES')
    plt.ylabel('COUNT')
    plt.ylim(0,60)
    plt.xticks(y_pos,bars)
    plt.savefig(graphicName)


graphicMaker(sos,good,bad,'test.png')