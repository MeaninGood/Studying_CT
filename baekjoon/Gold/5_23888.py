import sys
input = lambda : sys.stdin.readline().strip()

def gcd(a, b):
    a, b = max(a, b), min(a, b)
    if b == 0: return a
    while a % b != 0:
        a, b = b, a % b
        
    return b


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
            print(gcd(a, d))