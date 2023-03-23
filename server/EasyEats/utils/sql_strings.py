class Sql_Strings():

    GET_SESSION_ID_BY_ID = ("select id "
        " from users"
        " where id = :id_user ")

    GET_ADMIN = ("select id, id_rol, name"
        " from users"
        " where id_rol = 1")
    
    COUNT_USERS = ("SELECT COUNT(*) as 'conteo' FROM users "
                   "WHERE users.username = %s "
                   "AND users.tagline = %s ")

    COUNT_EMAILS = ("SELECT COUNT(*) as 'conteo' FROM users "
                   "WHERE users.email = %s")
    
    AUTH_COUNT_USERS = (
        "SELECT COUNT(*) as 'conteo' "
        "FROM users "
        "WHERE email = %s "
        "AND password = %s "
        "AND id_rol = 2"
    )

    AUTH_COUNT_ADMINS = (
        "SELECT COUNT(*) as 'conteo' "
        "FROM users "
        "WHERE email = %s "
        "AND password = %s "
        "AND id_rol = 1"
    )
