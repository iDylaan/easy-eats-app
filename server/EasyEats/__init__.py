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

### SQL ALCHEMY ###
app.config['SQLALCHEMY_DATABASE_URI'] = '{}://{}:{}@{}:{}/{}?charset=utf8mb4'.format(
    os.getenv("MARIA_TIPO_DB"),
    os.getenv("MARIA_USER"),
    os.getenv("MARIA_PASS"),
    os.getenv("MARIA_HOST"),
    os.getenv("MARIA_PORT"),
    os.getenv("MARIA_DB")
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

### ROUTER ###
from EasyEats.usuarios.routes import mod as mod_usuarios

### BLUEPRINTS ###
app.register_blueprint(mod_usuarios)