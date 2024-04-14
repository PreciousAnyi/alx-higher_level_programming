-- Lists all shows contained in the database
SELECT tv_shows.title, tsg.genre_id FROM tv_shows JOIN
tv_show_genres tsg ON tv_shows.id = tsg.show_id JOIN
tv_genres genres ON tsg.genre_id = genres.id
ORDER BY tv_shows.title, tsg.genre_id;
