recipe_review_schema = {
    "comment": {
        "type": "string",
        "maxlength": 300,
        "empty": True,
        "required": False,
        "nullable": True
    },
    "rating": {
        "type": "float",
        "min": 0,
        "max": 5,
        "required": True,
        "empty": False
    },
    "date_made": {
        "type": "date",
        "required": False,
        "empty": True,
        "nullable": True
    },
    "time_made": {
        "type": "datetime",
        "required": False,
        "empty": True,
        "nullable": True
    },
    "id_recipe": {
        "type": "integer",
        "required": True,
        "empty": False
    },
    "id_user": {
        "type": "integer",
        "required": True,
        "empty": False
    }
}