import requests
import json

URL = "http://192.168.1.8:8000/studentAPI/"

def get_data(id = None):
    data = {}
    if id is not None:
       data = {'id',id}
    json_data = json.dumps(data)
    r = requests.get(url = URL,data = json_data)
    data = r.json()
    print(data)

get_data()

# data = {
#     'id':77,
#     'name':'alpa',
#     'roll':11,
#     'city':'JND'
# }

# json_data = json.dumps(data)
# r = requests.post(url = URL,data=json_data)
# data = r.json()

# print(data)