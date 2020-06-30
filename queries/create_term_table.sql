CREATE table terms_and_titles AS
SELECT tag245.id, tag245.$a, terms.term_lc, terms.term_key, terms.language
FROM tag245, terms
WHERE tag245.$a LIKE(CONCAT('% ',terms.term_lc,' %'))
	OR tag245.$a LIKE(CONCAT('% ',terms.term_cap1,' %')); 
