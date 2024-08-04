# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/284530

SELECT
    YEAR(YM) AS 'YEAR',
    ROUND(AVG(PM_VAL1),2) AS 'PM10',
    ROUND(AVG(PM_VAL2),2) AS 'PM2.5'
FROM
    (SELECT YM, PM_VAL1, PM_VAL2
     FROM AIR_POLLUTION
     WHERE LOCATION2 = '수원') D
GROUP BY YEAR(YM)
ORDER BY YEAR(YM);
