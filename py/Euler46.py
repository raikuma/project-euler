from lib import isPrime
from math import sqrt

n = 7
while True:
    n += 2
    if isPrime(n): continue

    flag = False
    for i in range(2, n):
        if not isPrime(i): continue
        r = sqrt((n - i)/2)
        if r == int(r):
            flag = True
            #print("%d = %d + 2x%d^2" % (n, i, int(r)))
            break

    if flag == False:
        print(n)
