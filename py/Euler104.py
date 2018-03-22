from lib import isPanDigital

a = 1
b = 1
k = 2
while True:
    a += b
    k += 1
    h = str(a)[:9]
    t = str(a)[-9:]
    #print(h, t, len(str(a)))
    #print(isPanDigital(h), isPanDigital(t))
    if isPanDigital(h) and isPanDigital(t):
        print(a, k)
        break
    a, b = b, a