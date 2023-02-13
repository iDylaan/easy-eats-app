class Sql_Strings():
    SIGNIN_USER = ("INSERT INTO users (username, tagline, name, email, password, date_of_birth, id_rol) "
               "VALUES (%s, %s, %s, %s, %s, %s, %s)")
    
    QRY_USERS = ("SELECT id, email, password, id_rol, username, tagline FROM users")