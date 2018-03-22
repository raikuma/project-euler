from lib import *

res = []
for n in range(1,10):
    s = "123456789"[0:n]
    a = getAnagram(s)
    res += [x for x in a if isPrime(int(x))]
    print n
    
print max(res)
