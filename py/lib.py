from math import *

def isPrime(n):
    if n==1: return False
    if n!=2 and n%2==0: return False
    for i in range(2, int(sqrt(n))+1):
        if n%i == 0: return False
    return True

def isPalin(s):
    l = len(s)
    return s[:floor(l/2)] == s[:floor(l/2):-1]

def isPanDigital(s):
    return ''.join(sorted(s)) == '123456789'

def getAnagram(string):
    arr = []
    
    l = len(string)
    for n in range(0, factorial(l)):
        c = l
        s = ''
        a = string
        while a:
            c -= 1
            b = factorial(c)
            d, n = divmod(n, b)
            s += a[d]
            a = a[0:d]+a[d+1:len(a)]

        arr.append(s)
    return arr

def getWordValue(s):
    s = s.upper()
    return sum([ord(c)-ord('A')+1 for c in s])

def isTriNumber(n):
    i = 1
    while n > 0:
        n -= i
        i += 1
    if n == 0: return True
    return False

def isAnagram(a, b):
    a = list(a)
    b = list(b)
    a.sort()
    b.sort()
    return a == b

def reverseStr(s):
    return s[::-1]

def Eratos(n):
    if n < 2:
        return []
    r = []
    candi = list(range(2, n+1))

    while candi:
        c = candi.pop(False)
        r.append(c)
        if c > sqrt(n):
            continue
        i = 2
        while c * i <= n:
            try:
                candi.remove(c * i)
            except:
                pass
            i += 1
        
    return r