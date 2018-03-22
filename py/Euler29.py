arr = []
for a in range(2, 101):
    for b in range(2, 101):
        c = a**b
        if not c in arr: arr.append(c)

print len(arr)
