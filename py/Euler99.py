from math import log
f = open('base_exp.txt')
d = f.readlines()
f.close()
def s2l(s):
    a, x = s[:-1].split(',')
    a, x = int(a), int(x)
    return x * log(a)
d = [s2l(s) for s in d]
m = max(d)
print(d.index(m) + 1)