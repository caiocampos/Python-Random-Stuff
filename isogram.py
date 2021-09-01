def is_isogram(string):
    string = string.lower()
    for i, c in enumerate(string):
        if not c.isalpha():
            continue
        if string.rfind(c) > i:
            return False
    return True
