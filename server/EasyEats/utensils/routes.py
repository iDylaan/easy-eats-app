import io
from flask import Blueprint, request, jsonify, Response, send_file
from flask_cors import CORS
from .schemas import utensil_schema
from werkzeug.utils import secure_filename
from PIL import Image as PILImage
from .sql_strings import Sql_Strings as SQL_STRINGS
from EasyEats.config.conf_maria import query, sql
from EasyEats.utils.misc import val_req_data


# MODULE
mod = Blueprint('utensils', __name__, 
    template_folder='templates', 
    static_folder='static', 
    static_url_path='/%s' % __name__
)
# CORS acces to "users"
CORS(mod)

# CORS Configure Parameters
@mod.route('/utensils', methods=['OPTIONS'])
def handle_options():
    return "", 200, {
        "Access-Control-Allow-Origin": "*", # "*"
        "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE",
        "Access-Control-Allow-Headers": "Content-Type, Authorization"
    }


# =========== ROUTES =========== #
@mod.route('/utensils', methods=['GET'])
def get_utensils():
    try:
        result = query(SQL_STRINGS.QRY_ALL_UTENSILS)
        if result["status"] == "OK":
            utensils_dict = [dict(row) for row in result["data"]]
            respose = {
                "message": "OK",
                "status": 200,
                "data": utensils_dict
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
        print("Ha ocurrido un error en @get_utensils/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
        respose = {
            "message": "Error inesperado en el servidor",
            "status": 500
        }
        return jsonify(respose), 500
    
    
@mod.route('/utensils/<int:id>', methods=["GET"])
def get_utensil(id):
    try:
        result = query(SQL_STRINGS.QRY_UTENSIL_BY_ID, id, True)
        if result["status"] == "OK":
            respose = {
                "message": "OK",
                "status": 200,
                "data": result["data"]
            }
            return jsonify(respose), 200
        elif result["status"] == "NOT_FOUND":
            respose = {
                "message": "Utensilio no encontrado",
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
        print("Ha ocurrido un error en @get_utensil/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
        respose = {
            "message": "Error inesperado en el servidor",
            "status": 500
        }
        return jsonify(respose), 500
    
    
@mod.route("/utensils", methods=["POST"])
def save_utensil():
    try:
        data = request.get_json()
        
        # * Getting values from request
        name = data["name"].strip()
        
        if not name:
            return jsonify({"message": "Faltan campos obligatorios", "status": 400}), 200
        
        # TODO: Validar imagen almacenarla y guardarla en la db con su nombre
        
        if data:
            utensil = {
                'name': name
            }
            
            errors = val_req_data(utensil, utensil_schema)
            if errors:
                print("Error", errors)
                respose = {
                    "message": "Error en la valifación de la petición",
                    "errors": errors,
                    "status": 400
                }
                return jsonify(respose)
            result = sql(SQL_STRINGS.SQL_CREATE_UTENSIL, name)
            if result['status'] != "OK":
                return jsonify({"message": "Error al registrar el utensilio", "status": 400}), 200
            respose = {
                "message": "Utensilio registrado exitosamente!",
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
        print("Ha ocurrido un error en @save_utensil/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
        return jsonify({
            "message": "Error inesperado en el servidor",
            "status": 500
        }), 500
        

@mod.route('/utensils/<int:id>', methods=["PUT"])
def update_utensil(id):
    try:
        result = query(SQL_STRINGS.QRY_UTENSIL_BY_ID, id, True)
        if result["status"] == "NOT_FOUND":
            respose = {
                "message": "Utensilio no encontrado",
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
        
        # * Getting values from request
        name = data["name"].strip()
        
        if not name:
            return jsonify({"message": "Faltan campos obligatorios", "status": 400}), 200
        
        # TODO: Validar imagen almacenarla y guardarla en la db con su nombre
        
        if data:
            utensil = {
                'name': name
            }
            
            errors = val_req_data(utensil, utensil_schema)
            if errors:
                print("Error", errors)
                respose = {
                    "message": "Error en la valifación de la petición",
                    "errors": errors,
                    "status": 400
                }
                return jsonify(respose)
            result = sql(SQL_STRINGS.SQL_UPDATE_UTENSIL, (
                name, id
            ))
            if result['status'] != "OK":
                return jsonify({"message": "Error al actulizar el utensilio", "status": 400}), 200
            respose = {
                "message": "Utensilio actulizado exitosamente!",
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
        print("Ha ocurrido un error en @update_utensil/{}".format(e))
        return jsonify({
            "message": "Error inesperado en el servidor",
            "status": 500
        }), 500
        

@mod.route('/utensils/<int:id>', methods=["DELETE"])
def delete_utensil(id):
    try:
        result = query(SQL_STRINGS.QRY_UTENSIL_BY_ID, id, True)
        if result["status"] == "NOT_FOUND":
            respose = {
                "message": "Utensilio no encontrado",
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

        response = sql(SQL_STRINGS.SQL_DELETE_UTENSIL, id)
        if response["status"] != "OK":
            return jsonify({"message": "Error al borrar el utensilio", "status": 500}), 500
        return jsonify({"message": "Utensilio eliminado correctamente", "status": 200}), 200
    except Exception as e:
        print("Ha ocurrido un error en @delete_utensil/{}".format(e))
        respose = {
            "message": "Error inesperado en el servidor",
            "status": 500
        }
        return jsonify(respose), 500
    
    
    
@mod.route("/pic_utensil/<int:id_utensil>", methods=["GET"])
def get_pic_utensil(id_utensil):
    try:
        result = query(SQL_STRINGS.QRY_UTENSIL_BY_ID, id_utensil, True)
        if result["status"] == "NOT_FOUND":
            respose = {
                "message": "Utensilio no encontrado",
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
        
        result = query(SQL_STRINGS.QRY_UTENSIL_PIC, id_utensil, True)
        if result["status"] != "OK":
            return jsonify({"message": "Error al obtener la imagen", "status": 500}), 500
        
        if not result["data"]:
            return jsonify({'message': 'Imagen no encontrada', "status": 404}), 404
        
        image_bit = result['data']["image_bit"]

        img_io = io.BytesIO(image_bit)
        img_io.seek(0)
        
        return send_file(img_io, mimetype='image/png')
        
    except Exception as e:
        print("Ha ocurrido un error en @get_pic_utensil/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
        return None
        
    
    
@mod.route("/pic_utensil/<int:id_utensil>", methods=["POST"])
def save_pic_utensil(id_utensil):
    try:
        result = query(SQL_STRINGS.QRY_UTENSIL_BY_ID, id_utensil, True)
        if result["status"] == "NOT_FOUND":
            respose = {
                "message": "Utensilio no encontrado",
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
            
            response = sql(SQL_STRINGS.SQL_SAVE_PIC_UTENSIL, (filename, img_byte_arr, id_utensil))
            if response["status"] != "OK":
                return jsonify({"message": "Error al agregar la imagen", "status": 500}), 200
            
            return jsonify({'message': 'Imagen registrada correctamente', "status": 201}), 201
        return jsonify({'message': 'No se recibio una imagen valida', "status": 400}), 400
    except Exception as e:
        print("Ha ocurrido un error en @save_pic_utensil/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
        return None
    

# =========== FUNCTIONS =========== #