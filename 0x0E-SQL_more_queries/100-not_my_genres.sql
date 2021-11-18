-- shows without the genre Comedy in the database hbtn_0d_tvshows.
SELECT tv_genres.name
FROM tv_genres
WHERE  tv_genres.name NOT IN
	(
	SELECT tv_genres.name
	FROM tv_genres
	INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
	INNER JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
-- The tv_shows table contains only one record where title = Dexter
	WHERE tv_shows.title = 'Dexter'
)
-- sorted in ascending order by the genre name
ORDER BY name;
