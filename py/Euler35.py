from lib import *

def shift(s):
    return s[-1]+s[0:-1]

def foo(n):
    for i in range(0, len(str(n))):
        if not isPrime(n): return False
        n = int(shift(str(n)))
    return True

res = []
for n in range(2, 1000000):
    if foo(n): res.append(n)

print res
print len(res)
