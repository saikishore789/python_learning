import json


obj = {
  "name": "Alice",
  "city": "Madrid"
}
   
json_file = json.dumps(obj, indent = 1)

print(json_file)