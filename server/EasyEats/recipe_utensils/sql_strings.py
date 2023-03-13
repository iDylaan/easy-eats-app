class Sql_Strings():
    QRY_RECIPES_UTENSILS = (
        "SELECT "
            "rc.id AS 'recipe_id', "
            "rc.name AS 'recipe_name', "
            "GROUP_CONCAT( "
                "DISTINCT CONCAT( "
                    "'{ "
                        "\"id_utensil\":', u.id, ', "
                        "\"utensil\":\"', u.name, '\", "
                        "\"image\":\"', u.image, '\""
                    "}' "
                ") "
                "ORDER BY u.name "
                "SEPARATOR ',' "
            ") AS 'utensils' "
        "FROM "
            "recipes rc "
            "JOIN recipe_utensils ru ON rc.id = ru.id_recipe "
            "JOIN utensils u ON ru.id_utensil = u.id "
        "GROUP BY rc.id "
    )
    
    QRY_RECIPE_UTENSILS = (
        "SELECT "
        "ru.id_recipe, "
        "CONCAT( " 
            "GROUP_CONCAT( " 
                "'{', "
                    "'\"id_utensil\"', ':', u.id, ', ', "
                    "'\"utensil\"', ':', '\"', u.name, '\"', ', ', "
                    "'\"image\"', ':', '\"', u.image, '\"', "
                "'}' "
            ") "
        ") AS 'utensils' "
        "FROM recipe_utensils ru "
        "JOIN utensils u ON ru.id_utensil = u.id "
        "WHERE ru.id_recipe = %s;"
    )
    
    QRY_COUNT_RECIPES_BY_ID = (
        "SELECT COUNT(*) AS 'count' FROM recipes "
        "WHERE id = %s"
    )
    
    QRY_COUNT_UTENISL_BY_ID = (
        "SELECT COUNT(*) AS 'count' FROM recipe_utensils "
        "WHERE id_utensil = %s"
    )
    
    QRY_COUNT_RECIPE_UTENSIL_BY_ID = (
        "SELECT COUNT(*) AS 'count' FROM recipe_utensils "
        "WHERE id_recipe = %s "
        "AND id_utensil = %s"
    )
    
    SQL_INSERT_RECIPE_UTENSIL = (
        "INSERT INTO recipes_utensils (id_recipe, recipe_utensil) "
        "VALUES (%s, %s)"
    )
    
    SQL_DELETE_RECIPE_UTENSIL = (
        "DELETE FROM recipe_utensils "
        "WHERE id_recipe = %s "
        "AND id_utensil = %s"
    )