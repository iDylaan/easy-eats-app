import json
from flask import Blueprint, request, jsonify, Response
from flask_cors import CORS
from .sql_strings import Sql_Strings as SQL_STRINGS


# MODULE
mod = Blueprint('reviews', __name__, 
    template_folder='templates', 
    static_folder='static', 
    static_url_path='/%s' % __name__
)
# CORS acces to "users"
CORS(mod)

# CORS Configure Parameters
@mod.route('/reviews', methods=['OPTIONS'])
def handle_options():
    return "", 200, {
        "Access-Control-Allow-Origin": "*", # "*"
        "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE",
        "Access-Control-Allow-Headers": "Content-Type, Authorization"
    }


# =========== ROUTES ===========
@mod.route('/reviews', methods=['GET'])
def get_reviews():
    try:
        return jsonify({"message": "Desde @get_reviews"}), 200
    except Exception as e:
        print("Ha ocurrido un error en @get_reviews/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
        respose = {
            "message": "Error inesperado en el servidor",
            "status": 500
        }
        return jsonify(respose), 500