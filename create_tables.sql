CREATE TABLE users(
    id INTEGER PRIMARY KEY DESC UNIQUE,
    email TEXT UNIQUE,
    first_name TEXT,
    last_name TEXT,
);

CREATE TABLE wishlist_items(
    id INTEGER PRIMARY KEY DESC UNIQUE,
    name TEXT,
    description TEXT,
    link TEXT,
    price FLOAT,
    owner_id INTEGER
);