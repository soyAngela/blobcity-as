FROM python

#Instalar python
RUN apt update
RUN apt -y install python3

#Crear un directorio
WORKDIR /data

#Añadir el script de python al directorio
COPY ./aplicacion-cliente.py /data

#Descargar las librerias necesarias
RUN pip3 -y install 

#Ejecutar el script
CMD python3 aplicacion-cliente.py