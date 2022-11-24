import requests
import urllib

while True:
  nombre = input("Introduce tu nombre: ")
  if nombre == 'exit':
    break
  mensaje = input("Introduce el dato que quieres guardar en la bd: ")
  

  url = 'http://localhost:10111/rest/bquery'

  #Create datastore request
  datos = {
    "key": "",
    "username" : "root",
    "password" : "root",
    "ds" : "prueba",
    "c" : "coleccion",
    "q" : "insert",
    "p" : { },
    "data" : ["JSON", {
        "nombre": nombre,
        "mensaje": mensaje }]
  }

  headers = {
    'Content-Type': 'application/json',
    }

  response = requests.post(url=url, json=urllib.parse.urlencode(datos), headers=headers)

  print(response)
  print(response.headers)
  print(response.text)
  print(response.content)

  with open('./log_blobcity.txt','a') as f:
    f.write(str(response))
    f.write('\n')
    f.write(str(response.text))
    f.write('\n')
    f.write(str(response.content))