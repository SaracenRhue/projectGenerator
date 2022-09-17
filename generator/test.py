import json

f = open('./generator/data.json')
data = json.load(f)
print(data)

f.close()