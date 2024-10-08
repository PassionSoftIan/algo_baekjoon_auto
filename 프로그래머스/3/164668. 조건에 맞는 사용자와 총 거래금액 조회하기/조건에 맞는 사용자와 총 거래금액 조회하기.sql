SELECT
GU.USER_ID,
GU.NICKNAME,
SUM(GB.PRICE) AS TOTAL_SALES

FROM USED_GOODS_USER AS GU

LEFT JOIN USED_GOODS_BOARD AS GB ON GB.WRITER_ID = GU.USER_ID

WHERE GB.STATUS = 'DONE'

GROUP BY GU.USER_ID, GU.NICKNAME

HAVING TOTAL_SALES >= 700000

ORDER BY TOTAL_SALES ASC
