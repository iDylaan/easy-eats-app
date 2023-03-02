class Sql_Strings():
    QRY_COUNT_RECIPES_BY_ID = (
        "SELECT COUNT(*) AS 'count' FROM recipes "
        "WHERE id = %s"
    )