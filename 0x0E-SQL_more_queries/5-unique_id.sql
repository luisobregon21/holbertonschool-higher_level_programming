-- creates the table unique_id on MySQL server.
CREATE TABLE IF NOT EXISTS unique_id(
-- makes id unique
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
);
