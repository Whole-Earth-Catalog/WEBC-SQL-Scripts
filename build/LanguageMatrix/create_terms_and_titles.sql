drop table if exists terms_and_titles;
CREATE table terms_and_titles AS
SELECT master_help.id, master_help.title, terms.term, terms.term_key, terms.language, master_help.decade, terms.term_type
FROM master_help, terms
WHERE (
	clean_title(master_help.title) 
		LIKE(CONCAT('% ',terms.term,' %')) # term within title
    OR clean_title(master_help.title) 
		LIKE(CONCAT(terms.term,' %')) # term at beginning of title
    OR clean_title(master_help.title) 
		LIKE(CONCAT('% ',terms.term)) # term at end of title
    ) AND master_help.lang=lower(substring(terms.language,1,3)); 
