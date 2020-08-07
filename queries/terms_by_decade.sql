use webc;
# get key_terms per decade and language
select concat(term_key) as term_key , concat(language) AS language, CONCAT(decade_num, '0') as decade,COUNT(id) AS num_ids
from (
	SELECT terms_and_titles.*, SUBSTRING(tag008.data, 8, 3) AS decade_num
    FROM terms_and_titles, tag008
    WHERE terms_and_titles.id=tag008.id AND LOWER(SUBSTRING(terms_and_titles.language, 1, 3))=SUBSTRING(tag008.data, 36, 3)
) AS terms_and_decades
group by term_key, decade_num, language
order by term_key, decade_num;
