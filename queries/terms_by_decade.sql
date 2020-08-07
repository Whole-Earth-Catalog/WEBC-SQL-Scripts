use webc;
# get key_terms per decade and language
select concat(term_key) as term_key , concat(language) AS language, CONCAT(decade, '0') as decade,COUNT(id) AS num_ids
from terms_and_titles
group by term_key, decade, language
order by term_key, language, decade;
