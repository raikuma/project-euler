m = 0

for a in range(1, 100):
    for b in range(1, 100):
        n = a**b
        m = max(m, sum([int(x) for x in list(str(n))]))

print(m)
