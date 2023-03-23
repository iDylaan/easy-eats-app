import os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

### Cargar configuracion ###
load_dotenv(".env")
### Cargar App ###
app = Flask(__name__)

### CORS (Cross-Origin Resource Sharing) ### 
# CORS(app, supports_credentials=True, origins="*")
CORS(app)

### SQL ALCHEMY ###
# app.config['SQLALCHEMY_DATABASE_URI'] = '{}://{}:{}@{}:{}/{}'.format(
#     os.getenv("MARIA_TIPO_DB"),
#     os.getenv("MARIA_USER"),
#     os.getenv("MARIA_PASS"),
#     os.getenv("MARIA_HOST"),
#     os.getenv("MARIA_PORT"),
#     os.getenv("MARIA_DB")
# )
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

### MARIA DB ###
app.config['MARIA_TIPO_DB'] = os.getenv("MARIA_TIPO_DB")
app.config['MARIA_USER'] = os.getenv("MARIA_USER")
app.config['MARIA_PASS'] = os.getenv("MARIA_PASS")
app.config['MARIA_HOST'] = os.getenv("MARIA_HOST")
app.config['MARIA_DB'] = os.getenv("MARIA_DB")
app.config['MARIA_PORT'] = os.getenv("MARIA_PORT")
app.config['MARIA_CHARSET'] = os.getenv("MARIA_CHARSET")

### JWT ###
app.config['SECRET_JWT_KEY'] = os.getenv("SECRET_JWT_KEY")

### ROUTER ###
from EasyEats.login_signin.routes import mod as mod_login_signin
from EasyEats.users.routes import mod as mod_users
from EasyEats.recipes.routes import mod as mod_recipes
from EasyEats.ingredients.routes import mod as mod_ingredients
from EasyEats.categories.routes import mod as mod_categories
from EasyEats.utensils.routes import mod as mod_utensils
from EasyEats.recipe_ingredients.routes import mod as mod_recipe_ingredients
from EasyEats.recipe_categories.routes import mod as mod_recipe_categories
from EasyEats.recipe_utensils.routes import mod as mod_recipe_utensils
from EasyEats.favorite_recipes.routes import mod as mod_favorite_recipes
from EasyEats.steps.routes import mod as mod_steps
from EasyEats.reviews.routes import mod as mod_reviews

### BLUEPRINTS ###
app.register_blueprint(mod_login_signin)
app.register_blueprint(mod_users)
app.register_blueprint(mod_recipes)
app.register_blueprint(mod_ingredients)
app.register_blueprint(mod_categories)
app.register_blueprint(mod_utensils)
app.register_blueprint(mod_recipe_ingredients)
app.register_blueprint(mod_recipe_categories)
app.register_blueprint(mod_recipe_utensils)
app.register_blueprint(mod_favorite_recipes)
app.register_blueprint(mod_steps)
app.register_blueprint(mod_reviews)