import simplejson as json
import os

if os.path.isfile("./simple.json") and os.stat("./simple.json").st_size != 0:
    json_file = open("./simple.json", "r+")
    data = json.loads(json_file.read())
    print("Current age is:", data["age"], "-- adding a year")
    data["age"] = data["age"] + 1
    print("new age is:", data["age"])
else:
    json_file = open("./simple.json","w+")
    data = {"name": "Raju", "age": 29}
    print("No file found, setting default age to ", data["age"])

json_file.seek(0)
json_file.write(json.dumps(data))