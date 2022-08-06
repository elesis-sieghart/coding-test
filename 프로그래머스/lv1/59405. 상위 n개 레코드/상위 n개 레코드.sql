-- ORDER BY, LIMIT
SELECT NAME FROM ANIMAL_INS ORDER BY DATETIME LIMIT 1;

-- SUBQUERY
SELECT NAME
FROM ANIMAL_INS
WHERE DATETIME=(SELECT MIN(DATETIME)
                FROM ANIMAL_INS);
                
-- 최악의 경우(index가 없는 경우) min 이 order by limit 1 보다 빠르다. 즉, min 을 사용하는 것이 좋다.
-- 최선의 경우(index가 있는 경우) min 과 order by limit 1 의 성능이 비등비등하다. 
-- https://stackoverflow.com/a/426785

-- ORDER BY, LIMIT와 MAX의 차이점
-- ORDER BY, LIMIT는 row 단위로 데이터를 확인하면서 가져오는 쿼리
-- MAX는 하나의 컬럼 내에서 가장 큰 하나의 값을 찾아내는 쿼리
-- 즉, 테이블 내 한개의 컬럼에 대한 최소값, 최댓값을 구해야 할 경우 max와 order by, limit 1은 호환이 될 수 있으나. 그 이외의 경우에는 다르게 동작
-- https://www.inflearn.com/questions/60926
