class Sql_Strings():
    QRY_ALL_UTENSILS = ("SELECT * FROM utensils")
    
    QRY_UTENSIL_BY_ID = (
        "SELECT * FROM utensils "
        "WHERE id = %s"
    )
    
    SQL_CREATE_UTENSIL = (
        "INSERT INTO utensils (name, image) "
        "VALUES (%s, %s)"
    )
    
    SQL_UPDATE_UTENSIL = (
        "UPDATE utensils SET "
        "name = %s, "
        "image = %s "
        "WHERE id = %s"
    )
    
    SQL_DELETE_UTENSIL = (
        "DELETE FROM utensils "
        "WHERE id = %s"
    )