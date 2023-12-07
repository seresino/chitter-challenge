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
    email VARCHAR(255),
    password VARCHAR(255),
    logged_in BOOLEAN
);

CREATE SEQUENCE IF NOT EXISTS peep_id_seq;
CREATE TABLE peep (
    id SERIAL PRIMARY KEY,
    content VARCHAR(255),
    post_time TIMESTAMP,
    user_id INT
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO person (name, email, password, logged_in)
VALUES
    ('John Doe', 'johndoe@example.com', 'password123', true),
    ('Jane Smith', 'janesmith@example.com', 'securepass456', false),
    ('Alice Johnson', 'alice@example.com', 'mysecret789', true),
    ('Bob Brown', 'bobbrown@example.com', 'superpass321', false),
    ('Eva Williams', 'eva@example.com', 'topsecret987', true);

INSERT INTO peep (content, post_time, user_id)
VALUES
    ('Just had a delicious dinner!', '2023-12-07 18:30:00', 1),
    ('Working on a new project. Exciting times!', '2023-12-07 14:45:00', 2),
    ('Hiking in the mountains today. The view is breathtaking!', '2023-12-06 10:15:00', 3),
    ('Celebrating my birthday with friends tonight!', '2023-12-05 20:00:00', 4),
    ('Reading a great book. Can''t put it down!', '2023-12-05 12:20:00', 5),
    ('Watching my favorite movie for the 100th time!', '2023-12-04 19:55:00', 1);