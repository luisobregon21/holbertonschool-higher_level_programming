-- creates the database hbtn_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- creates user user_0d_2 in server localhost
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost'
-- sets the password for the user
IDENTIFIED BY 'user_0d_2_pwd';
-- Grants users priveledges...
-- SELECT allows to read through databases
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
