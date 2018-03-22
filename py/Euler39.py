res = [0,0]
for p in range(3,1000+1):
    cnt = 0
    for c in range(1,p):
        for b in range(1,c):
            a = p - c - b
            if a <= 0: continue
            if a+b <= c: continue
            if a*a+b*b==c*c: cnt+=1

    if res[0]<cnt: res[0]=cnt;res[1]=p
    if p%100 == 0: print p

print res
