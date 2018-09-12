import math
def foo(n, x, y):
    t = (n - y**2) // x
    p = int((math.sqrt(n) + y) // t)
    q = y - p*t
    return p, -q, t

def bar(n):
    rn = math.sqrt(n)
    a0 = int(rn)
    x, y = 1, a0
    r = []
    while True:
        # print(x, y)
        p, q, t = foo(n, x, y)
        # print(p)
        r.append(p)
        x, y = t, q
        if (x, y) == (1, a0):
            return len(r)
            
r = []
for i in range(2, 10000+1):
    if math.sqrt(i) == int(math.sqrt(i)):
        continue
    if bar(i) % 2 == 1:
        r.append(i)
print(len(r))