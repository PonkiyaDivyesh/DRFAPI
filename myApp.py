import requests
import json

URL = "http://192.168.1.8:8000/addStuInfo/"

data = {
    'id':5,
    'name':'alpa',
    'roll':11,
    'city':'JND'
}

json_data = json.dumps(data)
r = requests.post(url = URL,data=json_data)
data = r.json()

print(data)