f = open('matrix.txt')
d = f.read()
f.close()
d = d.split('\n')[0:-1]
d = [x.split(',') for x in d]
r = []
for i in range(0, 80):
    r.append([])
    for j in range(0, 80):
        if i == 0 and j == 0:
            t = 0
        elif i == 0:
            t = r[i][j-1]
        elif j == 0:
            t = r[i-1][j] 
        else:
            t = min(r[i-1][j], r[i][j-1])
        r[i].append(t + int(d[i][j]))

f = open('result.txt', 'w')
f.write(str(r))
f.close()

print(r[79][79])
