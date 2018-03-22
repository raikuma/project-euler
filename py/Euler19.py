# -*- coding: cp949 -*-
mon = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dic = ['월', '화', '수', '목', '금', '토', '일']

sum = 0
c = 0

for year in range(1900, 2000):
    t = 0
    if (year%4 == 0 and year%100 != 0) or year%400 == 0:
        t = 1

    for m in range(0, 12):
        if mon[m] == 28: sum += t
        sum += mon[m]
        sum %= 7
        if sum == 6 and (not year == 1900): c += 1
        #print "%d년 %d월 1일 %s" % (year, m+2, dic[sum])
    
print c
