import pandas as pd
import numpy as np
import csv

# get data from common_terms.tsv
decades = []
counts = []
languages = []
with open('common_terms.tsv') as tsv_file:
    tsv_reader = csv.reader(tsv_file, delimiter='\t')
    next(tsv_reader)
    for row in tsv_reader:
        decades.append(row[3])
        counts.append(row[4])
        languages.append(row[2])

data_dict = {'decade':decades, 'count':counts, 'language':languages}
# create pandas dataframe from data
terms_df = pd.DataFrame(data_dict)
new_terms_df = pd.DataFrame()
# get a list of all languages (without duplicates)
all_languages = list(set(languages))
# perform EMA for each language
for language in all_languages:
    # get df for language
    lang_df = terms_df.loc[terms_df['language']== language]
    # add EMA values to lang_df
    lang_df['EMA'] = lang_df.iloc[:,0].ewm(span=40,adjust=False).mean()
    # add SMA values to lang_df
    lang_df['pandas_SMA_3'] = lang_df.iloc[:,1].rolling(window=3).mean()
    new_terms_df = pd.concat([new_terms_df,lang_df])
    print(lang_df)

print(new_terms_df)

new_terms_df.to_csv('ema_data.csv', index=False)
