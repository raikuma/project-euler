p = [0,0]
d = 0
n = 1
c = 0
sum = 1
while True:
    if d == 0:
        p[0] += 1
        n += 1
        if abs(p[0]) == c: sum+=n
        if abs(p[0]) > c: c+=1; d+=1; d%=4
    elif d == 1:
        p[1] += 1
        n += 1
        if abs(p[1]) == c: d+=1; d%=4; sum+=n
    elif d == 2:
        p[0] -= 1
        n += 1
        if abs(p[0]) == c: d+=1; d%=4; sum+=n
    elif d == 3:
        p[1] -= 1
        n += 1
        if abs(p[1]) == c: d+=1; d%=4; sum+=n
    #print p, n, d, c

    if c >= 501: break
print sum
