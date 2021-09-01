import string

def is_pangram(sentence):
    return is_pangram_va(sentence)

def is_pangram_va(sentence):
    if len(sentence) < 26:
        return False
    dic = {}
    for c in sentence:
        if not c.isalpha():
            continue
        c = c.lower()
        if c not in dic:
            dic[c] = True
    return len(dic) == 26

def is_pangram_vb(sentence):
    if len(sentence) < 26:
        return False
    low_sentence = sentence.lower()
    for letter in string.ascii_lowercase:
        if letter not in low_sentence:
            return False
    return True