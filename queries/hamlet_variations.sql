use webc;
# select all publications of hamlet and study output for an idea of title variation in dataset
select tag245.$a as title, tag100.$a as author
from tag245, tag100
where tag245.id=tag100.id and tag100.$a like ('%Shakespeare%') and tag245.$a like ("%Hamlet%");
