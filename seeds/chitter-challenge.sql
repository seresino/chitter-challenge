-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS person;
DROP SEQUENCE IF EXISTS person_id_seq;
DROP TABLE IF EXISTS peep;
DROP SEQUENCE IF EXISTS peep_id_seq;


-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS person_id_seq;
CREATE TABLE person (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    username VARCHAR(255) UNIQUE,
    email VARCHAR(255) UNIQUE,
    password VARCHAR(255)
);

CREATE SEQUENCE IF NOT EXISTS peep_id_seq;
CREATE TABLE peep (
    id SERIAL PRIMARY KEY,
    content VARCHAR(255),
    post_time TIMESTAMP,
    user_id INT
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO person (name, username, email, password) VALUES 
('John Doe', 'johndoe', 'johndoe@example.com', 'password123'),
('Alice Smith', 'alicesmith', 'alicesmith@example.com', 'securepass'),
('Bob Johnson', 'bjohnson', 'bjohnson@example.com', 'mysecretpassword');

INSERT INTO peep (content, post_time, user_id) VALUES
('Hello, world!', '2023-12-05 14:30:00', '1'),
('This is a test post.', '2023-12-05 15:45:00', '2'),
('Another post here.', '2023-12-06 09:15:00', '3');