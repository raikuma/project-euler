arr = []
f = open("triangle.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    a = line[0:-1].split(' ')
    arr.append([int(x) for x in a])
f.close()

print arr[0]
for n in range(1, len(arr)):
    arr[n][0] += arr[n-1][0]
    for i in range(1, len(arr[n])-1):
        arr[n][i] += max(arr[n-1][i-1], arr[n-1][i])
    arr[n][-1] += arr[n-1][-1]
    print arr[n]

print max(arr[-1])
