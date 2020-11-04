# number of authors in tag600: 1,528,391
select count($a) from tag600;

# create table of personal names using tags 100, 600, and 700
Create Table personal_names as 
	select id, $a from tag100
    union
    select id, $a from tag600
    union 
    select id, $a from tag700;

# get number of authors per decade
select concat(decade, '0'), count($a)
from personal_names, master_help
where personal_names.id = master_help.id
group by master_help.decade
order by master_help.decade;

# get number of coauthors per decade
select concat(decade, '0') as decade, count(id_groups.id)
from (
	select id, count($a) as num_authors
	from personal_names
	group by id
	having count($a) > 1 ) as id_groups, master_help
where id_groups.id = master_help.id 
	and decade != '15u' and decade != '16u' and decade != '17u'
group by decade
order by decade;



  
