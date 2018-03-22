n = 1;
for i in range(1, 100+1):
    n *= i
    
print n
s = 0;
while n > 0:
    s += n%10
    n /= 10

print s
