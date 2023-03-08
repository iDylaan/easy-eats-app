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
    
    