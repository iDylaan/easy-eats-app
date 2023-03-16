class Sql_Strings():
    USERS_LIST = (
        "SELECT "
        "id, "
        "username, "
        "tagline, "
        "name, "
        "email, "
        "password, "
        "date_of_birth "
        "height, "
        "weight, "
        "banned, "
        "id_rol "
        "FROM users "
        "WHERE banned = 0"
    )
    
    GET_USER = (
        "SELECT "
        "id, "
        "username, "
        "tagline, "
        "name, "
        "email, "
        "password, "
        "date_of_birth "
        "height, "
        "weight, "
        "banned, "
        "id_rol "
        "FROM users "
        "WHERE id = %s AND banned = 0"
    )

    CATEGORIAS_LIST = ("SELECT * FROM categories WHERE banned = 0")
    
    COUNT_USERS = (
        "SELECT COUNT(*) AS 'conteo' "
        "FROM users "
        "WHERE username = %s "
        "AND tagline = %s "
    )
    
    COUNT_EMAILS = (
        "SELECT COUNT(*) AS 'conteo' " 
        "FROM users "
        "WHERE email = %s "
    )
    
    CREATE_USER = (
        "INSERT INTO users "
        "(username, "
        "tagline, "
        "name,  "
        "email,  "
        "password,  "
        "date_of_birth,  "
        "height,  "
        "weight,  "
        "id_rol) VALUES "
        "(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    )

    UPDATE_USER = (
        "UPDATE users SET "
        "username = %s,"
        "tagline = %s, "
        "name = %s, "
        "email = %s, "
        "password = %s, "
        "date_of_birth = %s, "
        "height = %s, "
        "weight = %s, "
        "id_rol = %s "
        "WHERE id = %s"
    )


    UPDATE_USER_NEW_IMAGE = (
        "UPDATE users SET "
        "username = %s,"
        "tagline = %s, "
        "image_name = %s, "
        "image_bit = %s, "
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
        "UPDATE users SET "
        "banned = 1 "
        "WHERE id = %s"
    )
    
    QRY_RECIPES_BY_USER_ID = (
        "SELECT r.id "
        "FROM "
            "recipes r "
            "JOIN users u ON u.id = r.user_id "
        "WHERE r.user_id = %s "
    )
    
    SQL_DELETE_RECIPES_BY_USER_ID = (
        "UPDATE recipes SET "
        "banned = 1 "
        "WHERE id_user = %s "
    )
    
    SQL_DELETE_REVIEWS_BY_ID = (
        "UPDATE reviews SET "
        "banned = 1 "
        "WHERE id_recipe = %s "
    )
    
    SQL_SAVE_PICPROFILE = (
        "UPDATE users SET "
        "image_name = %s, "
        "image_bit = %s "
        "WHERE id = %s"
    )
    
    GET_USER_PIC = (
        "SELECT "
        "image_bit "
        "FROM users "
        "WHERE id = %s "
    )