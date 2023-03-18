recipe_step_schema = {
    "id": {
        "type": "integer",
        "required": False,
        "empty": True
    },
    "description": {
        "type": "string",
        "required": True,
        "empty": False,
        "maxlength": 300
    },
    "step_number": {
        "type": "integer",
        "required": False,
        "empty": True
    },
    "id_recipe": {
        "type": "integer",
        "required": True,
        "empty": False
    }
}
