R = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
T = {1:'I', 4:'IV', 5:'V', 9:'IX', 10:'X', 40:'XL', 50:'L', 90:'XC',
    100:'C', 400:'CD', 500:'D', 900:'CM', 1000:'M'}

def R2D(rom_num):
    num = list(map(lambda x: R[x], rom_num))
    num2 = []
    i = 0
    while i < len(num)-1:
        if num[i] < num[i+1]:
            num2.append(num[i+1] - num[i])
            i += 1
        else:
            num2.append(num[i])
        i += 1
    if i == len(num)-1:
        num2.append(num[-1])
    return sum(num2)

def D2R(num):
    keys = sorted(T.keys(), reverse=True)
    r = ''
    for k in keys:
        while k <= num:
            num -= k
            r += T[k]
    return r
        
# a = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X',
#     'XVI', 'XIIIIII', 'VVVI', 'XIX']
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
#     16, 19, 49]
# print(list(map(lambda x:D2R(x), b)))

f = open('roman.txt')
data = f.read().split('\n')
f.close()
c = 0
for r in data:
    d = R2D(r)
    rd = D2R(d)
    c += len(r) - len(rd)
print(c)