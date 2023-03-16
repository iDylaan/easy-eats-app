class Sql_Strings():
    QRY_ALL_UTENSILS = ("SELECT * FROM utensils WHERE banned = 0")
    
    QRY_UTENSIL_BY_ID = (
        "SELECT * FROM utensils "
        "WHERE id = %s "
        "AND banned = 0 "
    )
    
    SQL_CREATE_UTENSIL = (
        "INSERT INTO utensils (name) "
        "VALUES (%s)"
    )
    
    SQL_UPDATE_UTENSIL = (
        "UPDATE utensils SET "
        "name = %s "
        "WHERE id = %s"
    )
    
    SQL_DELETE_UTENSIL = (
        "UPDATE utensils SET "
        "banned = 1 "
        "WHERE id = %s"
    )