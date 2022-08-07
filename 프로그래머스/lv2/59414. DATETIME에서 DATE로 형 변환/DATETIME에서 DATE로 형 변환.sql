SELECT ANIMAL_ID, NAME, DATE_FORMAT(DATETIME,'%Y-%m-%d') AS '날짜'
FROM ANIMAL_INS
ORDER BY ANIMAL_ID

-- https://dev.mysql.com/doc/refman/5.7/en/date-and-time-functions.html
