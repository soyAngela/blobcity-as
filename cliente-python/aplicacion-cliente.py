import requests
import urllib

url = 'http://blobcity-db-container:10111/rest/bquery'

datos = {
  "key": "BC.9f8e21f3e73e4751ac5582b5edb52548e1cd029d26554c6eb5ec70b31f67e2fc",
  "username" : "root",
  "password" : "root",
  "ds" : "registro",
  "c" : "visitas",
  "q" : "insert",
  "p" : { "data" : [{
      "nombre": "Angela",
      "mensaje": "Hola mundo!" }] },
  
}

headers = {
  'Content-Type': 'application/json',
  }

response = requests.post(url=url, json=datos, headers=headers)

with open('./log_blobcity.txt','a') as f:
  f.write(str(response))
  f.write('\n')
  f.write(str(response.text))
  f.write('\n')
  f.write(str(response.content))
  f.write('\n')
  f.write(str(response.request.body))