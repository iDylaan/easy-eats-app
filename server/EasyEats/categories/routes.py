import json
from flask import Blueprint, request, jsonify, Response
from flask_cors import CORS
from .schemas import category_schema
from .sql_strings import Sql_Strings as SQL_STRINGS
from EasyEats.config.conf_maria import query, sql
from EasyEats.utils.misc import val_req_data


# MODULE
mod = Blueprint('categories', __name__, 
    template_folder='templates', 
    static_folder='static', 
    static_url_path='/%s' % __name__
)
# CORS acces to "users"
CORS(mod)

# CORS Configure Parameters
@mod.route('/categories', methods=['OPTIONS'])
def handle_options():
    return "", 200, {
        "Access-Control-Allow-Origin": "*", # "*"
        "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE",
        "Access-Control-Allow-Headers": "Content-Type, Authorization"
    }


# =========== ROUTES =========== #
@mod.route('/categories', methods=['GET'])
def get_categories():
    try:
        result = query(SQL_STRINGS.QRY_ALL_CATEGORIES)
        if result["status"] == "OK":
            categories_dict = [dict(row) for row in result["data"]]
            respose = {
                "message": "OK",
                "status": 200,
                "data": categories_dict
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
        return jsonify({"message": "Desde @get_categories"}), 200
    except Exception as e:
        print("Ha ocurrido un error en @get_categories/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
        respose = {
            "message": "Error inesperado en el servidor",
            "status": 500
        }
        return jsonify(respose), 500
    
    
@mod.route('/categories/<int:id>', methods=["GET"])
def get_category(id):
    try:
        result = query(SQL_STRINGS.QRY_CATEGORY_BY_ID, id, True)
        if result["status"] == "OK":
            respose = {
                "message": "OK",
                "status": 200,
                "data": result["data"]
            }
            return jsonify(respose), 200
        elif result["status"] == "NOT_FOUND":
            respose = {
                "message": "Categoría no encontrada",
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
        print("Ha ocurrido un error en @get_category/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
    
    
@mod.route("/categories", methods=["POST"])
def save_category():
    try:
        data = request.get_json()
        
        # * Getting values from request
        name = data["name"].strip()
        
        if not name:
            return jsonify({"message": "Faltan campos obligatorios", "status": 400}), 200
                
        if data:
            category = {
                'name': name
            }
            
            errors = val_req_data(category, category_schema)
            if errors:
                print("Error", errors)
                respose = {
                    "message": "Error en la valifación de la petición",
                    "errors": errors,
                    "status": 400
                }
                return jsonify(respose)
            result = sql(SQL_STRINGS.SQL_CREATE_CATEGORY, ( name ))
            if result['status'] != "OK":
                return jsonify({"message": "Error al registrar la categoría", "status": 400}), 200
            respose = {
                "message": "Categoría registrada exitosamente!",
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
        print("Ha ocurrido un error en @save_category/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
        return jsonify({
            "message": "Error inesperado en el servidor",
            "status": 500,
            "data": None
        }), 500
        

@mod.route('/categories/<int:id>', methods=["PUT"])
def update_category(id):
    try:
        data = request.get_json()
        
        # * Getting values from request
        name = data["name"].strip()
        
        if not name:
            return jsonify({"message": "Faltan campos obligatorios", "status": 400}), 200
                
        if data:
            category = {
                'name': name
            }
            
            errors = val_req_data(category, category_schema)
            if errors:
                print("Error", errors)
                respose = {
                    "message": "Error en la valifación de la petición",
                    "errors": errors,
                    "status": 400
                }
                return jsonify(respose)
            result = sql(SQL_STRINGS.SQL_UPDATE_CATEGORY, ( name, id ))
            if result['status'] != "OK":
                return jsonify({"message": "Error al actulizar la categoría", "status": 400}), 200
            respose = {
                "message": "Categoría actulizada exitosamente!",
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
        print("Ha ocurrido un error en @update_category/{}".format(e))
        return jsonify({
            "message": "Error inesperado en el servidor",
            "status": 500,
            "data": None
        }), 500
        

@mod.route('/categories/<int:id>', methods=["DELETE"])
def delete_category(id):
    try:
        result = query(SQL_STRINGS.QRY_CATEGORY_BY_ID, id, True)
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

        response = sql(SQL_STRINGS.SQL_DELETE_CATEGORY, id)
        if response["status"] != "OK":
            return jsonify({"message": "Error al borrar la categoría", "status": 500}), 500
        return jsonify({"message": "Categoría eliminada correctamente", "status": 200}), 200
    except Exception as e:
        print("Ha ocurrido un error en @delete_category/{}".format(e))
        respose = {
            "message": "Error inesperado en el servidor",
            "status": 500
        }
        return jsonify(respose), 500

# =========== FUNCTIONS =========== #