def pro14(n):
    cnt = 0;
    while n != 1:
        if (n%2 == 0): n = n/2
        else: n = 3*n + 1
        cnt = cnt + 1
    return cnt

max = 0
n = 0
for i in range(1, 1000000+1):
    m = pro14(i)
    if (m > max):
        max = m
        n = i
        print(i,m)
