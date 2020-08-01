use webc;
drop table master_help;
# create master table with id, language, title, decade, to help with top term queries
create table master_help as
	select tag245.id as id, tag245.$a as title, substring(tag008.data, 36, 3) as lang, substring(tag008.data, 8, 3) as decade
    from tag245, tag008
    where tag008.id=tag245.id;
    
