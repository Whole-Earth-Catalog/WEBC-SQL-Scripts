drop table terms_and_titles;

CREATE table terms_and_titles AS
SELECT master_help.id, master_help.title, terms.term_lc, terms.term_key, terms.language, master_help.decade
FROM master_help, terms
WHERE (master_help.title LIKE(CONCAT('% ',terms.term_lc,' %')) # term within title
	OR master_help.title LIKE(CONCAT('% ',terms.term_cap1,' %'))
    OR master_help.title LIKE(CONCAT(terms.term_lc,' %')) # term at beginning of title
	OR master_help.title LIKE(CONCAT(terms.term_cap1,' %'))
    OR master_help.title LIKE(CONCAT('% ',terms.term_lc)) # term at end of title
	OR master_help.title LIKE(CONCAT('% ',terms.term_cap1))
    ) AND master_help.lang=lower(substring(terms.language,1,3)); 			 
