CREATE DATABASE IF NOT EXISTS login;

USE login;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARBINARY(255) NOT NULL
);

INSERT INTO users (username, password) VALUES ('guest', UNHEX(MD5('guest')));
INSERT INTO users (username, password) VALUES ('admin', UNHEX(MD5('asf@12nDFS_di')));
