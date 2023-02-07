❯ docker build -t easyeatsbackapp .

❯ docker run -it -p 7000:4000 easyeatsbackapp

# Como un proceso
❯ docker run -it -p 7000:4000 -d easyeatsbackapp

# Para verlo
❯ docker container ls

# Detenerlo
❯ docker stop (id del contenedor)