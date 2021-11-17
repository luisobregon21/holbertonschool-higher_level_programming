-- creates the table id_not_null on MySQL server.
CREATE TABLE IF NOT EXISTS id_not_null (
-- gives default value of 1
	id INT DEFAULT 1,
	name VARCHAR(256)
);
