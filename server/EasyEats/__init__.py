import os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

### Cargar configuracion ###
load_dotenv(".env")
### Cargar App ###
app = Flask(__name__)

### CORS (Cross-Origin Resource Sharing) ### 
# CORS(app, supports_credentials=True, origins="*", methods=["GET", "POST", "PUT", "DELETE"], headers="*")
CORS(app)


### ROUTER ###
from EasyEats.usuarios.routes import mod as mod_usuarios

### BLUEPRINTS ###
app.register_blueprint(mod_usuarios)