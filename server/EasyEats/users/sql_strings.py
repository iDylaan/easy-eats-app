class Sql_Strings():
    USERS_LIST = ("SELECT * FROM users")
    
    GET_USER = ("SELECT * FROM users WHERE id = %s")

    CATEGORIAS_LIST = ("SELECT * FROM categories")
    
    CREATE_USER = (
        "INSERT INTO users "
        "(username, "
        "tagline,  "
        "image,  "
        "name,  "
        "email,  "
        "password,  "
        "date_of_birth,  "
        "height,  "
        "weight,  "
        "id_rol) VALUES "
        "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    )

    UPDATE_USER = (
        "UPDATE users SET "
        "username = %s,"
        "tagline = %s, "
        "image = %s, "
        "name = %s, "
        "email = %s, "
        "password = %s, "
        "date_of_birth = %s, "
        "height = %s, "
        "weight = %s, "
        "id_rol = %s "
        "WHERE id = %s"
    )
    
    DELETE_USER = (
        "DELETE FROM users "
        "WHERE id = %s"
    )