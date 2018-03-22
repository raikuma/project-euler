def n2s(n):
    return ''.join(sorted(list(str(n))))

data = {}

i = 1
r = ''
while True:
    s = n2s(i**3)
    try:
        data[s][0] += 1
        data[s][1].append(i)
    except:
        data[s] = [1, [i]]
    if data[s][0] >= 5:
        break
    i += 1

print(data[s])
print(data[s][1][0]**3)
