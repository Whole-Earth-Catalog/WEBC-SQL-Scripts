# get the genre of all titles, 1 = fiction, 0 = non-fiction
select substring(tag008.data, 34, 1) as genre
from tag008;
# RESULTS: 0s and 1s

# get number of titles labeled as nonfiction
select count(*) as num_nonfiction
from tag008
where substring(tag008.data, 34, 1) = 0;
# RESULTS: 5,775,828

# get number of titles labeled as fiction
select count(*) as num_fiction
from tag008
where substring(tag008.data, 34, 1) = 1;
# RESULTS: 50,704

# total with genre
select count(*) as num_with_genre
from tag008
where substring(tag008.data, 34, 1) != "";
# RESULTS: 5,836,406

# total that are not 0 or 1
select count(*) as num_without_genre
from tag008
where substring(tag008.data, 34, 1) != 0 and
		substring(tag008.data, 34, 1) != 1;
# RESULTS: 0

# other notes: substring(data, 25, 4) only has nature of form for 301,172 records
