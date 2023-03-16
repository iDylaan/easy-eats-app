class Sql_Strings():
    QRY_ALL_CATEGORIES = ("SELECT * FROM categories WHERE banned = 0")
    
    QRY_CATEGORY_BY_ID = (
        "SELECT * FROM categories "
        "WHERE id = %s "
        "AND banned = 0 "
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
        "UPDATE categories SET "
        "banned = 1 "
        "WHERE id = %s"
    )