from lib import isPrime

n = 10
v = []
m = 0
digit = '0123456789'

#for _ in range(1000):
while True:
    s = str(n)
    char = list(set(s))
    form = []
    for x in char:
        form.append(s.replace(x, '*'))
    for f in form:
        if f in v:
            continue
        r = []
        for d in digit:
            t = f.replace('*', d)
            if t[0] == '0':
                continue
            if isPrime(int(t)):
                r.append(int(t))
        if len(r) > m:
            m = len(r)
            print(r)
        v.append(f)
    if n % 1000 == 0:
        print(n)
    n += 1

#[121313, 222323, 323333, 424343, 525353, 626363, 828383, 929393]
