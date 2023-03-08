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
    

@mod.route('/recipe_categories', methods=['POST'])
def save_favorite_recipe():
    try:
        data = request.get_json()
        
        # * Getting values from request
        id_recipe = int(data["id_recipe"])
        
        if not id_recipe:
            return jsonify({"message": "Faltan campos obligatorios", "status": 400}), 200
        
        id_categories = data["categories"]
        values_id_categories = ""
        for i in range(len(id_categories)):
            id_categories[i] = int(id_categories[i])
            
            recipe_category = {
                'id_recipe': id_recipe,
                'id_category': id_categories[i]
            }
            
            errors = val_req_data(recipe_category, favorite_recipe_schema)
            if errors:
                print("Error", errors)
                respose = {
                    "message": "Error en la valifación de la petición", 
                    "errors": errors,
                    "status": 400
                }
                return jsonify(respose)
            
            # * Creating the query
            if i == len(id_categories) - 1:
                values_id_categories += "({}, {})".format(id_recipe, id_categories[i])
            else:
                values_id_categories += "({}, {}), ".format(id_recipe, id_categories[i])
        result = sql(SQL_STRINGS.SQL_INSERT_RECIPE_CATEGORIES.format(values_id_categories))
        if result['status'] != "OK":
                return jsonify({"message": "Error al registrar las categorias de la receta", "status": 400}), 200
        respose = {
            "message": "Categoria registrada exitosamente!",
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
    