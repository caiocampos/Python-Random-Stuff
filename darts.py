def score(x, y):
    r =  (x*x + y*y) ** 0.5
    if r <= 1:
        return 10
    if r <= 5:
        return 5
    if r <= 10:
        return 1
    return 0
