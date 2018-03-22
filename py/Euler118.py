from itertools import *
from lib import *
from copy import deepcopy

s = '123456789'
c = 0
p = []

def goo(rest):
    global c
    if rest == "":
        c += 1
        #print "Find!"
        return
    
    for i in range(len(rest)):
        n = int(rest[0:i+1]);
        if n in p or isPrime(n):
            p.append(int(rest[0:i+1]))
            goo(rest[i+1:len(rest)])

for t in permutations(s, len(s)):
    r = "".join(t)
    goo(r)

print c
