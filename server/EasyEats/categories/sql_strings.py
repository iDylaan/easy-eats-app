class Sql_Strings():
    QRY_ALL_CATEGORIES = ("SELECT * FROM categories")
    
    QRY_CATEGORY_BY_ID = (
        "SELECT * FROM categories "
        "WHERE id = %s"
    )
    
    SQL_CREATE_CATEGORY = (
        "INSERT INTO categories (name) "
        "VALUES (%s)"
    )
    
    SQL_UPDATE_CATEGORY = (
        "UPDATE categories SET "
        "name = %s "
        "WHERE id = %s"
    )
    
    SQL_DELETE_CATEGORY = (
        "DELETE FROM categories "
        "WHERE id = %s"
    )