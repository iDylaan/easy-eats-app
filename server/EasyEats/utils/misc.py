import jwt, datetime
from flask import session, jsonify
from functools import wraps
from cerberus import Validator
from .sql_strings import Sql_Strings as SQL_STRINGS
from EasyEats import app
from EasyEats.config.conf_maria import query


# Schemas validate
def val_req_data(data, schema): # validate request data
    v = Validator(schema)
    if not v.validate(data):
        respose = {
            "message": v.errors,
            "status": 400,
            "data": None
        }
        return jsonify(respose)
    return None



def gen_jwt(user_id, user_role):
    try:
        payload = {
            "user_id": user_id,
            "is_admin": True if user_role == 2 else False,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=(60*60*24*1)) # ? seconds * minutes * hours * days
        }
        return jwt.encode(payload, app.config['SECRET_JWT_KEY'], algorithm='HS256')
    except Exception as e:
        print("Ha ocurrido un error en @misc.gen_jwt/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))


def login_required(f):
    @wrap(f)
    def wrap(*args, **kwargs):
        try:
            token = request.headers.get("Authorization", None)
            if not token: 
                return jsonify({"message": "Token faltante", "status": 401}), 401
                        
            # * Verify valid token
            decoded_token = verify_jwt_token(token.split(" ")[1])
            
            if not isinstance(decoded_token, str):
                # * Verify user exists
                user = False
                user_id = payload.get("user_id", None)
                user_email = payload.get("user_email", None)
                user_password = payload.get("user_password", None)

                if not user_id \
                or not user_email \
                or not user_password:
                    return jsonify({"message": "Invalid payload", "status": 401}), 401

                result = query(SQL_STRINGS.AUTH_COUNT_USERS, (user_email, user_password))
                if result["status"] != "OK":
                    return jsonify({"message": "Error en la consulta @AUTH_COUNT_USERS", "status": 400}), 400

                user = bool(int(result["data"]["conteo"]))
                if not user:
                    return jsonify({"message": "JWT Invalido"}), 401
            return func(*args, **kwargs)
        except Exception as e:
            print("Ha ocurrido el siguiente error en @login_required.misc/{}".format(e))
    return wrapper


def is_Admin(f):
    @wrap(f)
    def wrap(*args, **kwargs):
        try:
            auth_header = request.headers.get("Authorization", None)
            if not auth_header:
                return jsonify({"message": "Token faltante", "status": 401}), 401
            
            # * Verify valid token
            token = auth_header.split(" ")[1]
            payload = jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
            
             # * Verify user exists
            user = False
            user_id = payload.get("user_id", None)
            user_email = payload.get("user_email", None)
            user_password = payload.get("user_password", None)
            
            if not user_id \
            or not user_email \
            or not user_password:
                return jsonify({"message": "Invalid payload", "status": 401}), 401
            
            result = query(SQL_STRINGS.AUTH_COUNT_ADMINS, (user_email, user_password))
            if result["status"] != "OK":
                return jsonify({"message": "Error en la consulta @AUTH_COUNT_ADMINS", "status": 400}), 400
            
            user = bool(int(result["data"]["conteo"]))
            if not user:
                return jsonify({"message": "Usuario no encontrado"}), 401
            return func(*args, **kwargs)
        except Exception as e:
            print("Ha ocurrido el siguiente error en @login_required.misc/{}".format(e))
    return wrapper


def verify_jwt_token(token):
    try:
        decoded_token = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        return decoded_token
    except jwt.exceptions.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.exceptions.InvalidTokenError:
        return 'Invalid token. Please log in again.'

def validate_user_exist(username, tagline):
    try:
        cnt_users = query(SQL_STRINGS.COUNT_USERS, (username, tagline), True)
        if cnt_users["status"] != "OK":
            raise Exception("Error en la consulta de usuarios a la base de datos en @validate_email_exist")
        return (bool(int(cnt_users['data']['conteo'])))
    except Exception as e:
        print("Ha ocurrido el siguiente error en @validate_user_exist/{}".format(e))
        return None

def validate_email_exist(email):
    try:
        cnt_emails = query(SQL_STRINGS.COUNT_EMAILS, (email), True)
        if cnt_emails["status"] != "OK":
            raise Exception("Error en la consulta de emails a la base de datos en @validate_email_exist")
        return bool(int(cnt_emails['data']['conteo']))
    except Exception as e:
        print("Ha ocurrido el siguiente error en @validate_email_exist/{}".format(e))
        return None