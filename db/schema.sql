
CREATE TABLE users(id INTEGER PRIMARY KEY,
                   username TEXT,
                   password TEXT
                   );




CREATE TABLE pizza_providers(id INTEGER PRIMARY KEY,
                             name TEXT
                             );



CREATE TABLE pizza_sizes(id INTEGER PRIMARY KEY,
                         size INTEGER
                         );

CREATE TABLE crusts(id INTEGER PRIMARY KEY,
                    name TEXT
                    );

CREATE TABLE toppings(id INTEGER PRIMARY KEY,
                      name TEXT,
                      quantity INTEGER
                      );



CREATE TABLE orders(id INTEGER PRIMARY KEY,
                    average_price DOUBLE,
                    user_id INTEGER,
                    timestamp DATETIME
                    );


INSERT INTO users VALUES (NULL, 'claire', 'NOOOOOOOOOO');
