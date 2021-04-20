SELECT 
repubs,
COUNT(*) as cnt
FROM 
(
SELECT 
COUNT(*) as repubs
FROM
repub_data
GROUP BY title, author
) AS rpbs
GROUP BY repubs
INTO OUTFILE '/var/lib/mysql/repubs.csv';
