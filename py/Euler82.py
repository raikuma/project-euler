f = open('matrix.txt')
d = f.read()
f.close()
d = d.split('\n')[0:-1]
d = [x.split(',') for x in d]
s = [[int(x[i]) for x in d] for i in range(0, 80)]
r = [s[0]]
for i in range(1, 80):
    r.append([])
    for j in range(0, 80):
        m = []
        for k in range(0, 80):
            if j > k:
                t = sum(s[i][k:j+1])
            else:
                t = sum(s[i][j:k+1])
            m.append(r[i-1][k] + t)
        r[i].append(min(m))

print(r, min(r[79]))
