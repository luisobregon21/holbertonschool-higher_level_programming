-- displays the top 3 of cities temperature during July and August
SELECT city, AVG(value) AS "avg_temp"
FROM temperatures
-- July and August
WHERE month = 7 || month = 8
GROUP BY city
-- ordered by temperature (descending)
ORDER BY avg_temp DESC
-- chooses the top 3
LIMIT 3;
