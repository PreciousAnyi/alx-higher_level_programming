#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary:
        max_value = max(a_dictionary.values())
        best_key = []
        for key, value in a_dictionary.items():
            if value == max_value:
                best_key.append(key)
        return best_key[0]
    return None
