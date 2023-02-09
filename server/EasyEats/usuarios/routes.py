import json
from flask import Blueprint, request, jsonify, Response
from flask_cors import cross_origin, CORS
from cerberus import Validator
from werkzeug.security import generate_password_hash, check_password_hash
from .schemas import user_schema
from .users_demo import users
from .sql_strings import Sql_Strings as SQL_STRINGS
from EasyEats.config.conf_maria import query

# MODULE
mod = Blueprint('usuarios', __name__, 
    template_folder='templates', 
    static_folder='static', 
    static_url_path='/%s' % __name__
)
# CORS acces to "users"
CORS(mod)

# CORS Configure Parameters
@mod.route('/users', methods=['OPTIONS'])
def handle_options():
    return "", 200, {
        "Access-Control-Allow-Origin": "*", # "*"
        "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE",
        "Access-Control-Allow-Headers": "Content-Type"
    }



# Schemas validate
def val_req_data(data, schema): # validate request data
    v = Validator(schema)
    if not v.validate(data):
        return jsonify({"errors": v.errors}), 400
    return None


# =========== ROUTES ===========
@mod.route('/users', methods=["GET"])
def users_list():
    users_dict = {}
    users_json = None
    try:
        result = query(SQL_STRINGS.USERS_LIST)
        if result:
            users_dict = [dict(row) for row in result]
            return jsonify(users_dict)
        else:
            print("No hay resultados")
            return jsonify({"message": "No results"})
    except Exception as e:
        print("Ha ocurrido un error en @users_list/{}".format(e))

@mod.route('/users', methods=['POST'])
def create_user():
    try:
        user_data = request.get_json()

        print(user_data)

        response = {
            "status": "success",
            "message": "Usuario registrado exitosamente.",
            "recived": user_data
        }
        return jsonify(response)

    except Exception as e:
        print("Ha ocurrido el siguiente error: ", e)
        return None

