from decimal import *
getcontext().prec = 102

r = 0
for n in range(1, 100+1):
    d = Decimal(n).sqrt()
    s = str(d)
    if '.' not in s:
        continue
    l = [int(x) for x in s[:101] if x != '.']
    t = sum(l)
    r += t
    #print(s, t, len(l))
print(r)
