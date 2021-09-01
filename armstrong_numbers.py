def is_armstrong_number(number):
    if number < 10:
        return True
    sum = 0
    s_val = str(number)
    e = len(s_val)
    for c in s_val:
        sum += int(c)**e
    return sum == number
