f = open('../matrix.txt')
d = f.read()
f.close()
d = d.strip().split()
d = [x.split(',') for x in d]
init_matrix = [[int(x[i]) for x in d] for i in range(0, 80)]
min_matrix = [[-1]*80 for _ in range(80)]
min_matrix[0][0] = init_matrix[0][0]
candi_matrix = [[[] for _ in range(80)]*80 for _ in range(80)]
candi_matrix[0][0] = [(0, 1), (1, 0)]

def spread(x, y):
    global candi_matrix
    for c in candi_matrix[y][x]:
        nx, ny = c
        if (0 <= nx < 80) and (0 <= ny < 80):
            if (min_matrix[ny][nx] == -1 or min_matrix[ny][nx] > init_matrix[ny][nx] + min_matrix[y][x]):
                min_matrix[ny][nx] = init_matrix[ny][nx] + min_matrix[y][x]
                candi_matrix[ny][nx] = [(nx+1, ny), (nx, ny+1), (nx-1, ny), (nx, ny-1)]
    candi_matrix[y][x] = []

while True:
    for i in range(80):
        for j in range(80):
            spread(i, j)
    c = 0
    for i in range(80):
        for j in range(80):
            c += len(candi_matrix[i][j])
    if c == 0:
        break
print(min_matrix[79][79])