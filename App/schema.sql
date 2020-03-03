DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;
DROP TABLE IF EXISTS kart;
DROP TABLE IF EXISTS products;

CREATE TABLE user(
		user_id INTEGER PRIMARY KEY AUTOINCREMENT,
		password TEXT,
		email TEXT UNIQUE NOT NULL,
		username TEXT UNIQUE NOT NULL
		);

CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);

CREATE TABLE kart
		(user_id INTEGER,
		product_id INTEGER,
		FOREIGN KEY(user_id) REFERENCES user(user_id),
		FOREIGN KEY(product_id) REFERENCES product(product_id)
		);

CREATE TABLE products
(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
name TEXT,
price REAL,
description TEXT,
image TEXT,
stock INTEGER
);

INSERT INTO products (name, price, description, image, stock)
VALUES ('Fossil', 125, 'Analog Watch', 'static/images/Watch.jpg', 15);

INSERT INTO products (name, price, description, image, stock)
VALUES ('Reebok', 54, 'Formal Wear', 'static/images/shoe.jpeg', 15);

INSERT INTO products (name, price, description, image, stock)
VALUES ('Levis', 75, 'Casual T-Shirt', 'static/images/t-shirt.jpg', 7);

INSERT INTO products (name, price, description, image, stock)
VALUES ('H & M', 125, 'Formal Pant', 'static/images/pant.jpg', 13);

