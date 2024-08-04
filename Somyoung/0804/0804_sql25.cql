# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/164672

SELECT
    BOARD_ID AS 'BOARD_ID',
    WRITER_ID AS 'WRITER_ID',
    TITLE AS 'TITLE',
    PRICE AS 'PRICE',
    CASE WHEN STATUS = 'DONE' THEN '거래완료'
    WHEN STATUS = 'RESERVED' THEN '예약중'
    ELSE '판매중' END AS 'STATUS'
FROM USED_GOODS_BOARD
WHERE DATE_FORMAT(CREATED_DATE, '%Y%m%d') = '20221005'
ORDER BY 1 DESC;
