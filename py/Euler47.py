from lib import isPrime

k = 4
n = 2
c = 0
while True:
    i = 2
    s = set()
    m = n
    while i <= m:
        if isPrime(i):
            while m % i == 0:
                s.add(i)
                m = int(m/i)
        if len(s) > k:
            s = set()
            break
        i+=1
    if len(s) == k:
        c += 1
    else:
        c = 0
    if c == k:
        print(n, len(s))
        break
    n+=1
