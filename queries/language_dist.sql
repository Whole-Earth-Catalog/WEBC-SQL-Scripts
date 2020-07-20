select substring(tag008.data, 36, 3) as lang, count(*) 
from tag008
group by substring(tag008.data, 36, 3);