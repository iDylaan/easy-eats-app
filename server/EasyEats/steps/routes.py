from datetime import datetime
from flask import Blueprint, request, jsonify
from flask_cors import CORS
from .schemas import recipe_step_schema
from .sql_strings import Sql_Strings as SQL_STRINGS
from EasyEats.config.conf_maria import query, sql
from EasyEats.utils.misc import val_req_data


# MODULE
mod = Blueprint('steps', __name__, 
    template_folder='templates', 
    static_folder='static', 
    static_url_path='/%s' % __name__
)
# CORS acces to "users"
CORS(mod)

# CORS Configure Parameters
@mod.route('/steps', methods=['OPTIONS'])
def handle_options():
    return "", 200, {
        "Access-Control-Allow-Origin": "*", # "*"
        "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE",
        "Access-Control-Allow-Headers": "Content-Type, Authorization"
    }


# =========== ROUTES ===========
@mod.route('/steps/<int:id_recipe>', methods=['GET'])
def get_steps(id_recipe):
    try:
        result = query(SQL_STRINGS.QRY_RECIPE_EXISTS, id_recipe, True)
        if not int(result["data"]["exists"]):
            respose = {
                "message": "No se encontró la receta indicada",
                "status": 404
            }
            return jsonify(respose), 404
        result = query(SQL_STRINGS.QRY_STEPS_BY_RECIP_ID, id_recipe)
        if result["status"] == "OK":
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
        print("Ha ocurrido un error en @get_steps/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
        respose = {
            "message": "Error inesperado en el servidor",
            "status": 500
        }
        return jsonify(respose), 500
    
    
@mod.route('/steps/<int:id_recipe>', methods=['POST'])
def save_steps(id_recipe):
    try:
        data = request.get_json()
        
        # * Getting values from request
        description = data["description"]
        
        if not id_recipe \
        or not description:
            return jsonify({"message": "Faltan campos obligatorios", "status": 400}), 200
        
        step_ingredient = {
            "description": description,
            "id_recipe": id_recipe
        }
        
        errors = val_req_data(step_ingredient, recipe_step_schema)
        if errors:
            print("Error", errors)
            respose = {
                "message": "Error en la valifación de la petición",
                "errors": errors,
                "status": 400
            }
            return jsonify(respose)
        
        result = sql(SQL_STRINGS.SQL_INSERT_STEP, (description, id_recipe))
        if result['status'] != "OK":
                return jsonify({"message": "Error al registrar el paso de la receta", "status": 400}), 200
        respose = {
            "message": "Paso registrado exitosamente!",
            "status": 200   
        }
        return jsonify(respose), 200
    except Exception as e:
        print("Ha ocurrido un error en @save_step/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
        respose = {
            "message": "Error inesperado en el servidor",
            "status": 500
        }
        return jsonify(respose), 500
    
    
@mod.route('/steps/<int:id_step>', methods=['PUT'])
def update_step(id_step):
    try:
        result = query(SQL_STRINGS.QRY_COUNT_STEP_BY_ID, id_step, True)
        if result["status"] == "NOT_FOUND":
            respose = {
                "message": "Paso no encontrado",
                "status": 404,
            }
            return jsonify(respose), 404
        if result["data"]["count"] == 0:
            respose = {
                "message": "Paso no encontrado",
                "status": 404,
            }
            return jsonify(respose), 404
        
        data = request.get_json()
        
        # * Getting values from request
        description = data["description"]
        
        
        if not id_step \
        or not description:
            return jsonify({"message": "Faltan campos obligatorios", "status": 400}), 200
        
        
        result = sql(SQL_STRINGS.SQL_UPDATE_STEP, (description, id_step))
        if result['status'] != "OK":
                return jsonify({"message": "Error al actualizar el paso de la receta", "status": 400}), 200
        respose = {
            "message": "Paso actualizada exitosamente!",
            "status": 200
        }
        return jsonify(respose), 200
    except Exception as e:
        print("Ha ocurrido un error en @update_step/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
        respose = {
            "message": "Error inesperado en el servidor",
            "status": 500
        }
        return jsonify(respose), 500
    
    
@mod.route('/steps/<int:id_step>', methods=['DELETE'])
def delete_step(id_step):
    try:
        result = query(SQL_STRINGS.QRY_STEP_BY_ID, id_step, True)
        if result["status"] == "NOT_FOUND":
            respose = {
                "message": "Paso no encontrado",
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
        
        result = query(SQL_STRINGS.QRY_STEPS_UP_DELETED, (
            int(result["data"]["step_number"]), 
            int(result["data"]["id_recipe"])
        ))
        if result["status"] != "OK":
            respose = {
                "message": "Error intero en la obtención de pasos en el servidor",
                "status": 500
            }
            return jsonify(respose), 500
        if len(result["data"]) > 0:
            for row in result["data"]:
                result = sql(SQL_STRINGS.SQL_UPDATE_STEP_NUMBER, (int(row["step_number"]) - 1, row["id"]))
                if result["status"] != "OK":
                    return jsonify({"message": "Error interno en la reacomodación de pasos", "status": 500}), 200
        
        response = sql(SQL_STRINGS.SQL_DELETE_STEP, id_step)
        if response["status"] != "OK":
            return jsonify({"message": "Error al borrar el paso", "status": 500}), 500
        return jsonify({"message": "Paso eliminado correctamente", "status": 200}), 200
    except Exception as e:
        print("Ha ocurrido un error en @delete_step/{}".format(e))
        respose = {
            "message": "Error inesperado en el servidor",
            "status": 500
        }
        return jsonify(respose), 500
    