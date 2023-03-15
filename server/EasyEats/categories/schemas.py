category_schema = {
    "id": {
        "type": "integer",
        "required": False,
        "empty": True
    },
    "name": {
        "type": "string",
        "minlength": 3,
        "maxlength": 50,
        "required": True,
        "empty": False
    }
}

