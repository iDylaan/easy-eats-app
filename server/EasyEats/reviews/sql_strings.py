class Sql_Strings():
    QRY_REVIEWS = (
        "SELECT "
        "r.*, u.name as 'name', "
        "CONCAT(u.username, '#', u.tagline) as 'username' "
        "FROM "
            "reviews r "
            "JOIN users u "
        "ORDER BY r.time_made DESC"
    )
    
    SQL_INSERT_REVIEW = (
        "INSERT INTO reviews (id_recipe, id_user, rating, comment) "
        "VALUES (%s, %s, %s, %s)"
    )