/*
1. 조회수 가장 높은 중고거래 게시물
2. 첨부파일 경로 조회
3. FILE ID 내림차순
4. /HOME/GREP/SRC/순서로
5. 게시글 ID를 기준으로 디렉토리 구분
6. 파일 이름은 파일 ID, 파일 이름, 파일 확장자로 구성되도록
7. 조회수 가장 높은 게시물 하나만 존재
*/

SELECT CONCAT('/home/grep/src/', B.BOARD_ID, '/', B.FILE_ID, B.FILE_NAME, B.FILE_EXT) AS FILE_PATH

FROM USED_GOODS_BOARD AS A

JOIN USED_GOODS_FILE AS B ON A.BOARD_ID = B.BOARD_ID

WHERE A.BOARD_ID = (SELECT SA.BOARD_ID FROM USED_GOODS_BOARD AS SA ORDER BY SA.VIEWS DESC LIMIT 1)

ORDER BY B.FILE_ID DESC