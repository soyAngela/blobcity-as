container_id=$(sudo docker ps -aqf "name=blobcity-db-container")
password=$(sudo docker exec -it $container_id cat /data/root-pass.txt)
password=$(echo $password%?})

echo "root" > password-change.txt
echo "$password" >> password-change.txt
echo "set-user-password root $password root" >> password-change.txt
echo "exit" >> password-change.txt

nc localhost 10113 < password-change.txt