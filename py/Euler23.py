# -*- coding: cp949 -*-
def isCho(n):
    sum = 0
    for i in range(1, n/2+1):
        if n%i == 0: sum += i
        if sum > n: return True
    return False

cho = []
for n in range(1, 28123+1):
    if isCho(n): cho.append(n)

print "초과수 배열 구함"

sum = 0
for n in range(1, 28123+1):
    flag = True
    for a in range(1, n/2+1):
        if (a in cho) and (n-a in cho):
            flag = False
            break
    if flag: sum += n

    if n%100 == 0: print n

print sum
            
