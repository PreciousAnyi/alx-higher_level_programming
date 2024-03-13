-- lists all comedy shows in the database
SELECT title FROM tv_shows ts
LEFT JOIN tv_show_genres tsg ON ts.id = tsg.show_id
LEFT JOIN tv_genres g ON tsg.genre_id = g.id
WHERE g.name = 'Comedy'
GROUP BY ts.title
ORDER BY ts.title;
