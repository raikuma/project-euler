import math

def isTri(a):
    n = (-1 + math.sqrt(1+8*a)) / 2
    if n == int(n): return True
    return False

def isPen(a):
    n = (1 + math.sqrt(1+24*a)) / 6
    if n == int(n): return True
    return False

def isHex(a):
    n = (1 + math.sqrt(1+8*a)) / 4
    if n == int(n): return True
    return False

n = 285
while True:
    t = int(n * (n+1) / 2)
    if isPen(t) and isHex(t): print(t)
    n += 1
