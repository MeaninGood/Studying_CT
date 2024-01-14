import sys
input = sys.stdin.readline

def gcd(m, n):
    if m < n:
        m, n = n, m
    
    if n == 0:
        return m
    
    if m % n == 0:
        return n
    
    else:
        return gcd(n, m % n)


a, d = map(int, input().split())
n = int(input())
for _ in range(n):
    qry, b, c = map(int, input().split())

    if qry == 1:
        sb = ((b - 1) * (2 * a + (b - 2) * d)) // 2
        sc = (c * (2 * a + (c - 1) * d)) // 2
        print(sc - sb)

    else:
        if b == c:
            print(a + (b - 1) * d)
        else:
            tmp = gcd(a, d)        
            print(tmp)