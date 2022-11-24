import requests
import urllib

nombre = input("Introduce tu nombre: ")
mensaje = input("Introduce el dato que quieres guardar en la bd: ")

url = 'http://35.195.125.149:10111/rest/bquery'

#Create datastore request
datos = {
  "key": "BC.8c8a7327dfb64d02bda29df080b9e43338a5bd8f6735413d8e837dc58f235599",
  "username" : "root",
  "password" : "root",
  "ds" : "prueba",
  "c" : "coleccion",
  "q" : "insert",
  "p" : {
    "data" : ["JSON", {
      "nombre": nombre,
      "mensaje": mensaje }]
  }
}

headers = {
  'Content-Type': 'application/json',
  }

response = requests.post(url=url, json=urllib.parse.urlencode(datos), headers=headers)

print(response)
print(response.headers)
print(response.text)
print(response.content)

with open('./log_blobcity.txt','w') as f:
  f.write(str(response))
  f.write('\n')
  f.write(str(response.text))
  f.write('\n')
  f.write(str(response.content))