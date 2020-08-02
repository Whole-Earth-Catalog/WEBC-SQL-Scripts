use webc;
# get terms per decade
SELECT concat(term_lc) AS term, concat(term_key) AS term_key, concat(language) AS language, CONCAT(decade_num, '0') as decade, COUNT(id) AS num_ids
FROM (
	SELECT terms_and_titles.*, SUBSTRING(tag008.data, 8, 3) AS decade_num
    FROM terms_and_titles, tag008
    WHERE terms_and_titles.id=tag008.id
) AS terms_and_decades
GROUP BY term_lc, term_key, decade_num, language
order by term_lc, decade;
# get key_terms per decade and language
select concat(term_key) as term_key , concat(language) AS language, CONCAT(decade_num, '0') as decade,COUNT(id) AS num_ids
from (
	SELECT terms_and_titles.*, SUBSTRING(tag008.data, 8, 3) AS decade_num
    FROM terms_and_titles, tag008
    WHERE terms_and_titles.id=tag008.id
) AS terms_and_decades
group by term_key, decade_num, language
order by term_key, decade
