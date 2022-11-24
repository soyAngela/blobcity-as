import requests
import urllib

while True:
  nombre = input("Introduce tu nombre: ")
  if nombre == 'exit':
    break
  mensaje = input("Introduce el dato que quieres guardar en la bd: ")
  

  url = 'http://35.195.125.149:10111/rest/bquery'

  #Create datastore request
  datos = {
    "key": "BC.9f8e21f3e73e4751ac5582b5edb52548e1cd029d26554c6eb5ec70b31f67e2fc",
    "username" : "root",
    "password" : "root",
    "ds" : "prueba",
    "c" : "coleccion",
    "q" : "insert",
    "p" : { "data" : ["JSON", {
        "nombre": nombre,
        "mensaje": mensaje }] },
    
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
    f.write('\n')
    f.write('\n')