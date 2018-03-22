def getZari(n):
    a = []
    while n > 0:
        a.append(n%10)
        n/=10
    return a

n = 10
r = 0
while True:
    s = 0
    for i in getZari(n):
        s += i**5
    if n == s: r += s; print n, s, r
    n+=1
