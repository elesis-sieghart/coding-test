-- ORDER BY, LIMIT
SELECT NAME FROM ANIMAL_INS ORDER BY DATETIME LIMIT 1;

-- SUBQUERY
SELECT NAME
from ANIMAL_INS
where DATETIME=(SELECT MIN(DATETIME)
                from ANIMAL_INS);
                
-- 최악의 경우(index가 없는 경우) min 이 order by limit 1 보다 빠르다. 즉, min 을 사용하는 것이 좋다.
-- 최선의 경우(index가 있는 경우) min 과 order by limit 1 의 성능이 비등비등하다. 
-- https://stackoverflow.com/a/426785
