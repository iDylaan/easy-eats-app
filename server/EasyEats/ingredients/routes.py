import json
from flask import Blueprint, request, jsonify, Response
from flask_cors import CORS
from .schemas import ingredient_schema
from .sql_strings import Sql_Strings as SQL_STRINGS
from EasyEats.config.conf_maria import query, sql
from EasyEats.utils.misc import val_req_data


# MODULE
mod = Blueprint('ingredients', __name__, 
    template_folder='templates', 
    static_folder='static', 
    static_url_path='/%s' % __name__
)
# CORS acces to "ingredients"
CORS(mod)

# CORS Configure Parameters
@mod.route('/ingredients', methods=['OPTIONS'])
def handle_options():
    return "", 200, {
        "Access-Control-Allow-Origin": "*", # "*"
        "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE",
        "Access-Control-Allow-Headers": "Content-Type, Authorization"
    }


# =========== ROUTES =========== #
@mod.route('/ingredients', methods=['GET'])
def get_ingredients():
    try:
        result = query(SQL_STRINGS.QRY_ALL_INGREDIENTS)
        if result["status"] == "OK":
            ingredients_dict = [dict(row) for row in result["data"]]
            respose = {
                "message": "OK",
                "status": 200,
                "data": ingredients_dict
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
        print("Ha ocurrido un error en @get_ingredients/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
        respose = {
            "message": "Error inesperado en el servidor",
            "status": 500
        }
        return jsonify(respose), 500
    
    
@mod.route('/ingredients/<int:id>', methods=["GET"])
def get_ingredient(id):
    try:
        result = query(SQL_STRINGS.QRY_INGREDIENT_BY_ID, id, True)
        if result["status"] == "OK":
            respose = {
                "message": "OK",
                "status": 200,
                "data": result["data"]
            }
            return jsonify(respose), 200
        elif result["status"] == "NOT_FOUND":
            respose = {
                "message": "Ingrediente no encontrado",
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
        print("Ha ocurrido un error en @get_ingredient/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
    
    
@mod.route("/ingredients", methods=["POST"])
def save_ingredient():
    try:
        data = request.get_json()
        
        # * Validating null values
        price = data.get("price", None)
        image = data.get("image", None)
        
        # * Getting values from request
        name = data["name"].strip()
        description = data["description"].strip()
        
        if not name \
        or not description:
            return jsonify({"message": "Faltan campos obligatorios", "status": 400}), 200
        
        # TODO: Validar imagen almacenarla y guardarla en la db con su nombre
        
        if data:
            ingredient = {
                'name': name,
                'description': description,
                'price': price,
                'image': image
            }
            
            errors = val_req_data(ingredient, ingredient_schema)
            if errors:
                print("Error", errors)
                respose = {
                    "message": "Error en la valifación de la petición",
                    "errors": errors,
                    "status": 400
                }
                return jsonify(respose)
            result = sql(SQL_STRINGS.SQL_CREATE_INGREDIENT, (
                name, description, price, image
            ))
            if result['status'] != "OK":
                return jsonify({"message": "Error al registrar el ingrediente", "status": 400}), 200
            respose = {
                "message": "Ingrediente registrado exitosamente!",
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
        print("Ha ocurrido un error en @save_ingredient/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
        return jsonify({
            "message": "Error inesperado en el servidor",
            "status": 500,
            "data": None
        }), 500
        

@mod.route('/ingredients/<int:id>', methods=["PUT"])
def update_ingredient(id):
    try:
        data = request.get_json()
        
        # * Validating null values
        price = data.get("price", None)
        image = data.get("image", None)
        
        # * Getting values from request
        name = data["name"].strip()
        description = data["description"].strip()
        
        if not name \
        or not description:
            return jsonify({"message": "Faltan campos obligatorios", "status": 400}), 200
        
        # TODO: Validar imagen almacenarla y guardarla en la db con su nombre
        
        if data:
            ingredient = {
                'name': name,
                'description': description,
                'price': price,
                'image': image
            }
            
            errors = val_req_data(ingredient, ingredient_schema)
            if errors:
                print("Error", errors)
                respose = {
                    "message": "Error en la valifación de la petición",
                    "errors": errors,
                    "status": 400
                }
                return jsonify(respose)
            result = sql(SQL_STRINGS.SQL_UPDATE_INGREDIENT, (
                name, description, price, image, id
            ))
            if result['status'] != "OK":
                return jsonify({"message": "Error al actulizar el ingrediente", "status": 400}), 200
            respose = {
                "message": "Ingrediente actulizado exitosamente!",
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
        print("Ha ocurrido un error en @update_ingredient/{}".format(e))
        return jsonify({
            "message": "Error inesperado en el servidor",
            "status": 500,
            "data": None
        }), 500
        

@mod.route('/ingredients/<int:id>', methods=["DELETE"])
def delete_ingredient(id):
    try:
        result = query(SQL_STRINGS.QRY_INGREDIENT_BY_ID, id, True)
        if result["status"] == "NOT_FOUND":
            respose = {
                "message": "Ingrediente no encontrado",
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

        response = sql(SQL_STRINGS.SQL_DELETE_INGREDIENT, id)
        if response["status"] != "OK":
            return jsonify({"message": "Error al borrar el ingrediente", "status": 500}), 500
        return jsonify({"message": "Ingrediente eliminado correctamente", "status": 200}), 200
    except Exception as e:
        print("Ha ocurrido un error en @delete_ingredient/{}".format(e))
        respose = {
            "message": "Error inesperado en el servidor",
            "status": 500
        }
        return jsonify(respose), 500

# =========== FUNCTIONS =========== #