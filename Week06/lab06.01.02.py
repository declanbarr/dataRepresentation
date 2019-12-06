import requests
import json

dataString = {'reg':'08 c1234', 'make':'Ford', 'model':'Galaxy', 'price':1234}
url = 'http://127.0.0.1:5000/cars'

response = requests.post(url, json=dataString)

print(response.status_code)