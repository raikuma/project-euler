f = open("names.txt", 'r')
line = f.readline()
f.close()

arr = line[1:-1].split('","')
arr.sort()

result = 0
index = 1
for name in arr:
    score = 0
    for c in name:
        score += ord(c) - ord('A') + 1
    score *= index
    result += score
    index += 1

print result
