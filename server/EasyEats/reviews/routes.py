from datetime import datetime
from flask import Blueprint, request, jsonify
from flask_cors import CORS
from .schemas import recipe_review_schema
from .sql_strings import Sql_Strings as SQL_STRINGS
from EasyEats.config.conf_maria import query, sql
from EasyEats.utils.misc import val_req_data


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
        result = query(SQL_STRINGS.QRY_REVIEWS)
        if result["status"] == "OK":
            print(result["data"])
            respose = {
                "message": "OK",
                "status": 200,
                "data": result["data"]
            }
            return jsonify(respose), 200
        elif result["status"] == "NOT_FOUND":
            respose = {
                "message": "No hay resultados",
                "status": 200,
            }
            return jsonify(respose), 200
        else:
            respose = {
                "message": "Error inesperado en el servidor",
                "status": 500
            }
            return jsonify(respose), 500
    except Exception as e:
        print("Ha ocurrido un error en @get_reviews/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
        respose = {
            "message": "Error inesperado en el servidor",
            "status": 500
        }
        return jsonify(respose), 500
    

@mod.route('/reviews', methods=['POST'])
def save_review():
    try:
        data = request.get_json()
        
        # * Getting values from request
        id_user = int(data["id_user"])
        id_recipe = int(data["id_recipe"])
        rating = float(data["rating"])
        comment = data["comment"] if data["comment"] != "" else None
        
        if not id_recipe \
        or not id_user \
        or not rating:
            return jsonify({"message": "Faltan campos obligatorios", "status": 400}), 200
        
        recipe_ingredient = {
            "id_user": id_user,
            "id_recipe": id_recipe,
            "rating": rating,
            "comment": comment
        }
        
        errors = val_req_data(recipe_ingredient, recipe_review_schema)
        if errors:
            print("Error", errors)
            respose = {
                "message": "Error en la valifación de la petición",
                "errors": errors,
                "status": 400
            }
            return jsonify(respose)
        
        result = sql(SQL_STRINGS.SQL_INSERT_REVIEW, (id_recipe, id_user, rating, comment))
        if result['status'] != "OK":
                return jsonify({"message": "Error al registrar la reseña de la receta", "status": 400}), 200
        respose = {
            "message": "Reseña registrado exitosamente!",
            "status": 200
        }
        return jsonify(respose), 200
    except Exception as e:
        print("Ha ocurrido un error en @save_review/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
        respose = {
            "message": "Error inesperado en el servidor",
            "status": 500
        }
        return jsonify(respose), 500