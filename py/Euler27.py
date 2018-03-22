import math

def isPrime(n):
    if n < 0: return False
    for i in range(2, (int)(math.sqrt(n))+1):
        if n%i == 0: return False
    return True

def main():
    m = 0
    t = 0
    info = (0,0)
    for a in range(-999, 1000):
        for b in range(-999, 1000):
            n = 0
            while isPrime(n*n+a*n+b):
                n += 1
            if n > m: m = n; t = a*b; info = (a,b)
    print info[0], info[1], m, t

if(__name__ == "__main__"):
    main()
