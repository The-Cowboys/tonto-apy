CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    email text NOT NULL UNIQUE,
    hash text NOT NULL,
    estado text NOT NULL,
    rol text NOT NULL,
    created timestamptz NOT NULL
);