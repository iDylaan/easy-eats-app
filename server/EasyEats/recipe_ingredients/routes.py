import json
from flask import Blueprint, request, jsonify, Response
from flask_cors import CORS
from .sql_strings import Sql_Strings as SQL_STRINGS


# MODULE
mod = Blueprint('recipe_ingredients', __name__, 
    template_folder='templates', 
    static_folder='static', 
    static_url_path='/%s' % __name__
)
# CORS acces to "users"
CORS(mod)

# CORS Configure Parameters
@mod.route('/recipe_ingredients', methods=['OPTIONS'])
def handle_options():
    return "", 200, {
        "Access-Control-Allow-Origin": "*", # "*"
        "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE",
        "Access-Control-Allow-Headers": "Content-Type, Authorization"
    }


# =========== ROUTES ===========
@mod.route('/recipe_ingredients', methods=['GET'])
def get_recipe_ingredients():
    try:
        return jsonify({"message": "Desde @get_recipe_ingredients"}), 200
    except Exception as e:
        print("Ha ocurrido un error en @get_recipe_ingredients/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
        respose = {
            "message": "Error inesperado en el servidor",
            "status": 500
        }
        return jsonify(respose), 500