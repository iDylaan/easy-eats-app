from flask import Blueprint, request, jsonify, Response
from flask_cors import CORS
from .schemas import favorite_recipe_schema
from .sql_strings import Sql_Strings as SQL_STRINGS
from EasyEats.config.conf_maria import query, sql
from EasyEats.utils.misc import val_req_data


# MODULE
mod = Blueprint('favorite_recipes', __name__, 
    template_folder='templates', 
    static_folder='static', 
    static_url_path='/%s' % __name__
)
# CORS acces to "favorite_recipes"
CORS(mod)

# CORS Configure Parameters
@mod.route('/favorite_recipes', methods=['OPTIONS'])
def handle_options():
    return "", 200, {
        "Access-Control-Allow-Origin": "*", # "*"
        "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE",
        "Access-Control-Allow-Headers": "Content-Type, Authorization"
    }


# =========== ROUTES ===========
@mod.route('/favorite_recipes/<int:id_user>', methods=['GET'])
def get_favorite_recipes(id_user):
    try:
        result = query(SQL_STRINGS.QRY_FAVORITE_RECIPES_BY_USER_ID, id_user)
        if result["status"] == "OK":
            favorite_recipes = [dict(row) for row in result["data"]]
            
            respose = {
                "message": "OK",
                "status": 200,
                "data": favorite_recipes
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
        print("Ha ocurrido un error en @get_favorite_recipes/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
        respose = {
            "message": "Error inesperado en el servidor",
            "status": 500
        }
        return jsonify(respose), 500
    

@mod.route('/favorite_recipes', methods=['POST'])
def save_favorite_recipe():
    try:
        data = request.get_json()
        
        # * Getting values from request
        id_recipe = int(data["id_recipe"])
        id_user = int(data["id_user"])
        
        if not id_recipe \
        or not id_user:
            return jsonify({"message": "Faltan campos obligatorios", "status": 400}), 200
        
        favorite_recipe = {
            'id_recipe': id_recipe,
            'id_user': id_user
        }
        
        errors = val_req_data(favorite_recipe, favorite_recipe_schema)
        if errors:
            print("Error", errors)
            respose = {
                "message": "Error en la valifación de la petición", 
                "errors": errors,
                "status": 400
            }
            return jsonify(respose)
        
        result = query(SQL_STRINGS.QRY_COUNT_FAVORITE_RECIPES_BY_IDS, (id_user, id_recipe), True)
        if int(result["data"]["count"]) != 0:
            respose = {
                "message": "Esa receta ya está en favoritas",
                "status": 400
            }
            return jsonify(respose)

        result = sql(SQL_STRINGS.SQL_INSERT_FAVORITE_RECIPE, (id_user, id_recipe))
        if result['status'] != "OK":
                return jsonify({"message": "Error al registrar la receta en favoritos", "status": 400}), 200
        respose = {
            "message": "Receta registrada en favoritos exitosamente!",
            "status": 200
        }
        return jsonify(respose), 200
    except Exception as e:
        print("Ha ocurrido un error en @save_favorite_recipe/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
        respose = {
            "message": "Error inesperado en el servidor",
            "status": 500
        }
        return jsonify(respose), 500
    
    
@mod.route('/favorite_recipes/<int:id_recipe>/<int:id_user>', methods=['DELETE'])
def delete_favorite_recipe(id_user, id_recipe):
    try:
        result = query(SQL_STRINGS.QRY_COUNT_RECIPES_BY_ID, id_recipe, True)
        if result["data"]["count"] == 0:
            response = {
                "message": "Receta inexistente",
                "status": 404
            }
            return jsonify(response)
        result = query(SQL_STRINGS.QRY_COUNT_USERS_BY_ID, id_user, True)
        if result["data"]["count"] == 0:
            response = {
                "message": "Usuario inexistente",
                "status": 404
            }
            return jsonify(response)
        
        result = query(SQL_STRINGS.QRY_COUNT_FAVORITE_RECIPES_BY_IDS, (id_user, id_recipe), True)
        if result["status"] == "NOT_FOUND":
            respose = {
                "message": "Esa receta no está en favoritas",
                "status": 404,
            }
            return jsonify(respose), 404
        elif result["status"] != "OK":
            respose = {
                "message": "Error inesperado en el servidor",
                "status": 500,
                "data": None
            }
            return jsonify(respose), 500
        
        elif result["status"] != "OK":
            respose = {
                "message": "Error inesperado en el servidor",
                "status": 500,
                "data": None
            }
            return jsonify(respose), 500

        response = sql(SQL_STRINGS.SQL_DELETE_FAVORITE_RECIPE, (id_recipe, id_user))
        if response["status"] != "OK":
            return jsonify({"message": "Error al borrar el la categoría de la receta", "status": 500}), 500
        return jsonify({"message": "Categoría eliminada correctamente", "status": 200}), 200
    except Exception as e:
        print("Ha ocurrido un error en @delete_recipe_categories/{}".format(e))
        respose = {
            "message": "Error inesperado en el servidor",
            "status": 500
        }
        return jsonify(respose), 500