class Sql_Strings():
    QRY_RECIPES = ("SELECT * FROM recipes")
    
    GET_RECIPE = (
        "SELECT * FROM recipes "
        "WHERE id = %s"
    )