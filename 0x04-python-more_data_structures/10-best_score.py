#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max_key = {'name': list(a_dictionary.keys())[0]}
    max_num = list(a_dictionary.values())[0]
    for key, num in a_dictionary.items():
        if num > max_num:
            max_key['name'] = key
    return max_key['name']
