from lib import *

def foo1(s):
    if not s: return True
    if isPrime(int(s)): return foo1(s[0:-1])
    return False

def foo2(s):
    if not s: return True
    if isPrime(int(s)): return foo2(s[1:len(s)])
    return False

def foo(n):
    return foo1(str(n)) and foo2(str(n))

res = []
for n in range(11, 1000000):
    if foo(n): res.append(n)
print res, len(res)
print sum(res)
