class Sql_Strings():
    QRY_RECIPES = (
        "SELECT "
        "id, "
        "name, "
        "description, "
        "cooking_time, "
        "dinners, "
        "update_date, "
        "calories, "
        "fats, "
        "carbs, "
        "protein, "
        "satured_fats, "
        "sodium, "
        "fiber, "
        "sugars, "
        "id_user "
        "FROM recipes WHERE banned = 0"
    )
    
    QRY_RECIPE = (
        "SELECT "
        "id, "
        "name, "
        "description, "
        "cooking_time, "
        "dinners, "
        "update_date, "
        "calories, "
        "fats, "
        "carbs, "
        "protein, "
        "satured_fats, "
        "sodium, "
        "fiber, "
        "sugars, "
        "id_user " 
        "FROM recipes "
        "WHERE id = %s "
        "AND banned = 0 "
    )
    
    SQL_INSERT_RECIPE = (
        "INSERT INTO recipes "
        "(name, description, cooking_time, "
        "dinners, calories, "
        "fats, carbs, protein, satured_fats, "
        "sodium, fiber, sugars, budget, id_user) "
        "VALUES (%s, %s, %s, %s, %s, %s, "
        "%s, %s, %s, %s, %s, %s, %s, %s) "
    )
    
    SQL_UPDATE_RECIPE = (
        "UPDATE recipes SET "
        "name = %s, "
        "description = %s, "
        "cooking_time = %s, "
        "dinners = %s, "
        "calories = %s, "
        "fats = %s, "
        "carbs = %s, "
        "protein = %s, "
        "satured_fats = %s, "
        "sodium = %s, "
        "fiber = %s, "
        "sugars = %s, "
        "budget = %s "
        "WHERE id_user = %s "
        "AND id = %s"
    )
    
    SQL_DELETE_RECIPE = (
        "UPDATE recipes SET "
        "banned = 1 "
        "WHERE id = %s "
    )
    
    QRY_RECIPE_PIC = (
        "SELECT image_bit AS 'image' "
        "FROM recipes "
        "WHERE id = %s "
        "AND banned = 0"
    )
    
    SQL_SAVE_PIC_RECIPE = (
        "UPDATE recipes SET "
        "image_name = %s, "
        "image_bit = %s "
        "WHERE id = %s "
        "AND banned = 0"
    )