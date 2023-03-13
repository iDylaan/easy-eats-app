user_schema = {
    "id": {
        "type": "integer",
        "required": False,
        "empty": True
    },
    "username": {
        "type": "string",
        "minlength": 2,
        "required": True,
        "empty": False
    },
    "tagline": {
        "type": "string",
        "minlength": 4,
        "maxlength": 5,
        "required": True,
        "empty": False
    },
    "image": {
        "type": "string",
        "required": False,
        "empty": True,
        "nullable": True
    },
    "name": {
        "type": "string",
        "minlength": 3,
        "required": False,
        "empty": True,
        "nullable": True
    },
    "email": {
        "type": "string",
        "required": True,
        "empty": False,
        "regex": "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    },
    "password": {
        "type": "string",
        "minlength": 8,
        "required": True,
        "empty": False
    },
    "date_of_birth": {
        "type": "date", # Siempre formatos ISO 8601
        "required": True,
        "empty": False
    },
    "height": {
        "type": "integer",
        "required": False,
        "empty": True,
        "nullable": True
    },
    "weight": {
        "type": "integer",
        "required": False,
        "empty": True,
        "nullable": True
    },
    "id_rol": {
        "type": "integer",
        "required": True,
        "empty": False
    }
}

