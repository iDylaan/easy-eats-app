import os, uuid
from flask import Blueprint, request, jsonify, Response
from flask_cors import cross_origin, CORS
from cerberus import Validator
from werkzeug.security import generate_password_hash, check_password_hash
from .schemas import user_schema
from .users_demo import users
from .sql_strings import Sql_Strings as SQL_STRINGS
from EasyEats.config.conf_maria import query
from EasyEats import app

# MODULE
mod = Blueprint('usuarios', __name__, 
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
        "Access-Control-Allow-Headers": "Content-Type"
    }



# Schemas validate
def val_req_data(data, schema): # validate request data
    v = Validator(schema)
    if not v.validate(data):
        return jsonify({"errors": v.errors}), 400
    return None




# =========== ROUTES ===========
@mod.route('/users', methods=["GET"])
def users_list():
    users_dict = {}
    try:            
        result = query(SQL_STRINGS.USERS_LIST)
        if result:
            users_dict = [dict(row) for row in result]
            response = {
                "message": str(len(users_dict)) + " usuarios encontrados.",
                "status": 200,
                "data": users_dict
            }
            return jsonify(users_dict)
        else:
            print("No hay resultados")
            return jsonify({"message": "No results"})
    except Exception as e:
        print("Ha ocurrido un error en @users_list/{}".format(e))


@mod.route('/users', methods=['POST'])
def create_user():
    name = None
    username = None
    tagline = None
    email = None
    password = None
    id_rol = None
    heigh = None
    width = None
    date_of_birth = None
    image = None
    try:
        users_dict = request.form.get("users_dict")
        name = request.form.get("name")
        username = request.form.get("username")
        tagline = request.form.get("tagline")
        email = request.form.get("email")
        password = request.form.get("password")
        id_rol = request.form.get("id_rol")
        heigh = request.form.get("heigh")
        width = request.form.get("width")
        date_of_birth = request.form.get("date_of_birth")
        # Validacion de imagen
        image = request.files.get("image")
        if image:
            image_name = str(uui.uuid4()) + ".jpg"
            if not os.path.exist(app.config['USER_IMAGES']):
                ok.mkedirs(app.config['USER_IMAGES'])
            image.save(os.path.join(app.config['USER_IMAGES'], image_name))
            image = imagen_name
        else:
            image = None
        
        data = {
            "users_dict": users_dict,
            "name": name,
            "username": username,
            "tagline": tagline,
            "email": email,
            "password": password,
            "id_rol": id_rol,
            "heigh": heigh,
            "width": width,
            "date_of_birth": date_of_birth,
            "image": image
        }
        response = {
            "message": "Recibido correctamente",
            "status": 200,
            "data": data
        }

        
        return jsonify(response)

    except Exception as e:
        print("Ha ocurrido el siguiente error: ", e)
        return ({"message": "Error en el servidor", "status": 500})

