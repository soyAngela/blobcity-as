sleep 10

container_id=$ (sudo docker ps -aqf "name=blobcity-db-container")
password=$ (sudo docker exec -it $container_id cat /data/root-pass.txt)

sed -i "2s/.*/$password/" comandos-blobcitydb.txt

nc blobcity-db-container 10113 < comandos-blobcitydb.txt

echo "Creada nueva base de datos: REGISTRO"
echo "Creada nueva coleccion: VISITAS"