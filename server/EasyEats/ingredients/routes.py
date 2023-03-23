import json, io
from flask import Blueprint, request, jsonify, Response, send_file
from flask_cors import CORS
from .schemas import ingredient_schema
from werkzeug.utils import secure_filename
from PIL import Image as PILImage
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
                'price': price
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
                name, description, price
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
        
        data = request.get_json()
        
        # * Validating null values
        price = data.get("price", None)
        
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
                'price': price
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
                name, description, price, id
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
    
    
@mod.route("/pic_ingredient/<int:id_ingredient>", methods=["GET"])
def get_pic_ingredient(id_ingredient):
    try:
        result = query(SQL_STRINGS.QRY_INGREDIENT_BY_ID, id_ingredient, True)
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
        
        result = query(SQL_STRINGS.QRY_INGREDIENT_PIC, id_ingredient, True)
        if result["status"] != "OK":
            return jsonify({"message": "Error al obtener la imagen", "status": 500}), 500
        
        if not result["data"]:
            return jsonify({'message': 'Imagen no encontrada', "status": 404}), 404
        
        image_bit = result['data']['image']

        img_io = io.BytesIO(image_bit)
        img_io.seek(0)
        
        return send_file(img_io, mimetype='image/png')
        
    except Exception as e:
        print("Ha ocurrido un error en @get_pic_ingredient/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
        return None
        
    
    
@mod.route("/pic_ingredient/<int:id_ingredient>", methods=["POST"])
def save_pic_ingredient(id_ingredient):
    try:
        result = query(SQL_STRINGS.QRY_INGREDIENT_BY_ID, id_ingredient, True)
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
        
        # * Getting the image
        file = request.files.get('image', None)
        filename = None
        img_byte_arr = None
        if file:
            filename = secure_filename(file.filename)
            image = PILImage.open(file.stream)
            
            img_byte_arr = io.BytesIO()
            image.save(img_byte_arr, format='PNG')
            img_byte_arr = img_byte_arr.getvalue()
            
            response = sql(SQL_STRINGS.SQL_SAVE_PIC_INGREDIENT, (filename, img_byte_arr, id_ingredient))
            if response["status"] != "OK":
                return jsonify({"message": "Error al agregar la imagen", "status": 500}), 200
            
            return jsonify({'message': 'Imagen registrada correctamente', "status": 201}), 201
        return jsonify({'message': 'No se recibio una imagen valida', "status": 400}), 400
    except Exception as e:
        print("Ha ocurrido un error en @save_pic_ingredient/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
        return None
    

# =========== FUNCTIONS =========== #