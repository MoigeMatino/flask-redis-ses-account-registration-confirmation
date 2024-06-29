CREATE DATABASE users_prod;
CREATE DATABASE users_stage;
CREATE DATABASE users_dev;
CREATE DATABASE users_test;

\c users_dev;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    confirmed BOOLEAN NOT NULL DEFAULT false,
    email_sent BOOLEAN NOT NULL DEFAULT false
);
