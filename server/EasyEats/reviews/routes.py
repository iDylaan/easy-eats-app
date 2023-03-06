from flask import Blueprint, request, jsonify
from flask_cors import CORS
from .schemas import recipe_review_schema
from .sql_strings import Sql_Strings as SQL_STRINGS
from EasyEats.config.conf_maria import query, sql
from EasyEats.utils.misc import val_req_data


# MODULE
mod = Blueprint('reviews', __name__, 
    template_folder='templates', 
    static_folder='static', 
    static_url_path='/%s' % __name__
)
# CORS acces to "users"
CORS(mod)

# CORS Configure Parameters
@mod.route('/reviews', methods=['OPTIONS'])
def handle_options():
    return "", 200, {
        "Access-Control-Allow-Origin": "*", # "*"
        "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE",
        "Access-Control-Allow-Headers": "Content-Type, Authorization"
    }


# =========== ROUTES ===========
@mod.route('/reviews', methods=['GET'])
def get_reviews():
    try:
        result = query(SQL_STRINGS.QRY_REVIEWS)
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
        print("Ha ocurrido un error en @get_reviews/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
        respose = {
            "message": "Error inesperado en el servidor",
            "status": 500
        }
        return jsonify(respose), 500
    

@mod.route('/reviews/<int:id_recipe>', methods=['GET'])
def get_recipe_reviews(id_recipe):
    try:
        result = query(SQL_STRINGS.QRY_RECIPE_EXISTS, id_recipe, True)
        if not int(result["data"]["exists"]):
            respose = {
                "message": "No se encontró la receta indicada",
                "status": 404
            }
            return jsonify(respose), 404
        result = query(SQL_STRINGS.QRY_RECIPE_REVIEWS, (
                '%d-%m-%Y', # ? formato date_made
                '%d-%m-%Y %H:%i', # ? formato datetime_made
                '%H:%i', # ? formato time_made
                id_recipe
            ))
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
        print("Ha ocurrido un error en @get_recipes_reviews/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
        respose = {
            "message": "Error inesperado en el servidor",
            "status": 500
        }
        return jsonify(respose), 500
    

@mod.route('/reviews', methods=['POST'])
def save_review():
    try:
        data = request.get_json()
        
        # * Getting values from request
        id_user = int(data["id_user"])
        id_recipe = int(data["id_recipe"])
        rating = float(data["rating"])
        comment = data["comment"] if data["comment"] != "" else None
        
        if not id_recipe \
        or not id_user \
        or not rating:
            return jsonify({"message": "Faltan campos obligatorios", "status": 400}), 200
        
        recipe_ingredient = {
            "id_user": id_user,
            "id_recipe": id_recipe,
            "rating": rating,
            "comment": comment
        }
        
        errors = val_req_data(recipe_ingredient, recipe_review_schema)
        if errors:
            print("Error", errors)
            respose = {
                "message": "Error en la valifación de la petición",
                "errors": errors,
                "status": 400
            }
            return jsonify(respose)
        
        result = sql(SQL_STRINGS.SQL_INSERT_REVIEW, (id_recipe, id_user, rating, comment))
        if result['status'] != "OK":
                return jsonify({"message": "Error al registrar la reseña de la receta", "status": 400}), 200
        respose = {
            "message": "Reseña registrado exitosamente!",
            "status": 200
        }
        return jsonify(respose), 200
    except Exception as e:
        print("Ha ocurrido un error en @save_review/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
        respose = {
            "message": "Error inesperado en el servidor",
            "status": 500
        }
        return jsonify(respose), 500
    
    
@mod.route('/reviews/<int:id_review>', methods=['PUT'])
def update_review(id_review):
    try:
        result = query(SQL_STRINGS.QRY_COUNT_REVIEWS_BY_ID, id_review, True)
        if result["status"] == "NOT_FOUND":
            respose = {
                "message": "Reseña no encontrada",
                "status": 404,
            }
            return jsonify(respose), 404
        if result["data"]["count"] == 0:
            respose = {
                "message": "Reseña no encontrada",
                "status": 404,
            }
            return jsonify(respose), 404
        
        data = request.get_json()
        
        # * Getting values from request
        id_user = int(data["id_user"])
        id_recipe = int(data["id_recipe"])
        rating = float(data["rating"])
        comment = data["comment"] if data["comment"] != "" else None
        
        if not id_recipe \
        or not id_user \
        or not rating:
            return jsonify({"message": "Faltan campos obligatorios", "status": 400}), 200
        
        recipe_ingredient = {
            "id_user": id_user,
            "id_recipe": id_recipe,
            "rating": rating,
            "comment": comment
        }
        
        errors = val_req_data(recipe_ingredient, recipe_review_schema)
        if errors:
            print("Error", errors)
            respose = {
                "message": "Error en la valifación de la petición",
                "errors": errors,
                "status": 400
            }
            return jsonify(respose)
        
        result = sql(SQL_STRINGS.SQL_UPDATE_REVIEW, (id_recipe, id_user, rating, comment, id_review))
        if result['status'] != "OK":
                return jsonify({"message": "Error al actualizar la reseña de la receta", "status": 400}), 200
        respose = {
            "message": "Reseña actualizada exitosamente!",
            "status": 200
        }
        return jsonify(respose), 200
    except Exception as e:
        print("Ha ocurrido un error en @update_review/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
        respose = {
            "message": "Error inesperado en el servidor",
            "status": 500
        }
        return jsonify(respose), 500
    
    
# TODO: Cambiar a baja logica
@mod.route('/reviews/<int:id_review>', methods=['DELETE'])
def delete_review(id_review):
    try:
        result = query(SQL_STRINGS.QRY_COUNT_REVIEWS_BY_ID, id_review, True)
        if result["status"] == "NOT_FOUND":
            respose = {
                "message": "Reseña no encontrada",
                "status": 404,
            }
            return jsonify(respose), 404
        if result["data"]["count"] == 0:
            respose = {
                "message": "Reseña no encontrada",
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

        response = sql(SQL_STRINGS.SQL_DELETE_REVIEW, id_review)
        if response["status"] != "OK":
            return jsonify({"message": "Error al borrar la reseña", "status": 500}), 500
        return jsonify({"message": "Reseña eliminada correctamente", "status": 200}), 200
    except Exception as e:
        print("Ha ocurrido un error en @delete_review/{}".format(e))
        respose = {
            "message": "Error inesperado en el servidor",
            "status": 500
        }
        return jsonify(respose), 500
    