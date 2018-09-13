from fractions import Fraction, gcd
n = 12000
r = []
for i in range(1, n+1):
    for j in range(i+1, n+1):
        if gcd(i, j) == 1:
            r.append(Fraction(i, j))
r.sort()
s, t = r.index(Fraction(1, 3)), r.index(Fraction(1, 2))
print(t-s-1)