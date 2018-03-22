import sys
sys.setrecursionlimit(5000)

p = {}
n = 100

def P(n, k):
    if n < k:
        return 0
    if k == 1:
        return 1
    if n == k:
        return 1
    if (n, k) in p:
        return p[(n, k)]
    p[(n, k)] = P(n-1, k-1) + P(n-k, k)
    return p[(n, k)]

r = sum(P(n, k) for k in range(2, 100+1))
print(r)
