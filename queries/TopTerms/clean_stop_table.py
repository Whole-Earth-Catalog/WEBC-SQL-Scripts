import json
from unidecode import unidecode

def clean_stop_word_list(word_list):
    clean_list = []
    for word in word_list:
        clean_list.append(unidecode(word).lower())
    return clean_list

with open('original_stop_words.json') as f:
    stop_terms = json.load(f)

with open('user_stop_words.json') as f:
    user_stop_terms = json.load(f)

lang_dict = {'eng':'en', 'spa':'es', 'ita':'it', 'fre':'fr', 'lat':'la', 'dut':'nl', 'ger':'de'}

stop_word_dict = {}

for key in lang_dict:
    stop_lang = lang_dict[key]
    stop_list = clean_stop_word_list(stop_terms[stop_lang])
    user_stop_list = user_stop_terms[key]
    full_stop_list = list(set(stop_list + user_stop_list))
    stop_word_dict.update({key:full_stop_list})

# print(stop_word_dict)
sw_json  = json.dumps(stop_word_dict, indent = 4)

with open('all_stop_words.json', 'w') as f:
    f.write(sw_json)
    f.write('\n')

