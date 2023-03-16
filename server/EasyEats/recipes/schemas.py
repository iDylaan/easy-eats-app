recipe_schema = {
    "id": {
        "type": "integer",
        "required": False,
        "empty": True,
    },
    "name": {
        "type": "string",
        "minlength": 4,
        "maxlength": 50,
        "required": True,
        "empty": False
    },
    "description": {
        "type": "string",
        "minlength": 25,
        "maxlength": 300,
        "required": False,
        "empty": True,
    },
    "cooking_time": {
        "type": "integer",
        "required": True,
        "empty": False
    },
    "dinners": {
        "type": "integer",
        "required": True,
        "empty": False
    },
    "image": {
        "type": "string",
        "required": False,
        "empty": True,
        "nullable": True
    },
    "update_date": {
        "type": "date",
        "required": False,
        "empty": True,
        "nullable": True
    },
    "calories": {
        "type": "integer",
        "required": False,
        "empty": True,
        "nullable": True
    },
    "fats": {
        "type": "integer",
        "required": False,
        "empty": True,
        "nullable": True
    },
    "carbs": {
        "type": "integer",
        "required": False,
        "empty": True,
        "nullable": True
    },
    "protein": {
        "type": "integer",
        "required": False,
        "empty": True,
        "nullable": True
    },
    "satured_fats": {
        "type": "integer",
        "required": False,
        "empty": True,
        "nullable": True
    },
    "sodium": {
        "type": "integer",
        "required": False,
        "empty": True,
        "nullable": True
    },
    "fiber": {
        "type": "integer",
        "required": False,
        "empty": True,
        "nullable": True
    },
    "sugars": {
        "type": "integer",
        "required": False,
        "empty": True,
        "nullable": True
    },
    "budget": {
        "type": "float",
        "required": False,
        "empty": True,
        "nullable": True,
        "coerce": float,
        "max": 999999999.99,
        "min": -999999999.99,
        "regex": "^-?[0-9]{1,9}(\\.[0-9]{1,2})?$"
    },
    "banned": {
        "type": "boolean",
        "required": False,
        "empty": True,
        "nullable": True
    },
    "id_user": {
        "type": "integer",
        "required": True,
        "empty": False
    }
}