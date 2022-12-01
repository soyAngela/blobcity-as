FROM ubuntu:22.04

#Crear un directorio
WORKDIR /datosCliente

#Añadir el script de al directorio
COPY ./comandos-blobcity.txt /datosCliente
COPY ./cliente-blobcitydb.sh /datosCliente

#Instalar netcat
RUN apt update
RUN apt -y install netcat

#Ejecutar el script
CMD ./cliente-blobcitydb.sh