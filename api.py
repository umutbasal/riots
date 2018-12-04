import json
from pprint import pprint
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

    print("UserID", r107s['user_id'])
    print("FeedBack", r107s['feedback'])
    print("Location", r107s['location'])
    print("Sensors", r107s['sensors'])
    print("Time", r107s['time'])
    
'''
jsonData = json.dumps(data_item, sort_keys=True, indent=5)
    JSON CODE FORMATTER
    #print json.dumps(data_item, sort_keys=True, indent=5)
    data = json.loads(jsonData)
    '''