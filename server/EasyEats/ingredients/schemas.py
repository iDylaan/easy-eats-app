ingredient_schema = {
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
    "description": {
        "type": "string",
        "minlength": 50,
        "maxlength": 300,
        "required": True,
        "empty": False
    },
    "price": {
        "type": "float",
        "regex": r"^\d{1,9}(\.\d{1,2})?$",
        "required": False,
        "empty": True,
        "nullable": True
    },
    
    "image": {
        "type": "string",
        "required": False,
        "empty": True,
        "nullable": True
    },
}

