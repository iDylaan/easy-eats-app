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
@mod.route('/recipe_ingredients/<int:id_recipe>', methods=['GET'])
def get_recipe_ingredients(id_recipe):
    try:
        result = query(SQL_STRINGS.QRY_COUNT_RECIPES_BY_ID, id_recipe, True)
        if result["data"]["count"] == 0:
            response = {
                "message": "Receta inexistente",
                "status": 404
            }
            return jsonify(response)
        result = query(SQL_STRINGS.QRY_COUNT_INGREDIENTS_BY_RECIPE_ID, id_recipe, True)
        if result["data"]["count"] == 0:
            response = {
                "message": "No hay ingredientes",
                "status": 404
            }
            return jsonify(response)
        result = query(SQL_STRINGS.QRY_RECIPES_INGREDIENTS, id_recipe, True)
        if result["status"] == "OK":
            result["data"]["ingredients"] = eval(result["data"]["ingredients_raw_str"])
                
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
        amount = int(data["amount"])
        type_amount = data["type_amount"]
        id_recipe = int(data["id_recipe"])
        id_ingredient = int(data["id_ingredient"])
        
        if not id_recipe \
        or not id_ingredient \
        or not amount \
        or not type_amount:
            return jsonify({"message": "Faltan campos obligatorios", "status": 400}), 200
        
        recipe_ingredient = {
            "amount": amount,
            "type_amount": type_amount,
            "id_recipe": id_recipe,
            "id_ingredient": id_ingredient
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
        
        result = sql(SQL_STRINGS.SQL_INSERT_RECIPE_INGREDIENT, (amount, type_amount, id_recipe, id_ingredient))
        if result['status'] != "OK":
                return jsonify({"message": "Error al registrar el ingrediente de la receta", "status": 400}), 200
        respose = {
            "message": "Ingrediente registrado exitosamente!",
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
    
    
@mod.route('/recipe_ingredients/<int:id_recipe>/<int:id_ingredient>', methods=["DELETE"])
def delete_recipe_ingredients(id_recipe, id_ingredient):
    try:
        result = query(SQL_STRINGS.QRY_COUNT_RECIPE_INGREDIENT_BY_ID, (id_recipe, id_ingredient), True)
        if result["status"] == "NOT_FOUND":
            respose = {
                "message": "Ingrediente de la receta no encontrado",
                "status": 404,
            }
            return jsonify(respose), 404
        if result["data"]["count"] == 0:
            respose = {
                "message": "Ingrediente de la receta no encontrado",
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

        response = sql(SQL_STRINGS.SQL_DELETE_RECIPE_INGREDIENT, (id_recipe, id_ingredient))
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