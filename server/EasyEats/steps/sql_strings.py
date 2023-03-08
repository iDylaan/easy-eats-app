class Sql_Strings():
    QRY_STEPS_BY_RECIP_ID = (
        "SELECT id, description, step_number "
        "FROM steps "
        "WHERE id_recipe = %s "
        "ORDER BY step_number"
    )
    
    QRY_RECIPE_EXISTS = (
        "SELECT COUNT(*) AS 'exists' "
        "FROM recipes "
        "WHERE id = %s"
    )
    
    QRY_STEP_BY_ID = (
        "SELECT step_number, id_recipe "
        "FROM steps "
        "WHERE id = %s"
    )
    
    QRY_STEPS_UP_DELETED = (
        "SELECT * FROM steps "
        "WHERE step_number > %s "
        "AND id_recipe = %s"
    )
    
    SQL_INSERT_STEP = (
        "INSERT INTO steps (description, id_recipe) "
        "VALUES (%s, %s)"
    )
    
    SQL_UPDATE_STEP = (
        "UPDATE steps SET "
        "description = %s "
        "WHERE id = %s"
    )
    
    SQL_DELETE_STEP = (
        "DELETE FROM steps "
        "WHERE id = %s"
    )
    
    SQL_UPDATE_STEP_NUMBER = (
        "UPDATE steps SET "
        "step_number = %s "
        "WHERE id = %s"
    )