class Sql_Strings():
    QRY_ALL_INGREDIENTS = ("SELECT * FROM ingredients")
    
    QRY_INGREDIENT_BY_ID = (
        "SELECT * FROM ingredients "
        "WHERE id = %s"
    )
    
    SQL_CREATE_INGREDIENT = (
        "INSERT INTO ingredients (name, description, price, image) "
        "VALUES (%s, %s, %s, %s)"
    )
    
    SQL_UPDATE_INGREDIENT = (
        "UPDATE ingredients SET "
        "name = %s, "
        "description = %s, "
        "price = %s, "
        "image = %s "
        "WHERE id = %s"
    )
    
    SQL_DELETE_INGREDIENT = (
        "DELETE FROM ingredients "
        "WHERE id = %s"
    )