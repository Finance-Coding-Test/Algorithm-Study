# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/301646

SELECT
    COUNT(ID) AS 'COUNT'
FROM ECOLI_DATA
WHERE !(GENOTYPE&2) AND ((GENOTYPE&1) OR (GENOTYPE &4));
