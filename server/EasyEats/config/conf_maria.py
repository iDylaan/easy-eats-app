import mysql.connector
from EasyEats import app

def small_query(qry, params=None):
    conn = conn_maria()
    if conn is None:
        return None
    try:
        cursor = conn.cursor(buffered=True)
        result = cursor.execute(qry, params)
        return result
    except Exception as e:
        print("Ha ocurrido un error en el query @query.conf_maria/{}".format(e))
    finally:
        cursor.close()

def big_query(qry, params=None):
    conn = conn_maria()
    if conn is None:
        return None
    try:
        cursor = conn.cursor()
        result = cursor.execute(qry, params)
        return result
    except Exception as e:
        print("Ha ocurrido un error en el query @query.conf_maria/{}".format(e))
    finally:
        cursor.close()

def conn_maria():
    # config = {
    #     'host': app.config['MARIA_HOST'],
    #     'port': app.config['MARIA_PORT'],
    #     'user': app.config['MARIA_USER'],
    #     'password': app.config['MARIA_PASS'],
    #     'database': app.config['MARIA_DB']
    # }
    config = {
        'host': 'easyeasts_db',
        'port': 3306,
        'user': 'easy_eats_us',
        'password': 'admin',
        'database': 'easy_eats_db'
    }
    try: 
        conn = mysql.connector.connect(**config)
    except Exception as e:
        print("Ha ocurrido un error al conectar en @conn_maria.conf_maria/{}".format(e))
        return None
    return conn