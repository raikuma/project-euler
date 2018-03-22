import math

def f(n):
    a = [0,1,2,3,4,5,6,7,8,9]

    n -= 1
    c = 9
    s = ''
    while a:
        b = math.factorial(c)
        d, n = divmod(n, b)
        s += str(a[d])
        a.remove(a[d])
        c -= 1

    return s
