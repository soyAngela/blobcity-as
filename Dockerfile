FROM ubuntu:22.04

#Crear un directorio
WORKDIR /datosCliente

#Instalar python e instalar las librerias necesarias
RUN apt update
RUN apt -y install python3
RUN pip3 install requests

#Añadir el script de python al directorio
COPY ./aplicacion-cliente.py /datosCliente

#Ejecutar el script
CMD python3 aplicacion-cliente.py