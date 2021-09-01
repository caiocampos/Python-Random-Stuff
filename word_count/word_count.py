import re

def count_words(sentence):
    res = {}
    for word in re.split('(\'?[^0-9A-Za-z\']+\'?)+', sentence):
        word = word.strip(',.:;!&@$%^\'\n\t_ ').lower()
        if word == '':
            continue
        if word not in res:
            res[word] = 0
        res[word] += 1
    return res