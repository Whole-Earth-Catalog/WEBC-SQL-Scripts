drop table if exists terms_and_titles;
# function to remove punctuation and capital letters in titles
delimiter //
create function clean_title(title varchar(6000))
returns varchar(6000)
deterministic
begin
	declare new_title varchar(6000);
	set new_title = lower(replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(
    replace(replace(replace(replace(replace(replace(replace(replace(
    replace(replace(replace(replace(replace(replace(replace(replace(
    replace(replace(title, '|', ''), '=', '')
    , '+', ''), '\_', ''), '-', ''), '}' ,''), '{', ''), '*', ''), '^', ''), '>' ,'')
    , '<', ''), '\"', ''), '\'', ''), '\\', ''), '\%', ''), '$', ''), '#', ''), '@', '')
    , '!', ''), ')', ''), '(', ''), ']', ''),'[', ''), '/', ''), ';', ''), ':', ''), '?', ''), ',', ''), '.', ''));
    return new_title;
end//
delimiter ;

CREATE table terms_and_titles AS
SELECT master_help.id, master_help.title, terms.term_lc, terms.term_key, terms.language, master_help.decade
FROM master_help, terms
WHERE (
	clean_title(master_help.title) 
		LIKE(CONCAT('% ',terms.term_lc,' %')) # term within title
    OR clean_title(master_help.title) 
		LIKE(CONCAT(terms.term_lc,' %')) # term at beginning of title
    OR clean_title(master_help.title) 
		LIKE(CONCAT('% ',terms.term_lc)) # term at end of title
    ) AND master_help.lang=lower(substring(terms.language,1,3)); 
