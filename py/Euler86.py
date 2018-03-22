def is_square(n):
    return n**0.5 == int(n**0.5)

def count(a, b, c):
    s = a**2 + (b+c)**2
    if is_square(s): 
        return 1
    return 0

m = 0
cnt = 0

while cnt < 1000000:
    m += 1
    a = m
    for b in range(1, m+1):
        for c in range(b, m+1):
            cnt += count(a, b, c)
    print(cnt)

print(m, cnt)