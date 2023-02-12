import jwt, datetime
from flask import session, jsonify
from functools import wraps
from .sql_strings import Sql_Strings as SQL_STRINGS
from EasyEats import app
from EasyEats.config.conf_maria import query


def jwt(user_id, user_email, user_password):
    payload = {
        "user_id": user_id,
        "user_email": user_email,
        "user_password": user_password,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=(60*60*24))
    }
    return jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')


def login_required(f):
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
            
            result = query(SQL_STRINGS.AUTH_COUNT_USERS, (user_email, user_password))
            if result["status"] != "OK":
                return jsonify({"message": "Error en la consulta @AUTH_COUNT_USERS", "status": 400}), 400
            
            user = bool(int(result["data"]["conteo"]))
            if not user:
                return jsonify({"message": "Usuario no encontrado"}), 401
            return func(*args, **kwargs)
        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Token expirado", "status": 401}), 401
        except jwt.InvalidTokenError:
            return jsonify({"message": "Token inválido", "status": 401}), 401
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
        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Token expirado", "status": 401}), 401
        except jwt.InvalidTokenError:
            return jsonify({"message": "Token inválido", "status": 401}), 401
        except Exception as e:
            print("Ha ocurrido el siguiente error en @login_required.misc/{}".format(e))
    return wrapper



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