import math

def d(n):
    sum = 0;
    for i in range(1, n/2+1):
        if n % i == 0: sum += i

    return sum

sum = 0
for a in range(1, 10000+1):
    b = d(a)
    if d(b) == a and a != b: sum += a; print(a, b)

print sum
