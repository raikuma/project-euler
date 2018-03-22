import math

n = 2
a = 1
b = 1

while math.log10(b) < 999:
    c = a+b
    a = b
    b = c
    n += 1

print b, n
