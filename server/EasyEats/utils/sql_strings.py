class Sql_Strings():

    GET_SESSION_ID_BY_ID = ("select id "
        " from users"
        " where id = :id_user ")

    GET_ADMIN = ("select id, id_rol, name"
        " from users"
        " where id_rol = 1")