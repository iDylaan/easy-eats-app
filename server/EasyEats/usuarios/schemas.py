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
        "tpye": "string",
        "required": False,
        "empty": True
    },
    "name": {
        "type": "string",
        "minlength": 3,
        "required": True,
        "empty": False
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
        "type": "datetime", # Siempre formatos ISO 8601
        "required": True,
        "empty": False
    },
    "height": {
        "type": "integer",
        "required": False,
        "empty": True
    },
    "width": {
        "type": "integer",
        "required": False,
        "empty": True
    },
    "id_rol": {
        "type": "integer",
        "required": True,
        "empty": False
    }
}

