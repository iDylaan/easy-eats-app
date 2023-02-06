❯ docker build -t easyeatsapp .

❯ docker run -it -p 7000:4000 easyeatsapp

# Como un proceso
❯ docker run -it -p 7000:4000 -d easyeatsapp

# Para verlo
❯ docker container ls

# Detenerlo
❯ docker stop (id del contenedor)