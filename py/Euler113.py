def dir(n, m):
    if n < m:
        return 1
    if n > m:
        return -1
    return 0

def isBouncy(n):
    l = [int(x) for x in str(n)]
    d = dir(l[0], l[1])
    for i in range(1, len(l)-1):
        e = dir(l[i], l[i+1])
        if d == 0:
            d = e
            continue
        if e != 0 and e != d:
            return True
    return False

nb = 99

n = 10**100

for i in range(100, n):
    if not isBouncy(i):
        nb += 1
    if i % 100000 == 0:
        print(i)
        

print(nb)
