class Sql_Strings():
    QRY_ALL_CATEGORIES = (
        "SELECT rc.id_recipe, "
        "GROUP_CONCAT(c.name SEPARATOR ',') AS categories "
        "FROM recipe_categories rc "
        "JOIN categories c ON rc.id_category = c.id "
        "GROUP BY rc.id_recipe"
    )
    
    QRY_CATEGORIES_BY_RECIPE_ID = (
        "SELECT rc.id_recipe, "
        "GROUP_CONCAT(c.name SEPARATOR ',') AS categories "
        "FROM recipe_categories rc "
        "JOIN categories c ON rc.id_category = c.id "
        "WHERE rc.id_recipe = %s"
    )

    QRY_CATEGORY_BY_ID = (
        "SELECT * FROM categories "
        "WHERE id = %s"
    )

    SQL_INSERT_RECIPE_CATEGORIES = (
        "INSERT INTO recipe_categories VALUES {}"
    )
    
    SQL_DELETE_RECIPE_CATEGORY = (
        "DELETE FROM recipe_categories "
        "WHERE id_recipe = %s AND id_category = %s"
    )