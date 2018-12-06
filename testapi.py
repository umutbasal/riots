import json

def count(list, feedback):
  with open(list, "r") as file:
    decodeJson = json.loads(file.read())
    result = 0
    for data in decodeJson:
      if (data["feedback"] == feedback):
        result +=1
    return result
    
print(count("data.json", "SOS"))