# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/132203

SELECT
   DR_NAME AS 'DR_NAME',
   DR_ID AS 'DR_ID',
   MCDP_CD AS 'MCDP_CD',
   DATE_FORMAT(HIRE_YMD, '%Y-%m-%d') AS 'HIRE_YMD'
FROM
    DOCTOR
WHERE MCDP_CD IN ('CS', 'GS')
ORDER BY 4 DESC, 1 ASC;
