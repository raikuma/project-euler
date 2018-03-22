def spell(n):
    k = 0
    if n == 1000:
        k += 11  # one thousand
    elif n >= 100:
        l = n/100
        if l == 1 or l == 2 or l == 6:
            k += 3
        elif l == 4 or l == 5 or l == 9:
            k += 4
        elif l == 3 or l == 7 or l == 8:
            k += 5
        k += 7 # hundred
        n = n%100

        if n != 0: k+= 3 # and

    if n >= 20:
        l = n/10
        if l == 2 or l == 3 or l == 8 or l == 9:
            k += 6
        elif l == 4 or l == 5 or l == 6:
            k += 5
        elif l == 7:
            k += 7
        n %= 10

    if n == 1 or n == 2 or n == 6 or n == 10:
        k += 3
    elif n == 3 or n == 7 or n == 8:
        k += 5
    elif n == 4 or n == 5 or n == 9:
        k += 4
    elif n == 11 or n == 12:
        k += 6
    elif n == 13 or n == 14 or n == 18 or n == 19:
        k += 8
    elif n == 15 or n == 16:
        k += 7
    elif n == 17:
        k += 9

    return k

s = 0
for i in range(1, 1000+1):
    j = spell(i)
    print "%d: %d" % (i, j)
    s += j

print s
