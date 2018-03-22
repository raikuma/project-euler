s = ''
f = open("p8.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    s += line[0:-1]
f.close()

m = 0
for i in range(0, len(s)-1-13):
    r = 1
    for j in range(0, 13):
        r *= int(s[i+j])
    m = max(m, r)

print m
