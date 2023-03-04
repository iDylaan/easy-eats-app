class Sql_Strings():
    QRY_RECIPES_INGREDIENTS = (
        "SELECT "
            "r.id AS 'recipe_id', "
            "r.name AS 'recipe_name', "
            "GROUP_CONCAT( "
                "DISTINCT CONCAT( "
                    "'{ "
                        "\"id_ingredient\":', i.id, ', "
                        "\"ingredient\": \"', i.name, '\", "
                        "\"amount_desc\": \"', CONCAT(CAST(ri.amount AS CHAR), ' ', ri.type_amount), '\", "
                        "\"amount\":', ri.amount, ', "
                        "\"type_amount\": \"', ri.type_amount, '\", "
                        "\"description\": \"', i.description, '\", "
                        "\"image\": \"', i.image, '\", "
                        "\"price\": ',i.price,'"
                    "}' "
                ") "
                "ORDER BY i.name "
                "SEPARATOR ',' "
            ") AS 'ingredients' "
        "FROM "
            "recipes r "
            "JOIN recipe_ingredients ri ON r.id = ri.id_recipe "
            "JOIN ingredients i ON ri.id_ingredient = i.id "
        "GROUP BY r.id "
    )
    
    QRY_RECIPE_INGREDIENTS = (
        "SELECT "
        "r.id as 'recipe_id', "
        "CONCAT( "
            "GROUP_CONCAT( "
                "'{', "
                    "'\"id_ingredient\"', ':', i.id, ', ', "
                    "'\"ingredient\"', ':', '\"', i.name, '\"', ', ', "
                    "'\"amount_desc\"', ':', CONCAT('\"', CAST(ri.amount AS CHAR), ' ', ri.type_amount, '\"'), ', ', "
                    "'\"amount\"', ':', ri.amount, ', ', "
                    "'\"type_amount\"', ':', '\"', ri.type_amount, '\"', ', ', "
                    "'\"description\"', ':', '\"', i.description, '\"', ', ', "
                    "'\"image\"', ':', '\"', i.image, '\"', ', ',"
                    "'\"price\"', ':', i.price, "
                "'}' "
            ") "
        ") AS 'ingredients' "
        "FROM recipe_ingredients ri " 
        "JOIN ingredients i ON ri.id_ingredient = i.id " 
        "JOIN recipes r ON ri.id_recipe = r.id " 
        "WHERE id_recipe = %s"
    )
    
    QRY_COUNT_RECIPES_BY_ID = (
        "SELECT COUNT(*) AS 'count' FROM recipes "
        "WHERE id = %s"
    )
    
    QRY_COUNT_INGREDIENTS_BY_RECIPE_ID = (
        "SELECT COUNT(*) AS 'count' FROM recipe_ingredients "
        "WHERE id_recipe = %s"
    )

    QRY_COUNT_RECIPE_INGREDIENT_BY_ID = (
        "SELECT COUNT(*) AS 'count' FROM recipe_ingredients "
        "WHERE id_recipe = %s "
        "AND id_ingredient = %s"
    )

    SQL_INSERT_RECIPE_INGREDIENT= (
        "INSERT INTO recipe_ingredients (amount, type_amount, id_recipe, id_ingredient) "
        "VALUES (%s, %s, %s, %s)"
    )
    
    SQL_DELETE_RECIPE_INGREDIENT = (
        "DELETE FROM recipe_ingredients "
        "WHERE id_recipe = %s AND id_ingredient = %s"
    )