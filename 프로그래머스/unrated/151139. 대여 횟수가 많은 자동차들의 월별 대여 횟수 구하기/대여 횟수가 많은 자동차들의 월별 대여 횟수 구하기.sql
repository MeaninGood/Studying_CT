SELECT TMP.MONTH, TMP.CAR_ID, TMP.RECORDS 
FROM
(
    SELECT DISTINCT(EXTRACT(MONTH FROM START_DATE)) AS MONTH
            , CAR_ID
            , COUNT(HISTORY_ID) OVER(PARTITION BY CAR_ID) AS ALLRECORDS
            , COUNT(HISTORY_ID) OVER(PARTITION BY CAR_ID, EXTRACT(MONTH FROM START_DATE)) AS RECORDS
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE EXTRACT(MONTH FROM START_DATE) BETWEEN 8 AND 10
) TMP
WHERE TMP.ALLRECORDS >= 5
ORDER BY MONTH, CAR_ID DESC