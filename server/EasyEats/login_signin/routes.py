from datetime import datetime
from flask import Blueprint, request, jsonify
from flask_cors import CORS
from cerberus import Validator
from .schemas import user_schema
from werkzeug.security import generate_password_hash, check_password_hash
from .sql_strings import Sql_Strings as SQL_STRINGS
from EasyEats.config.conf_maria import query
from EasyEats.utils.misc import jwt, validate_email_exist, validate_user_exist


# MODULE
mod = Blueprint('login_signin', __name__, 
    template_folder='templates', 
    static_folder='static', 
    static_url_path='/%s' % __name__
)


# CORS acces to "login_signin"
CORS(mod)

# CORS Configure Parameters
@mod.route('/users', methods=['OPTIONS'])
def handle_options():
    return "", 200, {
        "Access-Control-Allow-Origin": "*", # "*"
        "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE",
        "Access-Control-Allow-Headers": "Content-Type, Authorization"
    }


# Schemas validate
def val_req_data(data, schema): # validate request data
    v = Validator(schema)
    if not v.validate(data):
        respose = {
            "message": v.errors,
            "status": 400,
            "data": None
        }
        return jsonify(respose)
    return None


@mod.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        email = data.get('email', None)
        password = data.get('password', None)
        
        if not email or not password:
            return jsonify({"message": "Todos los campos son obligatorios", "status": 200}), 200
        
        user = next((user for user in users if user["email"] == email), None)
        if user and check_password_hash(user["password"] == password, password):
            token = jwt(user["id"])
            return jsonify({"token": token.decode()}), 200
        else: 
            return jsonify({"message": "Credenciales inválidas", "status": 401}), 401
    except Exception as e:
        print("Ha ocurrido un error: {}".format(str(e)))
        