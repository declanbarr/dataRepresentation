import requests
import json

#Remove the minus sign
apiKey = 'e2242681c87c17a2e70c9469111ae8986495a5f-5'
url = 'https://api.github.com/user/repos'


filename = 'declan_repo.json'

response = requests.get(url, auth=('token', apiKey))

repoJSON = response.json()
#print(response.json())

file = open(filename, 'w')
json.dump(repoJSON, file, indent=4)