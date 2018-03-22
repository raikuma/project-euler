from itertools import permutations

f = open("cipher1.txt", 'r')
line = f.readline().split(",")
f.close()
code = [int(x) for x in line]

alpha = ''.join([chr(i+ord('a')) for i in range(26)])
keys = permutations(alpha, 3)
decodes = []

for key in keys:
    s = ''
    e_count = 0
    ascii_sum = 0
    for i in range(len(code)):
        c = chr(code[i]^ord(key[i%3]))
        if c == ' ': e_count += 1
        s += c
        ascii_sum += ord(c)
    decodes.append((e_count,key,s,ascii_sum))

decodes.sort(reverse=True)
for i in range(10):
    print decodes[i]
