import traceback
from datetime import datetime
from flask import Blueprint, request, jsonify
from flask_cors import CORS
from .schemas import user_schema
from werkzeug.security import generate_password_hash, check_password_hash
from .sql_strings import Sql_Strings as SQL_STRINGS
from EasyEats.config.conf_maria import query
from EasyEats.utils.misc import gen_jwt, val_req_data


# MODULE
mod = Blueprint('login_signin', __name__, 
    template_folder='templates', 
    static_folder='static', 
    static_url_path='/%s' % __name__
)


# CORS acces to "login_signin"
CORS(mod)

# CORS Configure Parameters
@mod.route('/login', methods=['OPTIONS'])
def handle_options():
    return "", 200, {
        "Access-Control-Allow-Origin": "*", # "*"
        "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE",
        "Access-Control-Allow-Headers": "Content-Type, Authorization"
    }


# =========== ROUTES ===========
@mod.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        email = data.get('email', None)
        password = data.get('password', None)
        
        if not email or not password:
            return jsonify({"message": "Todos los campos son obligatorios", "status": 400}), 200
        
        users = query(SQL_STRINGS.QRY_USERS)
        user = [user for user in users['data'] if user['email'] == email]
        
        if not user:
            return jsonify({"message": "Credenciales invalidas", "status": 401}), 200
        user = user[0]
        if not check_password_hash(user["password"], password):
            return jsonify({"message": "Credenciales invalidas", "status": 401}), 200
        
        username = user["username"]
        tagline = user["tagline"]
        token = gen_jwt(user["id"], user["id_rol"])
        response = {
            "username": username,
            "tagline": tagline,
            "token": token,
        }
        return jsonify(response), 200
    except Exception as e:
        print("Ha ocurrido un error en @login/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
        

# =========== FUNCTIONS ===========
def validate_user_exist(username, tagline):
    try:
        cnt_users = query(SQL_STRINGS.COUNT_USERS, (username, tagline), True)
        if cnt_users["status"] != "OK":
            raise Exception("Error en la consulta de usuarios a la base de datos en @validate_email_exist")
        return (bool(int(cnt_users['data']['conteo'])))
    except Exception as e:
        print("Ha ocurrido el siguiente error en @validate_user_exist/{}".format(e))
        return None

def validate_email_exist(email):
    try:
        cnt_emails = query(SQL_STRINGS.COUNT_EMAILS, (email), True)
        if cnt_emails["status"] != "OK":
            raise Exception("Error en la consulta de emails a la base de datos en @validate_email_exist")
        return bool(int(cnt_emails['data']['conteo']))
    except Exception as e:
        print("Ha ocurrido el siguiente error en @validate_email_exist/{}".format(e))
        return None        