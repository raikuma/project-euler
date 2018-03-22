def dir(n, m):
    if n < m:
        return 1
    if n > m:
        return -1
    return 0

b = 0

n = 99
p = 0

while p < 0.99:
    n += 1
    l = [int(x) for x in str(n)]
    d = dir(l[0], l[1])
    for i in range(1, len(l)-1):
        e = dir(l[i], l[i+1])
        if d == 0:
            d = e
            continue
        if e != 0 and e != d:
            #print(n)
            b += 1
            break
    p = b / n
    if n == 21780:
        print(p)

print(n)
