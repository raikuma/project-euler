s = ''
c = 0
i = 1
while c < 1000000:
    s += str(i)
    c += len(str(i))
    i += 1

r = 1
d = 1
for n in range(0,7):
    print s[d-1], d
    r *= int(s[d-1])
    d *= 10

print r
