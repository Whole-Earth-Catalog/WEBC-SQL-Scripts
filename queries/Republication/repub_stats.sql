SELECT 
MIN(repubs) AS minr,
AVG(repubs) AS avgr
FROM repubs_count
INTO OUTFILE '/var/lib/mysql/data.csv'
