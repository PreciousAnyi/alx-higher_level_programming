-- list all shows, and genres linked to the show
SELECT title, name FROM tv_shows ts
LEFT JOIN tv_show_genres tsg ON ts.id = tsg.show_id
LEFT JOIN tv_genres g ON tsg.genre_id = g.id
ORDER BY title, name;
