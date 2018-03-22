a = [200, 100, 50, 20, 10, 5, 2, 1]
c = 0

def solve(rest, startIdx):
    global c
    if rest <= 0:
        if rest == 0: c += 1
        return

    for i in range(startIdx, len(a)):
        solve(rest - a[i], i)

solve(200, 0);
print c
