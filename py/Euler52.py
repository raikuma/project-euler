from lib import isAnagram

n = 0
while True:
    n += 1

    flag = False
    for i in range(2, 7):
        if not isAnagram(str(n), str(n*i)):
            flag = True
            break

    if flag: continue

    break

print(n)
