import math

n = 1
res = []

def isFive(a, m):
    '''
    n = m
    b = 1
    while b <= a:
        b = (int)(n * (3*n - 1) / 2)
        if b == a: return True
        n += 1
    return False
    '''
    ret = (1+math.sqrt(1+24*a))/6
    if ret == int(ret): return True
    return False

while n < 100000:
    a = (int)(n * (3*n - 1) / 2)
    res.insert(0, a)
    n += 1
    #print("a :", a)

    m = -1
    for j in range(1, len(res)):
        #print(res)
        b = res[j]
        if m != -1 and a - b > m: break; #print("%d - %d > %d" % (a, b, m)); break
        if a - b > res[1]: break; #print("%d - %d > %d" % (a, b, res[1])); break
        if not ((a - b) in res): continue; #print("%d not in res" % (a-b)); continue
        if not isFive(a + b, n): continue; #print("%d is not Five" % (a+b)); continue

        m = a - b
        print("m:",m,"a:",a,"b:",b)
