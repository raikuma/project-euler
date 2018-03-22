res = []

for a in range(10,100):
    for b in range(10,100):
        #case1
        if a/10 == b/10:
            if b%10 == 0: continue
            if float(a)/b == float(a%10)/(b%10):
                pass#res.append([a,b])

        #case2
        if a/10 == b%10:
            if float(a)/b == float(a%10)/(b/10):
                res.append([a,b])

        #case3
        if a/10 == b%10:
            if float(a)/b == float(a%10)/(b/10):
                res.append([a,b])

print res
