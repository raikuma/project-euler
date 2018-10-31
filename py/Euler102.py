# http://zockrworld.blogspot.com/2007/11/2%EC%B0%A8%EC%9B%90%EC%97%90%EC%84%9C-%EC%9E%84%EC%9D%98%EC%9D%98-%ED%95%9C-%EC%A0%90%EC%9D%B4-%EC%82%BC%EA%B0%81%ED%98%95-%EB%82%B4%EB%B6%80%EC%97%90-%EC%9E%88%EB%8A%94%EC%A7%80-%ED%8C%90%EB%B3%84%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95.html

# 내분점을 이용한 방법
def tri_in(v1, v2, v3):
    x1 = v2[0] - v1[0]
    y1 = v2[1] - v1[1]
    x2 = v3[0] - v1[0]
    y2 = v3[1] - v1[1]
    xp = 0 - v1[0]
    yp = 0 - v1[1]

    if x2*y1 - x1*y2 == 0:
        return False
    t2 = (xp*y1 - yp*x1) / (x2*y1 - x1*y2)
    if x1 == 0:
        return False
    t1 = (xp - t2*x2) / x1

    if 0 < t1 < 1 and 0 < t2 < 1 and t1 + t2 < 1:
        return True
    return False

# 외적의 방향을 이용한 방법
def tri_in2(v1, v2, v3):
    ab = v1[0]*v2[1] - v2[0]*v1[1]
    bc = v2[0]*v3[1] - v3[0]*v2[1]
    ca = v3[0]*v1[1] - v1[0]*v3[1]

    if all([ab>=0, bc>=0, ca>=0]) or all([ab<=0, bc<=0, ca<=0]):
        return True
    return False

f = open('../triangles.txt')
d = f.read().strip().split()
f.close()
c = 0
for x in d:
    t = [int(y) for y in x.split(',')]
    v = list(zip(t[::2], t[1::2]))
    if tri_in2(*v):
        c += 1

print(c)