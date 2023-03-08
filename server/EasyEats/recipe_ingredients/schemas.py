recipe_ingredient_schema = {
    "amount": {
        "type": "integer",
        "required": True,
        "empty": False
    },
    "type_amount": {
        "type": "string",
        "required": True,
        "empty": False,
        "maxlength": 20
    },
    "id_recipe": {
        "type": "integer",
        "required": True,
        "empty": False
    },
    "id_ingredient": {
        "type": "integer",
        "required": True,
        "empty": False
    }
}
