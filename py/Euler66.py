from lib import *
from math import sqrt

def isSquare(n):
    return (int(sqrt(n))*int(sqrt(n)) == n)

for D in range(2,1000):
    if not isPrime(D): continue
    if not isSquare(D): continue

    x = 1
    while True:
        q, r = x**2-1
