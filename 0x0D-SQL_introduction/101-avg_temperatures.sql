-- this scriotdisplays the average temperature by city in descending order.
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP by CITY ORDER BY avg_temp DESC;
