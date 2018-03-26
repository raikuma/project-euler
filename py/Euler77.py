from lib import getPrime

prime = getPrime()
count = {0:1, 1:0}
for x in range(2, 11):
    m = 0
    for p in prime:
        if p > x:
            break
        if count[x-p] == 0:
            continue
        m += count[x-p]
    count[x] = m
    print(x, m)