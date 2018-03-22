def foo(n, x):
    return x*n / (x-n)

n = 55440
m = 0
while True:
    x = n + 1
    c = 0
    while True:
        y = foo(n, x)
        if y < n + 1:
            break
        if y == int(y):
            c += 1
        if y == x or y < x:
            break
        x += 1
    if c > m:
        print('[', n, ':', c, ']')
        m = c
    if c > 1000:
        print('ANSWER [', n, ':', c, ']')
        break
    n += 1
