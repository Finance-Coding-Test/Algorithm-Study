# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/299305

SELECT
    PARENT.ID AS 'ID',
    IFNULL(COUNT(CHILD.ID), 0) AS 'CHILD_COUNT'
FROM
    (SELECT ID FROM ECOLI_DATA) PARENT
    LEFT JOIN
    (SELECT ID, PARENT_ID FROM ECOLI_DATA) CHILD
    ON CHILD.PARENT_ID = PARENT.ID
GROUP BY PARENT.ID
ORDER BY 1;
