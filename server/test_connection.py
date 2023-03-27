import pymysql

host = "easy-eats-db.cuhuub668g0y.us-east-2.rds.amazonaws.com"
port = 3306
user = "admin"
password = "Easy-Eats_2023*"
database = "easy_eats_db"

try:
    connection = pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database
    )
    print("Conexión exitosa a la base de datos")
except Exception as e:
    print(f"Error al conectar a la base de datos: {e}")
