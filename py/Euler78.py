p = {}

def P(n, k):
    if n < k:
        return 0
    if k == 1:
        return 1
    if n == k:
        return 1
    if (n, k) in p:
        return p[(n, k)]
    p[(n, k)] = sum(P(n-k, i) for i in range(1, k+1))
    return p[(n, k)]

def S(n):
    return sum(P(n, k) for k in range(1, n+1))

n = 2
while True:
    r = S(n)
    print(n, r)
    if r % 1000000 == 0:
        break
    n += 1
    if n % 1000 == 0: print(n) 
print(n)
