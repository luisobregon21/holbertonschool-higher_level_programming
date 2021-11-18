--  uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT tv_genres.name AS 'name'
FROM  tv_genres
INNER JOIN tv_show_genres ON tv_genres.id =  tv_show_genres.genre_id
INNER JOIN tv_shows ON  tv_show_genres.show_id = tv_shows.id
-- The tv_shows table contains only one record where title = Dexter
WHERE tv_shows.title = 'Dexter'
ORDER BY name;
