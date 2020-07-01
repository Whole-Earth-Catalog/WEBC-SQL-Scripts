# Q1) get total number of rows
SELECT COUNT(*) num_rows FROM terms_and_titles;

# Q2) get number of titles per term
SELECT term_lc, COUNT(id) 
FROM terms_and_titles
GROUP BY term_lc;

# Q3) get total number of unique terms
SELECT COUNT(term_lc) num_unique_terms 
FROM (
	SELECT term_lc 
    FROM terms
    GROUP BY term_lc
    ) AS unique_terms;

# Q4) get number of terms found in titles during search
SELECT COUNT(*) num_found_terms
FROM (
	SELECT term_lc
	FROM terms_and_titles
	GROUP BY term_lc
    ) AS found_terms;

# Q5) get terms not found in search
SELECT term_lc unfound_terms
FROM terms
WHERE term_lc NOT IN (
    SELECT term_lc
	FROM terms_and_titles
	GROUP BY term_lc)
GROUP BY term_lc; 

# Q6) Get title count per language
SELECT language, count(id)
FROM terms_and_titles
GROUP BY language;

# Q7) Get number of titles with more than one language
SELECT COUNT(id), MAX(num_languages), AVG(num_languages)
FROM (
	SELECT id, COUNT(language) AS num_languages 
	FROM terms_and_titles
	GROUP BY id
) AS id_groups
WHERE num_languages > 1;

# Q8) get total number of unique ids
SELECT count(id) num_unique_ids
FROM (
	SELECT id
    FROM terms_and_titles
    GROUP BY id
    ) AS unique_ids;
