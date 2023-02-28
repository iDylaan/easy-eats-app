import json, re
from flask import Blueprint, request, jsonify, Response
from flask_cors import CORS
from .schemas import recipe_ingredient_schema
from .sql_strings import Sql_Strings as SQL_STRINGS
from EasyEats.config.conf_maria import query, sql
from EasyEats.utils.misc import val_req_data


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


# =========== ROUTES =========== #
@mod.route('/recipe_ingredients', methods=['GET'])
def get_recipe_ingredients():
    try:
        result = query(SQL_STRINGS.QRY_RECIPES_INGREDIENTS)
        if result["status"] == "OK":
            recipe_ingredients = [dict(row) for row in result["data"]]
            regex = r"\[(\d+), \s*([A-Za-z]+), \s*([\d\.]+)\]"
            for d in recipe_ingredients:
                ingredients = re.findall(regex, d["ingredients_array"])
                print(ingredients)
                # d["ingredients_array"]
            # for d in recipe_ingredients:
                # d["ingredients_array"] = d["ingredients_array"].split(",")
            respose = {
                "message": "OK",
                "status": 200,
                "data": recipe_ingredients
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
        print("Ha ocurrido un error en @get_recipe_ingredients/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
        respose = {
            "message": "Error inesperado en el servidor",
            "status": 500
        }
        return jsonify(respose), 500


@mod.route('/recipe_ingredients/<int:id>', methods=['GET'])
def get_recipe_ingredient(id):
    try:
        result = query(SQL_STRINGS.QRY_ingredients_BY_RECIPE_ID, id, True)
        if result["status"] == "OK":
            data = result["data"]
            data["ingredients"] = data["ingredients"].split(",")
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
        print("Ha ocurrido un error en @get_recipe_ingredients/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
        respose = {
            "message": "Error inesperado en el servidor",
            "status": 500
        }
        return jsonify(respose), 500


@mod.route('/recipe_ingredients', methods=['POST'])
def save_recipe_ingredient():
    try:
        data = request.get_json()
        
        # * Getting values from request
        id_recipe = int(data["id_recipe"])
        
        if not id_recipe:
            return jsonify({"message": "Faltan campos obligatorios", "status": 400}), 200
        
        id_ingredients = data["ingredients"]
        values_id_ingredients = ""
        for i in range(len(id_ingredients)):
            id_ingredients[i] = int(id_ingredients[i])
            
            recipe_ingredient = {
                'id_recipe': id_recipe,
                'id_category': id_ingredients[i]
            }
            
            errors = val_req_data(recipe_ingredient, recipe_ingredient_schema)
            if errors:
                print("Error", errors)
                respose = {
                    "message": "Error en la valifación de la petición",
                    "errors": errors,
                    "status": 400
                }
                return jsonify(respose)
            
            # * Creating the query
            if i == len(id_ingredients) - 1:
                values_id_ingredients += "({}, {})".format(id_recipe, id_ingredients[i])
            else:
                values_id_ingredients += "({}, {}), ".format(id_recipe, id_ingredients[i])
        result = sql(SQL_STRINGS.SQL_INSERT_recipe_ingredients.format(values_id_ingredients))
        if result['status'] != "OK":
                return jsonify({"message": "Error al registrar las categorias de la receta", "status": 400}), 200
        respose = {
            "message": "Categoria/s registrada/s exitosamente!",
            "status": 200
        }
        return jsonify(respose), 200
    except Exception as e:
        print("Ha ocurrido un error en @get_recipe_ingredients/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
        respose = {
            "message": "Error inesperado en el servidor",
            "status": 500
        }
        return jsonify(respose), 500
    
    
@mod.route('/recipe_ingredients/<int:id_recipe>/<int:id_category>', methods=["DELETE"])
def delete_recipe_ingredients(id_recipe, id_category):
    try:
        result = query(SQL_STRINGS.QRY_ingredients_BY_RECIPE_ID, id_recipe, True)
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

        response = sql(SQL_STRINGS.SQL_DELETE_recipe_ingredient, (id_recipe, id_category))
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