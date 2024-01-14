import sys
input = lambda: sys.stdin.readline().strip()

def gcd(a, b):
    while a % b != 0:
        a, b = b, a % b
        
    return b > 1

m = 1001
prefix = [0 for i in range(m)]
prefix[1] = 3
for i in range(2, m):
    cnt = 1
    
    for j in range(2, i):
        if not gcd(i, j):
            cnt += 1
            
    prefix[i] = prefix[i - 1] + cnt * 2

c = int(input())
for _ in range(c):
    n = int(input())
    print(prefix[n])