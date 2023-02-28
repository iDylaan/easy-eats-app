class Sql_Strings():
    QRY_RECIPE_INGREDIENTS_BY_ID = (
        "SELECT "
            "i.id, "
        	"i.name, "
        	"CONCAT(CAST(ri.amount AS CHAR), ' ', ri.type_amount) AS 'amount_message', "
        	"ri.amount, "
        	"ri.type_amount, "
        	"i.description, "
        	"i.price "
        "FROM recipe_ingredients ri "
        "JOIN ingredients i ON ri.id_ingredient = i.id "
        "JOIN recipes r ON ri.id_recipe = r.id "
        "WHERE r.id = %s"
    )
    
    QRY_RECIPES_INGREDIENTS = (
        "SELECT "
        "r.id as 'recipe_id', "
        "CONCAT( "
            "GROUP_CONCAT( "
                "'[', "
                "i.id, ', ', "
                "i.name, ', ', "
                "CONCAT(CAST(ri.amount AS CHAR), ' ', ri.type_amount), ', ', "
                "ri.amount, ', ', "
                "ri.type_amount, ', ', "
                "i.description, ', ', "
                "i.price, ']' "
            ") "
        ") AS 'ingredients_array' "
        "FROM recipe_ingredients ri " 
        "JOIN ingredients i ON ri.id_ingredient = i.id " 
        "JOIN recipes r ON ri.id_recipe = r.id " 
    )

    QRY_INGREDIENT_BY_ID = (
        "SELECT * FROM ingredients "
        "WHERE id = %s"
    )

    QRY_COUNT_INGREDIENT_BY_ID = (
        "SELECT COUNT(*) FROM ingredients AS 'count' "
        "WHERE id = %s"
    )

    SQL_INSERT_RECIPE_INGREDIENTS = (
        "INSERT INTO recipe_ingredients VALUES {}"
    )
    
    SQL_DELETE_RECIPE_INGREDIENT = (
        "DELETE FROM recipe_ingredients "
        "WHERE id_recipe = %s AND id_ingredient = %s"
    )