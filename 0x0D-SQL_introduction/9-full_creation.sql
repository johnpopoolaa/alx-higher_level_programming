-- this script creates a table in the datbase in MySQL server and adds multiple rows.
CREATE TABLE IF NOT EXISTS second_table(
	id INT, name VARCHAR(256), score INT
);
INSERT INTO
	second_table(id, name, score)
VALUES
	(1,"John",10),
	(2,"ALex",3),
	(3,"Bob",14),
	(4,"George",8);
