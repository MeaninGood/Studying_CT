-- BOOK : BOOK_ID, CATEGORY, AUTHOR_ID, PRICE, PUBLISHED_DATE
-- AUTHOR : AUTHOR_ID, AUTHOR_NAME
-- BOOK_SALES : BOOK_ID, SALES_DATE, SALES
-- 1. 2022년 1월 도서 판매 데이터 기준 V
-- 2. 저자별, 카테고리별 매출액(total_sales = 판매량 * 판매가)
-- 3. 저자명, 카테고리, 매출액 리스트 출력
-- 4. 저자아이디 오름차순, 카테고리 내림차순

SELECT AB.AUTHOR_ID, AB.AUTHOR_NAME, AB.CATEGORY, SUM(AB.PRICE*BS.SALES) AS TOTAL_SALES
FROM
(SELECT B.BOOK_ID, B.CATEGORY, B.AUTHOR_ID, B.PRICE, A.AUTHOR_NAME
FROM BOOK B, AUTHOR A
WHERE B.AUTHOR_ID = A.AUTHOR_ID) AB,
BOOK_SALES BS
WHERE BS.BOOK_ID = AB.BOOK_ID
AND TO_CHAR(BS.SALES_DATE, 'YYYY-MM') = '2022-01'
GROUP BY AB.AUTHOR_ID, AB.AUTHOR_NAME, AB.CATEGORY
ORDER BY AB.AUTHOR_ID, AB.CATEGORY DESC;