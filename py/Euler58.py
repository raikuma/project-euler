from lib import isPrime

p = [0,0]
d = 0
n = 1
c = 0
s = 1
t = 0
while True:
    if d == 0:
        p[0] += 1
        n += 1
        if abs(p[0]) == c:
            s+=1
            if isPrime(n): t += 1
        if abs(p[0]) > c: c+=1; d+=1; d%=4
    elif d == 1:
        p[1] += 1
        n += 1
        if abs(p[1]) == c:
            d+=1; d%=4; s+=1
            if isPrime(n): t += 1
    elif d == 2:
        p[0] -= 1
        n += 1
        if abs(p[0]) == c:
            d+=1; d%=4; s+=1
            if isPrime(n): t += 1
    elif d == 3:
        p[1] -= 1
        n += 1
        if abs(p[1]) == c:
            d+=1; d%=4; s+=1
            if isPrime(n): t += 1
    #print(p, n, d, c, s, t)

    #if c >= 501: break
    if t/s < 0.1: print(c)
print(c)
