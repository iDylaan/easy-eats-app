## Ambiente para backend
pip install virtualenv
virtualenv venv
venv/Scripts/activate
pip install -r requirements.txt

python EASY-EATS-APP.py

# ========================================

❯ docker build -t easyeatsbackapp .

❯ docker run -it -p 4000:4000 easyeatsbackapp

# Como un proceso
❯ docker run -it -p 7000:4000 -d easyeatsbackapp

# Para verlo
❯ docker container ls

# Detenerlo
❯ docker stop (id del contenedor)

# Deploy a produccion
flyctl deploy

# Entrar a consola 
flyctl ssh console

# Obtener IP Publica desde consola
curl ifconfig.me
