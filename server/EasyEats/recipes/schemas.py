recipe_schema = {
    "id": {
        "type": "integer",
        "required": False,
        "empty": True
    },
    "name": {
        "type": "string",
        "minlength": 3,
        "maxlength": 100,
        "required": True,
        "empty": False
    },
    "image": {
        "type": "string",
        "required": False,
        "empty": True,
        "nullable": True
    }
}