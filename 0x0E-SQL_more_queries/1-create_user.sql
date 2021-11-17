-- creates the MySQL server user user_0d_1.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
-- set the password
IDENTIFIED BY 'user_0d_1_pwd';
-- gives all priveleges 
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
