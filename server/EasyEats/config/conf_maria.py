import pymysql
from EasyEats import app

def query(qry, params=None, get_one=False):
    conn = conn_maria()
    if conn is None:
        return None
    try:
        with conn.cursor() as cursor:
            if params:
                cursor.execute(qry, params)
            else:
                cursor.execute(qry)
            conn.commit()
            result = cursor.fetchone() if get_one else cursor.fetchall()
            if not result:
                return {"status": "NOT_FOUND"} 
            return {"status": "OK", "data": result}
    except Exception as e:
        print("Ha ocurrido un error en el query @query.conf_maria/{}".format(e))
        return {"status": "Error"}
    finally:
        cursor.close()
        conn.close()
        
def sql(qry, params=None):
    conn = conn_maria()
    if conn is None:
        return None
    try:
        with conn.cursor() as cursor:
            if params:
                cursor.execute(qry, params)
            else:
                cursor.execute(qry)
            conn.commit()
            result = cursor.fetchone()
            return {"status": "OK"}
    except Exception as e:
        print("Ha ocurrido un error en el query @query.conf_maria/{}".format(e))
        return {"status": "Error"}
    finally:
        cursor.close()
        conn.close()


def conn_maria():
    config = {
        'host': app.config['MARIA_HOST'],
        'port': int(app.config['MARIA_PORT']),
        'user': app.config['MARIA_USER'],
        'password': app.config['MARIA_PASS'],
        'database': app.config['MARIA_DB'],
        'charset': app.config['MARIA_CHARSET'],
        'cursorclass': pymysql.cursors.DictCursor
    }
    # config = { # * Comentar en caso de utilizar contenedores
    #     'host': 'localhost',
    #     'port': 3090,
    #     'user': app.config['MARIA_USER'],
    #     'password': 'admin',
    #     'database': app.config['MARIA_DB'],
    #     'charset': app.config['MARIA_CHARSET'],
    #     'cursorclass': pymysql.cursors.DictCursor
    # }
    try: 
        conn = pymysql.connect(**config)
    except Exception as e:
        print("Ha ocurrido un error al conectar en @conn_maria.conf_maria/{}".format(e))
        return None
    return conn