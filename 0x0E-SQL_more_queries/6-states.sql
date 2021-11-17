-- creates the database hbtn_0d_usa
-- the table states (in the database hbtn_0d_usa) on MySQL server
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- selects database
USE hbtn_0d_usa;
-- Creates table states
CREATE TABLE IF NOT EXISTS states(
	id INT PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL
);
