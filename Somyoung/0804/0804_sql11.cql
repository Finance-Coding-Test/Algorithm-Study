# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/144853

SELECT
    BOOK_ID AS 'BOOK_ID',
    DATE_FORMAT(PUBLISHED_DATE, '%Y-%m-%d') AS 'PUBLISHED_DATE'
FROM BOOK
WHERE YEAR(PUBLISHED_DATE) = 2021 AND CATEGORY = '인문'
ORDER BY 2;
