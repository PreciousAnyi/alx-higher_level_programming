-- lists all genres in the database
SELECT g.name AS 'genre', COUNT(tsg.genre_id) AS 'number_of_shows'
FROM tv_genres g RIGHT JOIN tv_show_genres tsg ON g.id = tsg.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
