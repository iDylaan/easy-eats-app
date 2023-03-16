from flask import Blueprint, request, jsonify, Response
from flask_cors import CORS
from .schemas import recipe_schema
from .sql_strings import Sql_Strings as SQL_STRINGS
from EasyEats.config.conf_maria import query, sql
from EasyEats.utils.misc import val_req_data


# MODULE
mod = Blueprint('recipes', __name__, 
    template_folder='templates', 
    static_folder='static', 
    static_url_path='/%s' % __name__
)
# CORS acces to "recipes"
CORS(mod)

# CORS Configure Parameters
@mod.route('/recipes', methods=['OPTIONS'])
def handle_options():
    return "", 200, {
        "Access-Control-Allow-Origin": "*", # "*"
        "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE",
        "Access-Control-Allow-Headers": "Content-Type, Authorization"
    }


# =========== ROUTES ===========
@mod.route('/recipes', methods=['GET'])
def get_recipes():
    try:
        result = query(SQL_STRINGS.QRY_RECIPES)
        if result["status"] == "OK":
            recipes_dict = [dict(row) for row in result["data"]]
            respose = {
                "message": "OK",
                "status": 200,
                "data": recipes_dict
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
        print("Ha ocurrido un error en @get_recipes/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
        respose = {
            "message": "Error inesperado en el servidor",
            "status": 500
        }
        return jsonify(respose), 500
    
@mod.route('/recipes/<int:id>', methods=["GET"])
def get_recipe(id):
    try:
        result = query(SQL_STRINGS.QRY_RECIPE, id, True)
        if result["status"] == "OK":
            respose = {
                "message": "OK",
                "status": 200,
                "data": result["data"]
            }
            return jsonify(respose), 200
        elif result["status"] == "NOT_FOUND":
            respose = {
                "message": "Receta no encontrado",
                "status": 404,
            }
            return jsonify(respose), 404
        else:
            respose = {
                "message": "Error inesperado en el servidor",
                "status": 500,
                "data": None
            }
            return jsonify(respose), 500
    except Exception as e:
        print("Ha ocurrido un error en @get_recipe/{}".format(e))
        
        
@mod.route('/recipes', methods=["POST"])
def save_recipe():
    try:
        data = request.get_json()
        
        # * Validating null values
        name = data.get("name", None)
        description = data.get("description", None)
        cooking_time = data.get("cooking_time", None)
        dinners = data.get("dinners", None)
        image = data.get("image", None)
        calories = data.get("calories", None)
        fats = data.get("fats", None)
        carbs = data.get("carbs", None)
        protein = data.get("protein", None)
        satured_fats = data.get("satured_fats", None)
        sodium = data.get("sodium", None)
        fiber = data.get("fiber", None)
        sugars = data.get("sugars", None)
        budget = data.get("budget", None)
        id_user = data.get("id_user", None)
        
        if not name \
        or not description \
        or not cooking_time \
        or not dinners \
        or not id_user:
            return jsonify({"message": "Faltan campos obligatorios", "status": 400}), 200

        # TODO: Validar imagen almacenarla y guardarla en la db con su nombre
        
        if data:
            
            recipe = {
                'name': name,
                'description': description,
                'cooking_time': cooking_time,
                'dinners': dinners,
                'image': image,
                'calories': calories,
                'fats': fats,
                'carbs': carbs,
                'protein': protein,
                'satured_fats': satured_fats,
                'sodium': sodium,
                'fiber': fiber,
                'sugars': sugars,
                'budget': budget,
                'id_user': id_user
            }
            
            errors = val_req_data(recipe, recipe_schema)
            if errors:
                print("Error", errors)
                respose = {
                    "message": "Error en la valifación de la petición",
                    "errors": errors,
                    "status": 400,
                    "data": None
                }
                return jsonify(respose)
        
            result = sql(SQL_STRINGS.SQL_INSERT_RECIPE, (
                name,
                description,
                cooking_time,
                dinners,
                image,
                calories,
                fats,
                carbs,
                protein,
                satured_fats,
                sodium,
                fiber,
                sugars,
                budget,
                id_user,
            ))
            if result['status'] != "OK":
                return jsonify({"message": "Error al crear la receta", "status": 400}), 200
            respose = {
                "message": "Receta creada correctamente!",
                "status": 200,
            }
            return jsonify(respose), 200
        else: 
            return jsonify({
                "message": "Error en la petición",
                "status": 400,
                "data": None
            }), 400
    except Exception as e:
        print("Ha ocurrido un error en @save_recipe/{}".format(e))
        return jsonify({
            "message": "Error inesperado en el servidor",
            "status": 500
        }), 500
        
        
@mod.route('/recipes/<int:id_recipe>', methods=["PUT"])
def update_recipe(id_recipe):
    try:
        result = query(SQL_STRINGS.QRY_RECIPE, id_recipe, True)
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
            }
            return jsonify(respose), 500
        
        
        data = request.get_json()
        
        # * Validating null values
        name = data.get("name", None)
        description = data.get("description", None)
        cooking_time = data.get("cooking_time", None)
        dinners = data.get("dinners", None)
        image = data.get("image", None)
        calories = data.get("calories", None)
        fats = data.get("fats", None)
        carbs = data.get("carbs", None)
        protein = data.get("protein", None)
        satured_fats = data.get("satured_fats", None)
        sodium = data.get("sodium", None)
        fiber = data.get("fiber", None)
        sugars = data.get("sugars", None)
        budget = data.get("budget", None)
        id_user = data.get("id_user", None)
        
        if not name \
        or not id_recipe \
        or not description \
        or not cooking_time \
        or not dinners \
        or not id_user:
            return jsonify({"message": "Faltan campos obligatorios", "status": 400}), 200
        
        # TODO: Validar imagen almacenarla y guardarla en la db con su nombre
        
        if data:
            
            recipe = {
                'id': id_recipe,
                'name': name,
                'description': description,
                'cooking_time': cooking_time,
                'dinners': dinners,
                'image': image,
                'calories': calories,
                'fats': fats,
                'carbs': carbs,
                'protein': protein,
                'satured_fats': satured_fats,
                'sodium': sodium,
                'fiber': fiber,
                'sugars': sugars,
                'budget': budget,
                'id_user': id_user
            }
            
            errors = val_req_data(recipe, recipe_schema)
            if errors:
                print("Error", errors)
                respose = {
                    "message": "Error en la valifación de la petición",
                    "errors": errors,
                    "status": 400,
                }
                return jsonify(respose)
        
            result = sql(SQL_STRINGS.SQL_UPDATE_RECIPE, (
                name,
                description,
                cooking_time,
                dinners,
                image,
                calories,
                fats,
                carbs,
                protein,
                satured_fats,
                sodium,
                fiber,
                sugars,
                budget,
                id_user,
                id_recipe
            ))
            if result['status'] != "OK":
                return jsonify({"message": "Error al actualizar la receta", "status": 400}), 200
            respose = {
                "message": "Receta actualizada correctamente!",
                "status": 200,
            }
            return jsonify(respose), 200
        else: 
            return jsonify({
                "message": "Error en la petición",
                "status": 400,
                "data": None
            }), 400
    except Exception as e:
        print("Ha ocurrido un error en @update_recipe/{}".format(e))
        return jsonify({
            "message": "Error inesperado en el servidor",
            "status": 500,
            "data": None
        }), 500
        
    
@mod.route('/recipes/<int:id_recipe>', methods=["DELETE"])
def delete_recipe(id_recipe):
    try:
        result = query(SQL_STRINGS.QRY_RECIPE, id_recipe, True)
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
            }
            return jsonify(respose), 500
        if result['data']['banned'] != 0:
            response = {
                "message": "Esa receta ya fue dada de baja",
                "status": 400
            }
            return jsonify(response), 200
        
        response = sql(SQL_STRINGS.SQL_DELETE_RECIPE, id_recipe)
        if response["status"] != "OK":
            return jsonify({"message": "Error al borrar la receta", "status": 500}), 500
        return jsonify({"message": "Receta dada de baja correctamente", "status": 200}), 200
    except Exception as e:
        print("Ha ocurrido un error en @delete_user/{}".format(e))
        respose = {
            "message": "Error inesperado en el servidor",
            "status": 500
        }
        return jsonify(respose), 500