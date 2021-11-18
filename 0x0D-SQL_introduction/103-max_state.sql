-- displays the max temperature of each state
SELECT state, MAX(value) AS "max_temp"
FROM temperatures
GROUP BY state
-- ordered by State name
ORDER BY state;
