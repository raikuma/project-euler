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

c = 0
for d in range(2, 8+1):
    c += phi(d)
    if d % 10000 == 0:
        print(d)
print(c)