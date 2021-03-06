# import numpy as np
# a = np.stack((np.ones(33), np.arange(2, 68, 2), np.ones(33)))
# a = a.T.reshape(1, -1).squeeze().astype(int)
# a = [2] + list(a)
a = [2, 1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8, 1, 1, 10, 1, 1, 12, 1, 1, 14, 1, 1, 16, 1, 1, 18, 1, 1, 20, 1, 1, 22, 1, 1, 24, 1, 1, 26, 1, 1, 28, 1, 1, 30, 1, 1, 32, 1, 1, 34, 1, 1, 36, 1, 1, 38, 1, 1, 40, 1, 1, 42, 1, 1, 44, 1, 1, 46, 1, 1, 48, 1, 1, 50, 1, 1, 52, 1, 1, 54, 1, 1, 56, 1, 1, 58, 1, 1, 60, 1, 1, 62, 1, 1, 64, 1, 1, 66, 1]
x, y = 1, a[-1]
for i in a[-2::-1]:
    p, q = y * i + x, y
    x, y = q, p
print(x, y)
print(sum([int(t) for t in str(y)]))

from fractions import Fraction
s = Fraction(1, a[-1])
for i in a[-2::-1]:
    s = 1 / (i + s)
print(s)
print(sum([int(t) for t in str(s.denominator)]))