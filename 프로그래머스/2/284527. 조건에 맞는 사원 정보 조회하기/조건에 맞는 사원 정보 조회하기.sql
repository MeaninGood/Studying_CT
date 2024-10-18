-- 코드를 작성해주세요
# 평가점수의 합
# SELECT C.SCORE, C.EMP_NO, C.EMP_NAME, D.POSITON, C.EMAIL
# FROM HR_DEPARTMENT AS D
# JOIN 
SELECT SUM(A.SCORE) AS SCORE, A.EMP_NO, B.EMP_NAME, B.POSITION, B.EMAIL 
FROM HR_GRADE AS A
JOIN HR_EMPLOYEES AS B
ON A.EMP_NO = B.EMP_NO
WHERE A.YEAR = 2022
GROUP BY EMP_NO
 ORDER BY SCORE DESC
# ORDER BY SCORE DESC) AS C
# ON 
LIMIT 1;