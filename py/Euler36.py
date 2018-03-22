from lib import *

res = []
for n in range(1, 1000000+1):
    if isPalin(str(n)) and isPalin(str(bin(n))[2:len(str(bin(n)))]):
        res.append(n)

print res
print sum(res)
