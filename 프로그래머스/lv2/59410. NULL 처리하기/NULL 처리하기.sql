SELECT ANIMAL_TYPE, COALESCE(NAME, 'No name') AS NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
ORDER BY ANIMAL_ID

-- COALESCE, IFNULL
/* 
COALESCE 함수는 여러개의 파라미터, IFNULL은 두개의 파라미터
COALESCE 함수는 표준 SQL 함수, IFNULL은 MYSQL에 있는 함수
더 유연하고 표준함인 것은 COALESCE 함수 
https://velog.io/@gillog/DB-MySQL-NULL-%EC%B2%98%EB%A6%ACIFNULL-CASE-COALESCE
*/

-- NVL, NVL2
/*
IFNULL이 MySQL함수 였다면 NVL, NVL2는 Oracle함수
https://cheershennah.tistory.com/211
*/
