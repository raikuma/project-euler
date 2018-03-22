def phi(n):
    r = n
    d = 2
    p = n
    while r > 1:
        if r % d == 0:
            p -= int(r/d)
            while r % d == 0:
                r = int(r/d)
        d += 1
    return p

m = (0, 1)
for n in range(2, 1000000):
    p = phi(n)
    m = max(m, (n/p, n))
    if n % 10000 == 0:
        print(n)

print(m)
