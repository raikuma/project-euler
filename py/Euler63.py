n = 1
y = 1
r = 0

while True:
    while 10**(n-1) > y**n:
        y += 1
    if y > 9:
        break
    r += 10 - y
    n += 1

print(r)
