import mysql.connector
from flask import session, jsonify
from .sql_strings import Sql_Strings as SQL_STRINGS

def sql(rawSQL, sqlVars={}):
    from EasyEats.config.conf_alchemy import db
    res = None
    try:
        assert type(rawSQL)==str
        assert type(sqlVars)==dict
        res = db.session.execute(rawSQL, sqlVars)
        response = db.session.commit()
    except Exception as e:
        print("Ha ocurrido el siguiente error en @sql.misc/{}".format(e))


def login_required(f):
    @wrap(f)
    def wrap(*args, **kwargs):
        try:
            if 'logged_in' in session:
                db_session_id = sql(SQL_STRINGS.GET_SESSION_ID_BY_ID, {'id_user': session['id']}).fetchone()
                if db_session_id['session_id'] is None:
                    return jsonify({'auth': 'false'})
                else:
                    return f(*args, **kwargs)
            else:
                return jsonify({'auth': 'false'})
        except Exception as e:
            print("Ha ocurrido el siguiente error en @login_required.misc/{}".format(e))

def is_Admin(f):
    @wrap(f)
    def wrap(*args, **kwargs):
        try:
            if 'logged_in' in session:
                db_session_id = sql(SQL_STRINGS.GET_ADMIN, {'id_user': session['id']}).fetchone()
                if db_session_id['role'] is None:
                    return jsonify({'auth': 'false'})
                elif db_session_id['role'] != 1:
                    return jsonify({'message': 'Acceso denegado, no tienes permisos para acceder a este sitio'})
                else:
                    return f(*args, **kwargs)
            else:
                return jsonify({'auth': 'false'})
        except Exception as e:
            print("Ha ocurrido el siguiente error en @is_Admin.misc/{}".format(e))


