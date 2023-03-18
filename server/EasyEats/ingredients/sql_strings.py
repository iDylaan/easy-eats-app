class Sql_Strings():
    QRY_ALL_INGREDIENTS = (
        "SELECT "
        "id, name, description, price "
        "FROM ingredients WHERE banned = 0"
    )
    
    QRY_INGREDIENT_BY_ID = (
        "SELECT "
        "id, name, description, price "
        "FROM ingredients "
        "WHERE id = %s "
        "AND banned = 0"
    )
    
    SQL_CREATE_INGREDIENT = (
        "INSERT INTO ingredients (name, description, price) "
        "VALUES (%s, %s, %s)"
    )
    
    SQL_UPDATE_INGREDIENT = (
        "UPDATE ingredients SET "
        "name = %s, "
        "description = %s, "
        "price = %s "
        "WHERE id = %s"
    )
    
    SQL_DELETE_INGREDIENT = (
        "UPDATE ingredients SET "
        "banned = 1 "
        "WHERE id = %s"
    )
    
    QRY_INGREDIENT_PIC = (
        "SELECT image_bit AS 'image' "
        "FROM ingredients "
        "WHERE id = %s "
        "AND banned = 0"
    )
    
    SQL_SAVE_PIC_INGREDIENT = (
        "UPDATE ingredients SET "
        "image_name = %s, "
        "image_bit = %s "
        "WHERE id = %s "
        "AND banned = 0"
    )