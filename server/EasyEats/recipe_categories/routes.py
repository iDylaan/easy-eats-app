import json
from flask import Blueprint, request, jsonify, Response
from flask_cors import CORS
from .schemas import recipe_category_schema
from .sql_strings import Sql_Strings as SQL_STRINGS
from EasyEats.config.conf_maria import query, sql
from EasyEats.utils.misc import val_req_data


# MODULE
mod = Blueprint('recipe_categories', __name__, 
    template_folder='templates', 
    static_folder='static', 
    static_url_path='/%s' % __name__
)
# CORS acces to "users"
CORS(mod)

# CORS Configure Parameters
@mod.route('/recipe_categories', methods=['OPTIONS'])
def handle_options():
    return "", 200, {
        "Access-Control-Allow-Origin": "*", # "*"
        "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE",
        "Access-Control-Allow-Headers": "Content-Type, Authorization"
    }


# =========== ROUTES ===========
@mod.route('/recipe_categories', methods=['GET'])
def get_recipe_categories():
    try:
        result = query(SQL_STRINGS.QRY_ALL_CATEGORIES)
        if result["status"] == "OK":
            recipe_categories = [dict(row) for row in result["data"]]
            for d in recipe_categories:
                d["categories"] = d["categories"].split(",")
            respose = {
                "message": "OK",
                "status": 200,
                "data": recipe_categories
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
        print("Ha ocurrido un error en @get_recipe_categories/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
        respose = {
            "message": "Error inesperado en el servidor",
            "status": 500
        }
        return jsonify(respose), 500


@mod.route('/recipe_categories/<int:id>', methods=['GET'])
def get_recipe_category(id):
    try:
        result = query(SQL_STRINGS.QRY_CATEGORIES_BY_RECIPE_ID, id, True)
        if result["status"] == "OK":
            data = result["data"]
            data["categories"] = data["categories"].split(",")
            respose = {
                "message": "OK",
                "status": 200,
                "data": data
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
        print("Ha ocurrido un error en @get_recipe_categories/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
        respose = {
            "message": "Error inesperado en el servidor",
            "status": 500
        }
        return jsonify(respose), 500


@mod.route('/recipe_categories', methods=['POST'])
def save_recipe_category():
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
            
            errors = val_req_data(recipe_category, recipe_category_schema)
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
            "message": "Categoria/s registrada/s exitosamente!",
            "status": 200
        }
        return jsonify(respose), 200
    except Exception as e:
        print("Ha ocurrido un error en @get_recipe_categories/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
        respose = {
            "message": "Error inesperado en el servidor",
            "status": 500
        }
        return jsonify(respose), 500
    
    
@mod.route('/recipe_categories/<int:id_recipe>/<int:id_category>', methods=["DELETE"])
def delete_recipe_categories(id_recipe, id_category):
    try:
        result = query(SQL_STRINGS.QRY_CATEGORIES_BY_RECIPE_ID, id_recipe, True)
        if result["status"] == "NOT_FOUND":
            respose = {
                "message": "Receta no encontrada",
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
        
        result = query(SQL_STRINGS.QRY_CATEGORY_BY_ID, id_category, True)
        if result["status"] == "NOT_FOUND":
            respose = {
                "message": "Categoría no encontrada",
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

        response = sql(SQL_STRINGS.SQL_DELETE_RECIPE_CATEGORY, (id_recipe, id_category))
        if response["status"] != "OK":
            return jsonify({"message": "Error al borrar el la categoría de la receta", "status": 500}), 500
        return jsonify({"message": "Categoría eliminada correctamente", "status": 200}), 200
    except Exception as e:
        print("Ha ocurrido un error en @delete_ingredient/{}".format(e))
        respose = {
            "message": "Error inesperado en el servidor",
            "status": 500
        }
        return jsonify(respose), 500