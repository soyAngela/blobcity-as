'''
https://docs.db.blobcity.com/docs/inserting-data

'''
import requests

url = 'http://35.195.125.149:10111/rest/bquery'

#Create datastore request
payload = {
  'username' : 'root',
  'password' : 'root',
  'q' : 'list-ds'
}

headers = { 
    'Content-Length': str(len(payload)),
    'Content-Type': 'application/json'
}

response = requests.post(url=url, json=payload, headers=headers)

print(response)
print(response.headers)
print(response.text)