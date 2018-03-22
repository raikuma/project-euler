from lib import *


m = 0
a = []
c = 0
while m <= 10000:
    m += 1
    n = m

    flag = False
    for i in range(50-1):
        n = n + int(reverseStr(str(n)))
        if isPalin(str(n)):
            flag = True
            break

    if flag: continue
    c += 1
    a.append(m)
    #print(m, n)

print(len(a), a)
