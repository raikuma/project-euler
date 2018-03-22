from lib import isPrime

k = 1000000
n = 1
r = []
while n <= k:
    n += 1
    m = n
    if not isPrime(n): continue
    s = 0
    a = 0
    c = 0
    d = 0
    while s <= k:
        if isPrime(n):
            s += n
            c += 1
            if s <= k and isPrime(s):
                d = c
                a = s
        n+=1
    
    if [d, m, a] > r: r = [d, m, a]
    n = m

print(r)
