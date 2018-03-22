from lib import isPrime
from itertools import permutations

p = []

for n in range(1000, 10000):
    if isPrime(n):
        p.append(n)
print("Start")
for n in range(1000, 10000):
    if n % 1000 == 0:
        print(n)
    a = permutations(str(n))
    r = set()
    for x in a:
        x = int(''.join(x))
        if x in p:
            r.add(x)
    r = list(r)
    if len(r) < 3:
        continue
    r.sort()
    for i in range(0, len(r)):
        for j in range(i+1, len(r)):
            for k in range(j+1, len(r)):
                if r[i] + r[k] == 2 * r[j]:
                    print(r[i], r[j], r[k])
        
