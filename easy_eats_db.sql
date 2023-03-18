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
  banned BOOL DEFAULT 0,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_General_ci;



CREATE TABLE ingredients (
  id INT AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,
  description VARCHAR(300) NOT NULL,
  price NUMERIC(11, 2) DEFAULT NULL,
  image_name VARCHAR(100) DEFAULT NULL,
  image_bit LONGBLOB DEFAULT NULL,
  banned BOOL DEFAULT 0,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_General_ci;


CREATE TABLE users (
  id INT NOT NULL AUTO_INCREMENT,
  username VARCHAR(15) NOT NULL,
  tagline VARCHAR(9) NOT NULL,
  image_name VARCHAR(100) DEFAULT NULL,
  image_bit LONGBLOB DEFAULT NULL,
  name VARCHAR(60) DEFAULT NULL,
  email VARCHAR(60) NOT NULL,
  password VARCHAR(102) NOT NULL,
  date_of_birth DATE NOT NULL,
  height INT DEFAULT NULL,
  weight NUMERIC(5,2) DEFAULT NULL,
  banned BOOL DEFAULT 0,
  id_rol INT NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (id_rol) REFERENCES rols(id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT,
  UNIQUE KEY (tagline),
  UNIQUE KEY (email)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_General_ci;


CREATE TABLE recipes (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(50) NOT NULL,
  description VARCHAR(300) NOT NULL,
  cooking_time INT NOT NULL, -- tiempo de preparacion
  dinners INT NOT NULL, -- personas
  image_name VARCHAR(100) DEFAULT NULL,
  image_bit LONGBLOB DEFAULT NULL,
  update_date DATE DEFAULT CURRENT_DATE, -- fecha de creacion
  calories INT DEFAULT NULL, -- Calorias
  fats INT DEFAULT NULL, -- Grasas
  carbs INT DEFAULT NULL, -- Carbohidratos
  protein INT DEFAULT NULL, -- Proteinas
  satured_fats INT DEFAULT NULL, -- Grasas saturadas
  sodium INT DEFAULT NULL, -- Sodio
  fiber INT DEFAULT NULL, -- Fibra
  sugars INT DEFAULT NULL, -- Azucares
  budget NUMERIC(11, 2) DEFAULT NULL, -- Presupuesto
  banned BOOL DEFAULT 0,
  id_user INT NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (id_user) REFERENCES users(id) 
    ON UPDATE CASCADE 
    ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_General_ci;

 
 
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
  edited BOOL DEFAULT 0,
  banned BOOL DEFAULT 0,
  id_recipe INT NOT NULL,
  id_user INT NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT fk_reviews_recipe_id FOREIGN KEY (id_recipe) REFERENCES recipes(id),
  CONSTRAINT fk_reviews_user_id FOREIGN KEY (id_user) REFERENCES users(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_General_ci;



CREATE TABLE recipe_ingredients (
  amount INT NOT NULL,
  type_amount VARCHAR(20) NOT NULL,
  id_recipe INT NOT NULL,
  id_ingredient INT NOT NULL,
  CONSTRAINT fk_recipe_ingredient_recipe_id FOREIGN KEY (id_recipe) REFERENCES recipes(id),
  CONSTRAINT fk_recipe_ingredient_ingredient_id FOREIGN KEY (id_ingredient) REFERENCES ingredients(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_General_ci;



CREATE TABLE utensils (
  id INT AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,
  image_name VARCHAR(100) DEFAULT NULL,
  image_bit LONGBLOB DEFAULT NULL,
  banned BOOL DEFAULT 0,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_General_ci;



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