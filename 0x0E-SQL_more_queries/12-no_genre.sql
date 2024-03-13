-- lists all shows in the database
SELECT tvs.title, tsg.genre_id FROM tv_shows tvs
LEFT JOIN tv_show_genres tsg ON tvs.id = tsg.show_id
WHERE tsg.genre_id IS NULL
ORDER BY tvs.title, tsg.genre_id;
