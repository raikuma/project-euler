import math

def foo(arr):
    zrr = []
    for i in arr:
        for s in str(i):
            zrr.append(s)
    if len(zrr) > len(set(zrr)): return False
    if len(zrr) != 9: return False
    if '0' in zrr: return False
    return True

s = 0
res = []
for n in range(1000, 10000):
    arr = []
    for i in range(1, (int)(math.sqrt(n))+1):
        if n%i == 0: arr.append([i,n/i])

    for d in arr:
        if foo([d[0],d[1],n]): res.append(n); break

print res
print sum(res)
