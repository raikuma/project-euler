n = 1;
for i in range(1,1000+1):
    n *= 2
s = 0;
while n > 0:
    s += n%10
    n /= 10
print s
