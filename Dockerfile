FROM ubuntu:22.04

#Crear un directorio
WORKDIR /datosCliente

#Añadir el script de al directorio
COPY ./cliente-blobcitydb.txt /datosCliente

#Ejecutar el script
CMD nc localhost 10113 < cliente-blobcitydb.txt