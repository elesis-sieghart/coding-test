-- 코드를 입력하세요
SELECT *
FROM (SELECT NAME, COUNT(*) AS COUNT 
      FROM ANIMAL_INS 
      GROUP BY NAME
      ORDER BY NAME) A
WHERE A.COUNT>=2 AND A.NAME IS NOT NULL;

-- 의문점: GROUP BY는 NULL 집계가 안된다고 배워 IS NOT NULL 조건을 빼고 풀었는데, 그때는 오답 처리되었다. 왜그럴까?
-- https://school.programmers.co.kr/questions/28525
