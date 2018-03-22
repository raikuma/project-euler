from math import *

def isPrime(n):
    if n==1: return False
    if n!=2 and n%2==0: return False
    for i in range(2, int(sqrt(n))+1):
        if n%i == 0: return False
    return True

def isPalin(s):
    l = len(s)
    return s[:floor(l/2)] == s[:floor(l/2):-1]

def isPanDigital(s):
    return ''.join(sorted(s)) == '123456789'

def getAnagram(string):
    arr = []
    
    l = len(string)
    for n in range(0, factorial(l)):
        c = l
        s = ''
        a = string
        while a:
            c -= 1
            b = factorial(c)
            d, n = divmod(n, b)
            s += a[d]
            a = a[0:d]+a[d+1:len(a)]

        arr.append(s)
    return arr

def getWordValue(s):
    s = s.upper()
    return sum([ord(c)-ord('A')+1 for c in s])

def isTriNumber(n):
    i = 1
    while n > 0:
        n -= i
        i += 1
    if n == 0: return True
    return False

def isAnagram(a, b):
    a = list(a)
    b = list(b)
    a.sort()
    b.sort()
    return a == b

def reverseStr(s):
    return s[::-1]

def Eratos(n):
    if n < 2:
        return []
    r = []
    candi = list(range(2, n+1))

    while candi:
        c = candi.pop(False)
        r.append(c)
        if c > sqrt(n):
            continue
        i = 2
        while c * i <= n:
            try:
                candi.remove(c * i)
            except:
                pass
            i += 1
        
    return r
    

def getPrime(n):
    #결과 값을 저장하는 목록을 미리 생성한다.
    result = []
    #전체 범위를 지정한다. : 1은 소수임을 알고 있으므로 제외하고 2부터 수행해야 하지만 초기값은 별도로 생성할 것이므로 3부터 999까지의 범위로 한다.
    candidates = list(range(3,n))
    #초기값을 설정한다.
    base = 2
    #초기값의 배수를 구하기 위한 임시 변수를 생성한다.
    product = base

    #전체 범위 내에서 "에라토스테네스의 체" 알고리즘을 수행한다.
    while candidates:
        #임시변수가 n미만일 때까지 다음을 수행한다.
        while product < n:
            #임시변수가 전체 범위내 존재한다면 :
            if product in candidates:
                #전체 범위 목록에서 임시변수를 삭제한다.
                candidates.remove(product)
            #임시변수는 기본값의 배수이다.
            product = product+base
        #결과 목록에 기본값을 추가한다.
        result.append(base)
        #다음 기본값은 (이미 걸러진)전체 목록의 첫 번째 값이다. : 1회 걸렀을 경우 2와 2의 배수를 모두 삭제했으므로 3이다.
        base = candidates[0]
        #초기값의 배수를 구하기 위해 임시 변수를 다시 생성한다.
        product = base
        #전체 범위에서 초기값을 제거한다.
        del candidates[0]
    # 범위 내의 마지막 기본값을 결과 목록에 추가한다.
    result.append(base)
    #결과 목록을 화면에 출력한다.
    return result