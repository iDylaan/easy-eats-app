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
    
    QRY_RECIPE_REVIEWS = (
        "SELECT " 
        	"comment, " 
        	"rating, " 
        	"DATE_FORMAT(date_made, %s) as 'date_made', "
        	"DATE_FORMAT(time_made, %s) as 'datetime_made', "
        	"DATE_FORMAT(time_made, %s) as 'time_made', "
        	"id_recipe, "
        	"id_user "
        "FROM reviews "
        "WHERE id_recipe = %s "
        "ORDER BY time_made DESC"
    )
    
    SQL_INSERT_REVIEW = (
        "INSERT INTO reviews (id_recipe, id_user, rating, comment) "
        "VALUES (%s, %s, %s, %s)"
    )