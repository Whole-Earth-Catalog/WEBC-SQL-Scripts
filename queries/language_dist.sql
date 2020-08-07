# get total count of titles per language
select lang, count(*) 
from master_help, lang_table
where master_help.lang=lang_table.lang_short
group by lang;
# create table to relate different spellings of languages
drop table lang_table;
CREATE TABLE lang_table(
	lang_short char(3),
    lang_long varchar(10)
);
insert into lang_table values ("eng", "English");
insert into lang_table values ("spa", "Spanish");
insert into lang_table values ("lat", "Latin");
insert into lang_table values ("ita", "Italian");
insert into lang_table values ("fre", "French");
insert into lang_table values ("ger", "German");
insert into lang_table values ("dut", "Dutch");
# get total count of titles per language and decade
select lang_table.lang_long as language, CONCAT(decade, '0') as decade, count(master_help.id) as num_id 
from master_help, lang_table
where master_help.lang=lang_table.lang_short
group by lang_long, decade
order by lang_long, decade;
