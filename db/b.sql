DROP TABLE items;
DROP TABLE orders;
DROP TABLE users;

CREATE TABLE IF NOT EXISTS items(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, price integer);
CREATE TABLE IF NOT EXISTS orders(id INTEGER PRIMARY KEY AUTOINCREMENT, item_id integer, user_id integer);
CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT);


INSERT INTO items(name, price) VALUES('PECHENKA', 200);
INSERT INTO items(name, price) VALUES('MYASO', 400);
INSERT INTO items(name, price) VALUES('BUBLIK', 400);

INSERT INTO users(name) VALUES('VASYA');
INSERT INTO users(name) VALUES('PETYA');
INSERT INTO users(name) VALUES('MISHA');
-- INSERT INTO users(name) VALUES('B');

INSERT INTO orders(item_id, user_id) VALUES(1, 1);
INSERT INTO orders(item_id, user_id) VALUES(2, 1);
INSERT INTO orders(item_id, user_id) VALUES(3, 1);
INSERT INTO orders(item_id, user_id) VALUES(2, 2);
INSERT INTO orders(item_id, user_id) VALUES(3, 2);
-- INSERT INTO orders(item_id, user_id) VALUES(3, 3);

-- SELECT * FROM items 
-- JOIN orders ON items.id = orders.item_id
-- JOIN users ON users.id = orders.user_id

SELECT * FROM users
JOIN orders ON users.id = orders.user_id
JOIN items ON items.id = orders.item_id

-- SELECT * FROM users
-- LEFT JOIN orders ON users.id = orders.user_id
-- LEFT JOIN items ON items.id = orders.item_id

-- WHERE users.name = 'PETYA'
