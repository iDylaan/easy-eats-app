import json
from flask import Blueprint, request, jsonify, Response
from flask_cors import cross_origin, CORS
from cerberus import Validator
from werkzeug.security import generate_password_hash, check_password_hash
from .schemas import user_schema
from .users_demo import users
from .sql_strings import Sql_Strings as SQL_STRINGS
from EasyEats.config.conf_maria import big_query, small_query

# MODULE
mod = Blueprint('usuarios', __name__, 
    template_folder='templates', 
    static_folder='static', 
    static_url_path='/%s' % __name__
)
# CORS acces to "users"
CORS(mod)


# Schemas validate
def val_req_data(data, schema): # validate request data
    v = Validator(schema)
    if not v.validate(data):
        return jsonify({"errors": v.errors}), 400
    return None


# =========== ROUTES ===========
@mod.route('/users_list', methods=["GET", "POST"])
def users_list():
    users_dict = {}
    users_json = None
    try:
        response = small_query(SQL_STRINGS.USERS_LIST)
        # response = query("SELECT (1 + 1)")
        print(response)
        return jsonify({"message": "Ya me canse de que no retorne nada..."}, {"response": response})
        users_dict = [dict(row) for row in response]
        print(users_dict)
        return 'as'
        users_json = json.dumps()
        print(users_json)
    except Exception as e:
        print("Ha ocurrido un error en @users_list/{}".format(e))