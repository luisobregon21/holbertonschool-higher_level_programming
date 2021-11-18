-- lists all genres from hbtn_0d_tvshows
-- displays the number of shows linked to each.
SELECT tv_genres.name AS "genre", COUNT(tv_show_genres.show_id) AS number_of_shows
-- returns all records that are commonly shared between two tables
-- or those records that exist in both tables that match the ON condition.
FROM tv_genres INNER JOIN tv_show_genres
ON  tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
-- describe the list of column definitions for specified table.
ORDER BY number_of_shows DESC;
