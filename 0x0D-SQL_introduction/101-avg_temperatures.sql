-- displays the average temperature (Fahrenheit)
SELECT city, AVG(value) AS "avg_temp"
FROM temperatures
GROUP BY city
-- ordered by city ordered by temperature (descending).
ORDER BY avg_temp DESC;
