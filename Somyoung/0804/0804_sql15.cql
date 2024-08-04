# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/276034

SELECT
   DISTINCT(D.ID) AS 'ID',
   D.EMAIL AS 'EMAIL',
   D.FIRST_NAME AS 'FIRST_NAME',
   D.LAST_NAME AS 'LAST_NAME'
FROM
    DEVELOPERS D
    INNER JOIN (SELECT CODE FROM SKILLCODES WHERE NAME IN ('Python', 'C#')) S
    ON (D.SKILL_CODE & S.CODE)
ORDER BY 1;
