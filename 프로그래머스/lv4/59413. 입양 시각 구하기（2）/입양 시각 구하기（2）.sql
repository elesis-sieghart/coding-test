WITH RECURSIVE test AS ( 
    -- Non-Recursive 문장( 첫번째 루프에서만 실행됨 )
    SELECT 0 AS num
    UNION ALL
    -- Recursive 문장(읽어 올 때마다 행의 위치가 기억되어 다음번 읽어 올 때 다음 행으로 이동함)
    SELECT num+1 AS num FROM test WHERE num+1<24
)

SELECT T.num, COALESCE(H.COUNT, 0) FROM TEST T
LEFT JOIN (
SELECT HOUR(DATETIME) HOUR, COUNT(*) COUNT
      FROM ANIMAL_OUTS
      GROUP BY HOUR
      ORDER BY 1) H ON T.num = H.HOUR;
      



