import os
import requests
import json

url = "http://homelockos.com/data/json/statuses.json"

r = requests.get(url)

data = json.loads(r.content.decode())



print(data["lock"]["locked"])
