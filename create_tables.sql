CREATE TABLE users(
    id INTEGER PRIMARY KEY DESC UNIQUE,
    email TEXT UNIQUE,
    first_name TEXT,
    last_name TEXT,
);

CREATE TABLE items(
    id INTEGER PRIMARY KEY DESC UNIQUE,
    title TEXT,
    description TEXT,
    owner_id INTEGER
);

CREATE TABLE wishlist_items(
    id INTEGER PRIMARY KEY DESC UNIQUE,
    name TEXT,
    description TEXT,
    link TEXT,
    price FLOAT,
    owner_id INTEGER
);