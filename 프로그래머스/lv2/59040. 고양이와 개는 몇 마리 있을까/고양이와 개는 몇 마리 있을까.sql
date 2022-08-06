-- 코드를 입력하세요
SELECT ANIMAL_TYPE, COUNT(*) count FROM ANIMAL_INS GROUP BY ANIMAL_TYPE ORDER BY 1;

-- ORDER BY 1
-- 첫번째 열을 기준으로 정렬을 수행하라는 의미
-- 위 코드에서 첫번째 열은 ANIMAL_TYPE이므로 이 열을 기준으로 정렬
-- (문제 조건: 고양이를 개보다 우선으로 표시)

-- 위 처럼 GROUP BY ANIMAL_TYPE도 GROUP BY 1 형태로 사용 
