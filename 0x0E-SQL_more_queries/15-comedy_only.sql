--  lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT tv_shows.title
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
-- The tv_genres table contains only one record where name = Comedy
WHERE tv_genres.name = "comedy"
-- Results must be sorted in ascending order by the show title
ORDER BY tv_shows.title;
