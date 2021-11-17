-- lists all the cities of California
-- that can be found in the database hbtn_0d_usa
SELECT id,name
-- syntax: SELECT (name) FROM tableName WHERE condition;
FROM cities WHERE state_id = (
	SELECT id
	FROM states
	WHERE name = "California"
)
-- sort the data in ascending or descending order,based on one or more columns.
ORDER BY cities.id;
