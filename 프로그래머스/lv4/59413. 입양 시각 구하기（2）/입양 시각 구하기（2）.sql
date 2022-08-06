WITH RECURSIVE test AS ( 
    SELECT 0 AS num # Non-Recursive 문장( 첫번째 루프에서만 실행됨 )
    UNION ALL
    SELECT num+1 AS num FROM test WHERE num+1<24 # Recursive 문장(읽어 올 때마다 행의 위치가 기억되어 다음번 읽어 올 때 다음 행으로 이동함)
)
SELECT T.num, COALESCE(H.COUNT, 0) FROM TEST T
LEFT JOIN (
SELECT HOUR(DATETIME) HOUR, COUNT(*) COUNT
      FROM ANIMAL_OUTS
      GROUP BY HOUR
      ORDER BY 1) H ON T.num = H.HOUR;
      
-- JOIN
-- https://inpa.tistory.com/entry/MYSQL-%F0%9F%93%9A-JOIN-%EC%A1%B0%EC%9D%B8-%EA%B7%B8%EB%A6%BC%EC%9C%BC%EB%A1%9C-%EC%95%8C%EA%B8%B0%EC%89%BD%EA%B2%8C-%EC%A0%95%EB%A6%AC#inner_join_%ED%95%A8%EC%B6%95_%EA%B5%AC%EB%AC%B8


