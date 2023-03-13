class Sql_Strings():
    QRY_FAVORITE_RECIPES_BY_USER_ID = (
        "SELECT "
            "r.name, "
            "r.image, "
            "r.cooking_time, "
            "r.dinners, "
            "r.budget, "
            "r.calories "   
        "FROM "
            "favorite_recipes fr "
            "JOIN recipes r ON fr.id_recipe = r.id "
        "WHERE fr.id_user =%s"
    )
    
    QRY_COUNT_FAVORITE_RECIPES_BY_IDS = (
        "SELECT COUNT(*) AS 'count' "
        "FROM favorite_recipes "
        "WHERE id_user = %s "
        "AND id_recipe = %s"
    )
    
    SQL_INSERT_FAVORITE_RECIPE = (
        "INSERT INTO favorite_recipes (id_user, id_recipe) "
        "VALUES (%s, %s)"
    )