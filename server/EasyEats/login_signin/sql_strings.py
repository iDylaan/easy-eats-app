class Sql_Strings():
    SIGNIN_USER = ("INSERT INTO users (username, tagline, name, email, password, date_of_birth, id_rol) "
               "VALUES (%s, %s, %s, %s, %s, %s, %s)")