def fact(n):
    f = 1
    for i in range(2, n+1):
        f *= i
    return f

def combi(n, r):
    return fact(n) / (fact(r) * fact(n-r))

c = 0
for n in range(1, 100+1):
    for r in range(0, n+1):
        print(n, r)
        if combi(n, r) > 1000000:
            c += 1

print(c)