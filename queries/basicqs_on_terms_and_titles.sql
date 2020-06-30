# get total number of rows
SELECT COUNT(*) num_rows FROM terms_and_titles;
# get number of titles per term
SELECT term_lc, COUNT(id) 
FROM terms_and_titles
GROUP BY term_lc;
# get number of total terms
SELECT COUNT(*) num_all_terms FROM terms;
# get number of terms found in titles during search
SELECT COUNT(*) num_found_terms
FROM (
	SELECT COUNT(*)
	FROM terms_and_titles
	GROUP BY term_lc
    ) AS found_terms;
# get terms not found in search
SELECT term_lc unfound_terms
FROM terms
WHERE term_lc NOT IN (
    SELECT term_lc
	FROM terms_and_titles
	GROUP BY term_lc ); 
# Get title count per language
SELECT language, count(id)
FROM terms_and_titles
GROUP BY language;
