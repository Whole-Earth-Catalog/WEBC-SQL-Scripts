USE webc;

CREATE TABLE repub_data AS
(
SELECT  a.id,  
a.title,  
b.$a AS author, 
SUBSTRING(c.data, 8, 4) as year 
FROM fullTitles AS a 
JOIN tag100 AS b ON a.id = b.id 
JOIN tag008 AS c ON a.id = c.id 
)

