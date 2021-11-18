-- lists all cities contained in the database hbtn_0d_usa
SELECT cities.id, cities.name, states.name
-- return the records that are shared
FROM cities INNER JOIN states
ON cities.state_id = states.id
-- sorted in ascending order by cities.id
ORDER BY cities.id;
