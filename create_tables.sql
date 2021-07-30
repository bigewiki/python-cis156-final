CREATE TABLE users(
    id INTEGER PRIMARY KEY DESC UNIQUE,
    email TEXT UNIQUE,
    hashed_password TEXT,
    is_active INTEGER
);

CREATE TABLE items(
    id INTEGER PRIMARY KEY DESC UNIQUE,
    title TEXT,
    description TEXT,
    owner_id INTEGER
);