# Update Graph
These are all of the programs used to get, analyze, and clean the data necessary to make the graph in the TermSearchResults repository.

## term_search.py
This is the full code for getting the data needed to make the graph. The results are outputted in data.tsv and then the url for data.tsv raw data is called in by the 
js script in TermSearchResults. This code could be automated to update regularly if titles are being modified with cleaning techniques.

## .json files
The .json files have stop words used to remove unwanted words from titles when trying to find the most common term in a language per decade. 
- original_stop_words.json: taken from a web source that has stop words for all of the languages in the dataset
- user_stop_words.json: words that I found should not be considered for the common word trendline (now not graphed)
- all_stop_words.json: a combination of the above 2 files

## clean_stop_table.py
This combines all of the json files into one, all_stop_words.json

## topterms.py
The full code for getting the top most frequently word used in each decade per language. 
- common_terms.tsv has the output of this code
- moving_average.py modifies y values to fit a moving average algorithm
- ema_data.csv has the results of the moving_average.py code with the same terms as common_terms.tsv but different frequency values that were adjusted for a moving average.
