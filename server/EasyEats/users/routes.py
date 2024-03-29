import io
from datetime import datetime
from flask import Blueprint, request, jsonify, send_file
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from PIL import Image as PILImage
from .schemas import user_schema
from .sql_strings import Sql_Strings as SQL_STRINGS
from EasyEats.config.conf_maria import query, sql
from EasyEats.utils.misc import (
    val_req_data,
    login_required
)

# MODULE
mod = Blueprint('users', __name__, 
    template_folder='templates', 
    static_folder='static', 
    static_url_path='/%s' % __name__
)
# CORS acces to "users"
CORS(mod)

# CORS Configure Parameters
@mod.route('/users', methods=['OPTIONS'])
def handle_options():
    return "", 200, {
        "Access-Control-Allow-Origin": "*", # "*"
        "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE",
        "Access-Control-Allow-Headers": "Content-Type, Authorization"
    }


# =========== ROUTES ===========
@mod.route('/users', methods=["GET"])
def get_users():
    try:
        result = query(SQL_STRINGS.USERS_LIST)
        if result["status"] == "OK":
            users_dict = [dict(row) for row in result["data"]]
                    
            respose = {
                "message": "OK",
                "status": 200,
                "data": users_dict
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
        print("Ha ocurrido un error en @get_users/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
        respose = {
            "message": "Error inesperado en el servidor",
            "status": 500
        }
        return jsonify(respose), 500


@mod.route('/users/<int:id>', methods=["GET"])
def get_user(id):
    try:
        result = query(SQL_STRINGS.GET_USER, id, True)
        if result["status"] == "OK":
            respose = {
                "message": "OK",
                "status": 200,
                "data": result["data"]
            }
            return jsonify(respose), 200
        elif result["status"] == "NOT_FOUND":
            respose = {
                "message": "Usuario no encontrado",
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
        print("Ha ocurrido un error en @get_user/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
        
        
@mod.route('/users', methods=["POST"])
def save_user():
    try:
        data = request.get_json()
        
        # * Validating null values
        name = data.get("name", None)
        height = data.get("height", None)
        weight = data.get("weight", None)
        username = data.get("username", None)
        tagline = data.get("tagline", None)
        email = data.get("email", None)
        id_rol = data.get("id_rol", None)
        password = data.get("password", None)
        date_of_birth = data.get("date_of_birth", None)
        
        if not username \
        or not tagline \
        or not email \
        or not password \
        or not date_of_birth \
        or not id_rol:
            return jsonify({"message": "Faltan campos obligatorios", "status": 400}), 200
        
        # * Getting values from request
        tagline = data["tagline"].upper()
        id_rol = int(data["id_rol"])
        # * Heashed password for security
        password = generate_password_hash(data["password"], method='sha256')
        # * Formating date
        date_of_birth = datetime.strptime(data["date_of_birth"], '%d-%m-%Y').date() # ? Format (yyyy-mm-dd)
        
        
        # TODO: Validar imagen almacenarla y guardarla en la db con su nombre
        
        if data:
            ### * VALIDATION  UNIQUE UNSERNAME + TAGLINE* ###
            user_exist = validate_user_exist(username, tagline)
            if user_exist == None:
                respose = {
                    "message": "Error inesperado en el servidor",
                    "status": 500
                }
                return jsonify(respose), 500
            elif user_exist:
                respose = {
                    "message": "Tagline no disponible",
                    "campo": "tagline",
                    "status": 400
                }
                return jsonify(respose), 200
            ### * VALIDATION  UNIQUE EMAIL * ###
            email_exist = validate_email_exist(email)
            if email_exist == None:
                respose = {
                    "message": "Error inesperado en el servidor",
                    "status": 500
                }
                return jsonify(respose), 500
            elif email_exist:
                respose = {
                    "message": "Email no disponible",
                    "campo": "email",
                    "status": 400
                }
                return jsonify(respose), 200
            
            user = {
                'username': username,
                'tagline': tagline,
                'name': name,
                'email': email,
                'password': password,
                'date_of_birth': date_of_birth,
                'height': height,
                'weight': weight,
                'id_rol': id_rol
            }
            
            errors = val_req_data(user, user_schema)
            if errors:
                print("Error", errors)
                respose = {
                    "message": "Error en la valifación de la petición",
                    "errors": errors,
                    "status": 400,
                    "data": None
                }
                return jsonify(respose)

            result = sql(SQL_STRINGS.CREATE_USER, (
                username,
                tagline,
                name,
                email,
                password,
                date_of_birth,
                height,
                weight,
                id_rol
            ))
            if result['status'] != "OK":
                return jsonify({"message": "Error al crear el usuario", "status": 400}), 200
            respose = {
                "message": "Usuario creado correctamente!",
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
        print("Ha ocurrido un error en @save_user/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
        return jsonify({
            "message": "Error inesperado en el servidor",
            "status": 500,
            "data": None
        }), 500
        
        
@mod.route('/users/<int:id>', methods=["PUT"])
def update_user(id):
    try:
        data = request.get_json()
        
        
        # * Validating null values
        name = data.get("name", None)
        height = data.get("height", None)
        weight = data.get("weight", None)
        username = data.get("username", None)
        tagline = data.get("tagline", None)
        email = data.get("email", None)
        id_rol = data.get("id_rol", None)
        password = data.get("password", None)
        date_of_birth = data.get("date_of_birth", None)
        
        if not username \
        or not tagline \
        or not email \
        or not password \
        or not date_of_birth \
        or not id_rol:
            return jsonify({"message": "Faltan campos obligatorios", "status": 400}), 200
        
        # * Heashed password for security
        password = generate_password_hash(data["password"], method='sha256')
        # * Getting values from request
        tagline = data["tagline"].upper()
        id_rol = int(data["id_rol"])
        # * Formating date
        date_of_birth = datetime.strptime(data["date_of_birth"], '%d-%m-%Y').date() # ? Format (yyyy-mm-dd)
        
        
        # TODO: Validar imagen almacenarla y guardarla en la db con su nombre
        
        if data:
            ### * VALIDATION  UNIQUE UNSERNAME + TAGLINE* ###
            user_exist = validate_user_exist(username, tagline)
            if user_exist == None:
                respose = {
                    "message": "Error inesperado en el servidor",
                    "status": 500
                }
                return jsonify(respose), 500
            elif user_exist:
                respose = {
                    "message": "Tagline no disponible",
                    "status": 200
                }
                return jsonify(respose), 200
            
            user = {
                'username': username,
                'tagline': tagline,
                'name': name,
                'email': email,
                'password': password,
                'date_of_birth': date_of_birth,
                'height': height,
                'weight': weight,
                'id_rol': id_rol
            }
            
            errors = val_req_data(user, user_schema)
            if errors:
                print("Error", errors)
                respose = {
                    "message": "Error en la valifación de la petición",
                    "errors": errors,
                    "status": 400,
                    "data": None
                }
                return jsonify(respose)


            result = sql(SQL_STRINGS.UPDATE_USER, (
                username,
                tagline,
                name,
                email,
                password,
                date_of_birth,
                height,
                weight,
                id_rol,
                id
            ))
            
            if result['status'] != "OK":
                return jsonify({"message": "Error al actualizar el usuario", "status": 400}), 400
            respose = {
                "message": "OK",
                "status": 200,
                "data": "Usuario actualizado correctamente!",
            }
            return jsonify(respose), 200
        else: 
            return jsonify({
                "message": "Error en la petición",
                "status": 400,
                "data": None
            }), 400
    except Exception as e:
        print("Ha ocurrido un error en @update_user/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
        return jsonify({
            "message": "Error inesperado en el servidor",
            "status": 500,
            "data": None
        }), 500
        

@mod.route('/users/<int:id>', methods=["DELETE"])
def delete_user(id):
    try:
        result = query(SQL_STRINGS.GET_USER, id, True)
        if result["status"] == "NOT_FOUND":
            respose = {
                "message": "Usuario no encontrado",
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
        
        response = sql(SQL_STRINGS.SQL_DELETE_RECIPES_BY_USER_ID, id)
        if response["status"] != "OK":
            return jsonify({"message": "Error al eliminar las recetas del usuario dado de baja", "status": 500}), 500
        
        response = sql(SQL_STRINGS.SQL_DELETE_REVIEWS_BY_ID, id)
        if response["status"] != "OK":
            return jsonify({"message": "Error al eliminar las reseñas del usuario dado de baja", "status": 500}), 500

        response = sql(SQL_STRINGS.DELETE_USER, id)
        if response["status"] != "OK":
            return jsonify({"message": "Error al dar de baja al usuario", "status": 500}), 500
        return jsonify({"message": "Usuario dado de baja correctamente", "status": 200}), 200
    except Exception as e:
        print("Ha ocurrido un error en @delete_user/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
        respose = {
            "message": "Error inesperado en el servidor",
            "status": 500
        }
        return jsonify(respose), 500
    
    
@mod.route("/pic_user/<int:id_user>", methods=["GET"])
def get_pic_user(id_user):
    try:
        result = query(SQL_STRINGS.GET_USER, id_user, True)
        if result["status"] == "NOT_FOUND":
            respose = {
                "message": "Usuario no encontrado",
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
        
        result = query(SQL_STRINGS.GET_USER_PIC, id_user, True)
        if result["status"] != "OK":
            return jsonify({"message": "Error al obtener la imagen", "status": 500}), 500
        
        if not result["data"]:
            return jsonify({'message': 'Imagen no encontrada', "status": 404}), 404
        
        image_bit = result['data']["image_bit"]

        img_io = io.BytesIO(image_bit)
        img_io.seek(0)
        
        return send_file(img_io, mimetype='image/png')
        
    except Exception as e:
        print("Ha ocurrido un error en @get_pic_user/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
        return None
        
    
    
@mod.route("/pic_user/<int:id_user>", methods=["POST"])
def save_pic_user(id_user):
    try:
        result = query(SQL_STRINGS.GET_USER, id_user, True)
        if result["status"] == "NOT_FOUND":
            respose = {
                "message": "Usuario no encontrado",
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
            
            response = sql(SQL_STRINGS.SQL_SAVE_pic_user, (filename, img_byte_arr, id_user))
            if response["status"] != "OK":
                return jsonify({"message": "Error al agregar la imagen", "status": 500}), 500
            
            return jsonify({'message': 'Imagen registrada correctamente', "status": 201}), 201
    except Exception as e:
        print("Ha ocurrido un error en @save_pic_user/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
        return None
    

# =========== FUNCTIONS ===========
def validate_user_exist(username, tagline):
    try:
        cnt_users = query(SQL_STRINGS.COUNT_USERS, (username, tagline), True)
        if cnt_users["status"] != "OK":
            raise Exception("Error en la consulta de usuarios a la base de datos en @validate_email_exist")
        return (bool(int(cnt_users['data']['conteo'])))
    except Exception as e:
        print("Ha ocurrido un error en @get_utensils/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
        return None

def validate_email_exist(email):
    try:
        cnt_emails = query(SQL_STRINGS.COUNT_EMAILS, email, True)
        if cnt_emails["status"] != "OK":
            raise Exception("Error en la consulta de emails a la base de datos en @validate_email_exist")
        return bool(int(cnt_emails['data']['conteo']))
    except Exception as e:
        print("Ha ocurrido un error en @get_utensils/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
        return None
    
