from time import time
from functools import reduce
from operator import add

def speed_test():
    tt = time()
    res, v , n = [], 0, 100
    for i in range(n):
        t = time()
        for j in range(n ** 2):
            v += n * i * j
        res += [time() - t]
    print('menor:', min(res))
    print('maior:', max(res))
    print('média:', reduce(add,res)/len(res))
    print('total:', time() - tt)
