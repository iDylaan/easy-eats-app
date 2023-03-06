CREATE DATABASE IF NOT EXISTS easy_eats_db
  DEFAULT CHARACTER SET utf8mb4
  COLLATE utf8mb4_general_ci;


USE easy_eats_db;


CREATE TABLE rols (
  id INT NOT NULL,
  name VARCHAR(5) NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_General_ci;

INSERT INTO rols (id, name) VALUES 
  (1, 'Admin'),
  (2, 'User');


CREATE TABLE categories (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(50) NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_General_ci;

INSERT INTO categories (name) VALUES 
  ("Comida Mexicana"),
  ("Comida Italiana"),
  ("Comida Japonesa"),
  ("Comida China"),
  ("Comida India"),
  ("Comida Asiática"),
  ("Comida vegetariana"),
  ("Comida rápida"),
  ("Comida saludable"),
  ("Comida para el desayuno");

CREATE TABLE ingredients (
  id INT AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,
  description VARCHAR(300) NOT NULL,
  price NUMERIC(11, 2) DEFAULT NULL,
  image VARCHAR(40) DEFAULT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_General_ci;

INSERT INTO ingredients (name, description, price, image) VALUES 
  ('Arroz', 'Arroz de calidad', 12.50, 'arroz.jpg'),
  ('Tomate', 'Tomate fresco y maduro', 5.00, 'tomate.jpg'),
  ('Pollo', 'Pollo fresco y tierno', 25.00, 'pollo.jpg'),
  ('Lechuga', 'Lechuga verde y fresca', 3.00, 'lechuga.jpg'),
  ('Pan', 'Pan fresco y recién horneado', 7.50, 'pan.jpg');


CREATE TABLE users (
  id INT NOT NULL AUTO_INCREMENT,
  username VARCHAR(15) NOT NULL,
  tagline VARCHAR(9) NOT NULL,
  image VARCHAR(25) DEFAULT NULL,
  name VARCHAR(60) DEFAULT NULL,
  email VARCHAR(60) NOT NULL,
  password VARCHAR(102) NOT NULL,
  date_of_birth DATE NOT NULL,
  height INT DEFAULT NULL,
  weight NUMERIC(5,2) DEFAULT NULL,
  id_rol INT NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (id_rol) REFERENCES rols(id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT,
  UNIQUE KEY (tagline),
  UNIQUE KEY (email)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_General_ci;

INSERT INTO users (id, username, tagline, image, name, email, password, date_of_birth, height, weight, id_rol) VALUES 
  (1, 'johndoe', '34RF3', 'image1.jpg', 'John Doe', 'johndoe@example.com', 'password1', '1990-01-01', 180, 80.3, 1),
  (2, 'janedoe', '4TDGF', 'image2.jpg', 'Jane Doe', 'janedoe@example.com', 'password2', '1995-05-05', 170, 60.77, 2);


CREATE TABLE recipes (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(50) NOT NULL,
  description VARCHAR(300) NOT NULL,
  image VARCHAR(40) NOT NULL,
  cooking_time INT NOT NULL,
  dinners INT NOT NULL,
  update_date DATE DEFAULT CURRENT_DATE,
  yields INT NOT NULL, -- Porciones
  calories INT DEFAULT NULL, -- Calorias
  fats INT DEFAULT NULL, -- Grasas
  carbs INT DEFAULT NULL, -- Carbohidratos
  protein INT DEFAULT NULL, -- Proteinas
  satured_fats INT DEFAULT NULL, -- Grasas saturadas
  sodium INT DEFAULT NULL, -- Sodio
  fiber INT DEFAULT NULL, -- Fibra
  sugars INT DEFAULT NULL, -- Azucares
  budget NUMERIC(11, 2) DEFAULT NULL, -- Presupuesto
  id_user INT NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (id_user) REFERENCES users(id) 
    ON UPDATE CASCADE 
    ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_General_ci;

INSERT INTO recipes (name, description, image, cooking_time, dinners, update_date, yields, calories, budget, id_user) VALUES 
  ('Receta 1', 'Esta es una descripción de la receta 1', 'imagen1.jpg', 30, 4, '2023-02-06', 4, 500, 10.5, 1),
  ('Receta 2', 'Esta es una descripción de la receta 2', 'imagen2.jpg', 60, 2, '2023-02-06', 2, 700, 15.0, 2);
 
 
CREATE TABLE steps (
  id INT AUTO_INCREMENT,
  description VARCHAR(300) NOT NULL,
  step_number INT NOT NULL DEFAULT 0,
  id_recipe INT NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (id_recipe) REFERENCES recipes(id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_General_ci;

INSERT INTO steps (description, step_number, id_recipe) VALUES
  ("Para la salsa, licúa el puré de tomate con las hierbas finas, el agua y el Concentrado de Tomate con Pollo CONSOMATE®; cocina hasta que espese ligeramente.", 1, 1),
  ("Para el relleno, calienta 2 cucharadas de aceite, fríe la cebolla con el ajo hasta que cambien de color, agrega la carne, el Jugo MAGGI®, la Salsa Tipo Inglesa CROSSE & BLACKWELL® y la sal con cebolla; cocina por 8 minutos o hasta que la carne esté cocida.", 2, 1),
  ("En una sartén, unta el aceite restante, vierte un poco de la salsa, añade una capa de 3 láminas de pasta, una de relleno, otra de salsa y una más de queso; repite el procedimiento hasta terminar con el resto de los ingredientes.", 3, 1),
  ("Tapa y cocina a fuego bajo por 17 minutos. Decora con el perejil y ofrece.", 4, 1);


CREATE TABLE recipe_categories (
  id_recipe INT NOT NULL,
  id_category INT NOT NULL,
  CONSTRAINT fk_recipe_categories_recipe_id FOREIGN KEY (id_recipe) REFERENCES recipes(id),
  CONSTRAINT fk_recipe_categories_category_id FOREIGN KEY (id_category) REFERENCES categories(id)
);


INSERT INTO recipe_categories (id_category, id_recipe) VALUES 
(1, 1), (2, 1), (3, 2), (4, 2), (9, 2), (10, 2);


CREATE TABLE reviews (
  id INT AUTO_INCREMENT,
  comment VARCHAR(300) DEFAULT NULL,
  rating NUMERIC(2, 1) DEFAULT NULL,
  date_made DATE DEFAULT CURRENT_DATE,
  time_made DATETIME DEFAULT NOW(),
  edited BOOL DEFAULT false,
  underground BOOL DEFAULT false,
  id_recipe INT NOT NULL,
  id_user INT NOT NULL,
  CONSTRAINT fk_reviews_recipe_id FOREIGN KEY (id_recipe) REFERENCES recipes(id),
  CONSTRAINT fk_reviews_user_id FOREIGN KEY (id_user) REFERENCES users(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_General_ci;



INSERT INTO reviews (comment, rating, id_recipe, id_user) VALUES 
  ("Excelente receta, muy fácil de seguir.", 4.5, 1, 1),
  ("Esta receta es un poco aburrida, pero la comida resultó buena.", 3.0, 1, 2),
  ("Esta receta es un fracaso, no me gustó nada.", 2.0, 2, 1),
  ("Esta receta es increíble, la recomiendo altamente.", 5.0, 2, 2),
  ("Esta receta es buena, pero necesita más sabor.", 3.5, 2, 1);


CREATE TABLE recipe_ingredients (
  amount INT NOT NULL,
  type_amount VARCHAR(20) NOT NULL,
  id_recipe INT NOT NULL,
  id_ingredient INT NOT NULL,
  CONSTRAINT fk_recipe_ingredient_recipe_id FOREIGN KEY (id_recipe) REFERENCES recipes(id),
  CONSTRAINT fk_recipe_ingredient_ingredient_id FOREIGN KEY (id_ingredient) REFERENCES ingredients(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_General_ci;

INSERT INTO recipe_ingredients(amount, type_amount, id_recipe, id_ingredient) VALUES
  (1500, 'gr', 1, 1),
  (8, 'piezas', 1, 2),
  (4, 'muslos', 1, 3),
  (3, 'piezas', 1, 4),
  (1, 'pieza', 1, 5);


CREATE TABLE utensils (
  id INT AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,
  image VARCHAR(40) DEFAULT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_General_ci;

INSERT INTO utensils (name, image) VALUES
  ("Olla", "olla1.jpg"),
  ("Sartén", "sarten1.jpg"),
  ("Cuchillo", "cuchillo1.jpg"),
  ("Taza de medir", "tazamedir1.jpg"),
  ("Tabla de cortar", "tablacortar1.jpg");


CREATE TABLE recipe_utensils (
  id_recipe INT NOT NULL,
  id_utensil INT NOT NULL,
  CONSTRAINT fk_recipe_utensils_recipe_id FOREIGN KEY(id_recipe) REFERENCES recipes(id),
  CONSTRAINT fk_recipe_utensils_utensil_id FOREIGN KEY(id_utensil) REFERENCES utensils(id)
);

INSERT INTO recipe_utensils (id_recipe, id_utensil) VALUES
(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 5);

CREATE TABLE favorite_recipes (
  id_recipe INT NOT NULL,
  id_user INT NOT NULL,
  CONSTRAINT fk_favorite_recipes_recipe_id FOREIGN KEY(id_recipe) REFERENCES recipes(id),
  CONSTRAINT fk_favorite_recipes_user_id FOREIGN KEY(id_user) REFERENCES users(id)
);

INSERT INTO easy_eats_db.favorite_recipes (id_recipe, id_user) VALUES
(1, 1),
(2, 1);


-- INDICES --
CREATE INDEX idx_email ON users (email);
CREATE INDEX idx_auth ON users (id, email, password, id_rol, username, tagline);
CREATE INDEX idx_username_tagline ON users (username, tagline);



-- TRIGGERS --
-- Trigger para insertar un paso de una receta
DELIMITER $$
CREATE TRIGGER before_insert_steps
BEFORE INSERT ON steps
FOR EACH ROW
BEGIN
  SET NEW.step_number = (
    SELECT COUNT(*) + 1
    FROM steps
    WHERE id_recipe = NEW.id_recipe
  );
END$$
DELIMITER ;