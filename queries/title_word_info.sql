select MAX(
	round(
		length(tag245.$a) - length(replace(tag245.$a, " ", ""))
    )
) as max_words_in_title,
AVG(
	round(
		length(tag245.$a) - length(replace(tag245.$a, " ", ""))
    )
) as avg_words_in_title,
sum(
	round(
		length(tag245.$a) - length(replace(tag245.$a, " ", ""))
    )
) as total_words
from tag245;