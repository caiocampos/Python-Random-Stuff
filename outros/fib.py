def fib1():
    print('Série de Fibonacci\n')
    a, b, m = 0, 1, int(input('Qual o tamanho de sua sequencia?\n'))
    for n in range(m - 1):
        a, b = b, a + b
        print(a, end = ', ')
    print(b)

def fib2(m):
    a, b = 0, 1
    for n in range(m - 1):
        print(b, end = ', ')
        a, b = b, a + b
    print(b)

def fib3(m):
    a, b, r = 0, 1, []
    for n in range(m): r, a, b = r + [b], b, a + b
    return r

def fib4(m):
    a = [0,1]
    return [a[-2] for i in range(m) if not a.append(a[-2] + a[-1])]

def fib5(m, a = 0, b = 1):
    return [] if m < 1 else [b] + fib5(m - 1, b, a + b)

fib6 = lambda m, a = 0, b = 1: [] if m < 1 else [b] + fib6(m - 1, b, a + b)
