-- List all records of second_table having a name in my MySQL server.
-- Records in descending order of score.
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
