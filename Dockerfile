FROM python

#Instalar python
RUN apt update
RUN apt -y install python3

#Crear un directorio
WORKDIR /datosCliente

#Añadir el script de python al directorio
COPY ./aplicacion-cliente.py /datosCliente

#Descargar las librerias necesarias
RUN pip3 install requests

#Ejecutar el script
CMD python3 aplicacion-cliente.py