-- creates the database hbtn_0d_usa
-- the table cities (in the database hbtn_0d_usa) on MySQL server.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- select DATABASE hbtn_0d_usa
USE hbtn_0d_usa;
-- Create the table cities
CREATE TABLE IF NOT EXISTS cities(
-- AUTO_INCREMENT generate a unique identity for new rows:
	id INT PRIMARY KEY AUTO_INCREMENT,
	state_id INT NOT NULL,
-- foreign key is a constraint that links a column in one table
-- to a column in a different table and ensures that a value can be added
-- to column_a only if the same value already exists in column_b.
	FOREIGN KEY(state_id) REFERENCES states(id),
	name VARCHAR(256) NOT NULL
);
