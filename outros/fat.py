def _fat1(n):
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r

def _fat2(n):
    return 1 if n < 1 else n * _fat2(n - 1)

_fat3 = lambda n: 1 if n < 1 else n * _fat3(n - 1)

from functools import * # importa reduce()

_fat4 = lambda n: 1 if n < 2 else reduce(lambda a, b: a * b, range(2, n + 1))

from operator import * # importa mul()

_fat5 = lambda n: 1 if n < 2 else reduce(mul, range(2, n + 1))

_fat6 = lambda n: n < 1 and 1 or n * _fat6(n - 1)

fat = _fat6
