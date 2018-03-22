arr = []
f = open("triangle.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    arr.append(line[0:-1].split(' '))
f.close()

def go(arr, line, cur):
    if line >= len(arr): return 0
    l = go(arr, line+1, cur)
    r = go(arr, line+1, cur+1)
    return int(arr[line][cur]) + max(l,r) 

print go(arr, 0, 0)
