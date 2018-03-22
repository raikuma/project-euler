s = 0
for n in range(1, 1000+1):
    s += n**n
print s % 10**10

s = 0
for n in range(1, 1000+1):
    l = str(n**n)
    s += int(l[-10:len(l)])
    s = int(str(s)[-10:len(str(s))])
print s
