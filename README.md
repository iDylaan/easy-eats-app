# Primera ejecucion
docker-compose up

# Actualizar
docker-compose up --build


# Instanciando las variables de entorno desde el .env
docker run --env-file=.env environ_image.

# Instanciar base de datos
docker-compose exec bd sh -c 'mysql -u root -p"password" < /docker-entrypoint-initdb.d/easy_eats_db.sql'


## Para conocer la direccion IP de la base de datos 
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' easyeats_db