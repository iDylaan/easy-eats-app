from flask import Blueprint, request, jsonify, Response
from flask_cors import CORS
from .schemas import recipe_utensil_schema
from .sql_strings import Sql_Strings as SQL_STRINGS
from EasyEats.config.conf_maria import query, sql
from EasyEats.utils.misc import val_req_data


# MODULE
mod = Blueprint('recipe_utensils', __name__, 
    template_folder='templates', 
    static_folder='static', 
    static_url_path='/%s' % __name__
)
# CORS acces to "users"
CORS(mod)

# CORS Configure Parameters
@mod.route('/recipe_utensils', methods=['OPTIONS'])
def handle_options():
    return "", 200, {
        "Access-Control-Allow-Origin": "*", # "*"
        "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE",
        "Access-Control-Allow-Headers": "Content-Type, Authorization"
    }



# =========== ROUTES =========== #
@mod.route('/recipe_utensils', methods=['GET'])
def get_recipes_utensils():
    try:
        result = query(SQL_STRINGS.QRY_RECIPES_UTENSILS)
        if result["status"] == "OK":
            for row in result["data"]:
                row["utensils"] = eval(row["utensils"])
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
        print("Ha ocurrido un error en @get_recipes_utensils/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
        respose = {
            "message": "Error inesperado en el servidor",
            "status": 500
        }
        return jsonify(respose), 500
    
    
@mod.route('/recipe_utensils/<int:id_recipe>', methods=['GET'])
def get_recipe_utensils(id_recipe):
    try:
        result = query(SQL_STRINGS.QRY_COUNT_RECIPES_BY_ID, id_recipe, True)
        if result["data"]["count"] == 0:
            response = {
                "message": "Receta inexistente",
                "status": 404
            }
            return jsonify(response)
        result = query(SQL_STRINGS.QRY_RECIPE_UTENSILS, id_recipe, True)
        if result["status"] == "OK":
            result["data"]["utensils"] = eval(result["data"]["utensils"])
                
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
        print("Ha ocurrido un error en @get_recipe_utensils/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
        respose = {
            "message": "Error inesperado en el servidor",
            "status": 500
        }
        return jsonify(respose), 500


@mod.route('/recipe_utensils', methods=['POST'])
def save_recipe_utensil():
    try:
        data = request.get_json()
        
        # * Getting values from request
        id_recipe = int(data["id_recipe"])
        id_utensil = int(data["id_utensil"])
        
        if not id_recipe \
        or not id_utensil:
            return jsonify({"message": "Faltan campos obligatorios", "status": 400}), 200
        
        recipe_utensil = {
            "id_recipe": id_recipe,
            "id_utensil": id_utensil
        }
        
        errors = val_req_data(recipe_utensil, recipe_utensil_schema)
        if errors:
            print("Error", errors)
            respose = {
                "message": "Error en la valifación de la petición",
                "errors": errors,
                "status": 400
            }
            return jsonify(respose)
        
        result = sql(SQL_STRINGS.SQL_INSERT_RECIPE_UTENSIL, (id_recipe, id_utensil))
        if result['status'] != "OK":
                return jsonify({"message": "Error al registrar el ingrediente de la receta", "status": 400}), 200
        respose = {
            "message": "Utensilio registrado exitosamente en la receta!",
            "status": 200
        }
        return jsonify(respose), 200
    except Exception as e:
        print("Ha ocurrido un error en @save_recipe_utensil/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
        respose = {
            "message": "Error inesperado en el servidor",
            "status": 500
        }
        return jsonify(respose), 500
    
    
@mod.route('/recipe_utensils/<int:id_recipe>/<int:id_utensil>', methods=["DELETE"])
def delete_recipe_utensils(id_recipe, id_utensil):
    try:
        result = query(SQL_STRINGS.QRY_COUNT_RECIPE_UTENSIL_BY_ID, (id_recipe, id_utensil), True)
        if result["status"] == "NOT_FOUND":
            respose = {
                "message": "Utensilio de la receta no encontrado",
                "status": 404,
            }
            return jsonify(respose), 404
        if result["data"]["count"] == 0:
            respose = {
                "message": "Utensilio de la receta no encontrado",
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

        response = sql(SQL_STRINGS.SQL_DELETE_RECIPE_UTENSIL, (id_recipe, id_utensil))
        if response["status"] != "OK":
            return jsonify({"message": "Error al borrar el el utensilio de la receta", "status": 500}), 500
        return jsonify({"message": "Utensilio eliminado correctamente de la receta", "status": 200}), 200
    except Exception as e:
        print("Ha ocurrido un error en @delete_recipe_utensils/{}".format(e))
        respose = {
            "message": "Error inesperado en el servidor",
            "status": 500
        }
        return jsonify(respose), 500