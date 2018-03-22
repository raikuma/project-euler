a = 3
b = 2
c = 0
for n in range(1000):
    #print(a, '/', b)

    if len(str(a)) > len(str(b)): c += 1

    a += 1 * b
    tmp = a
    a = b
    b = tmp
    a += 1 * b

print(c)
