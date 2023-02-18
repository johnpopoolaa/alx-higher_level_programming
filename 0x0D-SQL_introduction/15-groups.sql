-- this script lists the number of records with the same score in the table of a database in your MySQL server.
SELECT score, COUNT(score) as 'number'
FROM second_table
GROUP BY score
ORDER BY score DESC;
