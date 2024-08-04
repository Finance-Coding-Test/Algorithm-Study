# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/131112

SELECT
    FACTORY_ID,
    FACTORY_NAME,
    ADDRESS
FROM
    FOOD_FACTORY
WHERE LEFT(ADDRESS,3) = '강원도'
ORDER BY 1;
