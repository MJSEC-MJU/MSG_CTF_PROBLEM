
DROP DATABASE IF EXISTS testdb;
CREATE DATABASE testdb;
USE testdb;


CREATE TABLE test_table (
    name VARCHAR(64),
    uid VARCHAR(32),
    upassword VARCHAR(128),
    body TEXT
);


INSERT INTO test_table (uid, upassword, name, body) VALUES
    ('admin', SUBSTRING(MD5(RAND()), 1, 24), 'nayoung', 'This is a body for admin'),
    ('guest', 'guest', 'guest', 'Body text for guest, user guest'),
    ('jiyoon', 'y8R^Nwz5L&1X', 'jiyoonjung', 'This is a body for jiyoon'),
    ('jongyoon', 'U9oK7c1Tx@V2', 'jongyoonlee', 'This is a body for jongyoon'),
    ('MJSEC', 'R#4tWg3Pz0qZ', 'MJSEC', 'This is a body for MJSEC');

CREATE TABLE important_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    description TEXT
);

INSERT INTO important_table (name, description) VALUES
    ('Test Item 1', 'This is a description for Test Item 1'),
    ('Test Item 2', 'This is a description for Test Item 2'),
    ('Test Item 3', 'This is a description for Test Item 3');

CREATE TABLE secret_table (
    code VARCHAR(10),
    value DECIMAL(10, 2)
);

INSERT INTO secret_table (code, value) VALUES
    ('A123', 123.45),
    ('B456', 678.90),
    ('C789', 234.56);

