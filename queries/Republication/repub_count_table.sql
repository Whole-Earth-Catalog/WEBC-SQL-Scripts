CREATE TABLE repubs_count AS 
(
SELECT 
title, 
author,
COUNT(*) as repubs
FROM
repub_data
GROUP BY title, author
)
