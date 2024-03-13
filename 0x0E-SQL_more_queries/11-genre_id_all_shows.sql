-- lists all shows in the database
SELECT tvs.title, tsg.genre_id FROM tv_shows tvs
LEFT JOIN tv_show_genres tsg ON tvs.id = tsg.show_id
LEFT JOIN tv_genres g ON tsg.genre_id = g.id
ORDER BY tvs.title, tsg.genre_id;
