from lib import *

ba = [2, 3, 5, 7, 11, 13, 17]
def foo(s):   
    if len(s) < 4: return True
    for i in range(len(s)-3):
        if not int(s[i+1:i+4]) % ba[i] == 0:
            print s, int(s[i+1:i+4]), ba[i]
            return False
    return True

string = "1234567890"

l = len(string)
res = []
k = 0
while k < factorial(l):
    print k
    c = l
    s = ''
    a = string

    n = k
    while a:
        #print n, s
        
        c -= 1
        b = factorial(c)
        d, m = divmod(n, b)
        if d >= len(a):
            a += s[-1]
            s = s[0:-1]
            n += factorial(c+1)
            c += 1
            continue
        s += a[d]

        if not foo(s):
            s = s[0:-1]
            n += factorial(c)
            c += 1
            continue

        n = m
        a = a[0:d]+a[d+1:len(a)]
        
    if len(s) == 10:
        res.append(int(s))
        print s
    k+=1

print res
print sum(res)
