length = 50
stack = [1] * length
s = length
c = 1

while True:
    p = stack.pop()
    s -= p
    if p == 1:
        if len(stack) > 0 and stack[-1] > 1:
            continue
        stack.append(3)
        s += 3
    elif p >= 3:
        stack.append(p+1)
        s += p+1
    # s = sum(stack)
    if s == length:
        c += 1
        t = stack.pop()
        s -= t
        if t == length:
            break
    elif s > length:
        s -= stack.pop()
    elif s < length:
        t = length - s
        stack += [1] * t
        s += t
        c += 1
print(c)