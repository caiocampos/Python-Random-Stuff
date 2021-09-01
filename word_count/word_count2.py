import re

def count_words(sentence):
    res = {}
    for word in re.split('(\'?[^0-9A-Za-z\']+\'?)+', sentence):
        word = word.strip(',.:;!&@$%^\'\n\t_ ').lower()
        if word == '':
            continue
        res[word] = 1 + (res.get(word) or 0)
    return res