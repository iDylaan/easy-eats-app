import pymysql
from EasyEats import app

def query(qry, params=None):
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
            result = cursor.fetchall()
            return result
    except Exception as e:
        print("Ha ocurrido un error en el query @query.conf_maria/{}".format(e))
    finally:
        print("Conexion finalizada")
        cursor.close()


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
    try: 
        conn = pymysql.connect(**config)
    except Exception as e:
        print("Ha ocurrido un error al conectar en @conn_maria.conf_maria/{}".format(e))
        return None
    return conn