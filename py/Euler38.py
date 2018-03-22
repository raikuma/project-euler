def isPan(s):
    a = []
    for i in range(0,9):
        if s[i] == '0' or s[i] in a: return False
        a.append(s[i])
    return True

res = []
for n in range(1,100000):
    s = ''
    m = 1
    while len(s) < 9:
        s += str(m*n)
        m += 1

    #print s
    if not len(s) == 9: continue
    if isPan(s): res.append(s)

print res
print max([int(s) for s in res])
    
    
