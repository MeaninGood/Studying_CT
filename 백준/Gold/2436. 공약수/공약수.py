import sys
input = lambda : sys.stdin.readline().strip()
    
def gcd(a, b):
    a, b = max(a, b), min(a, b)
    
    while a % b != 0:
        a, b = b, a % b
    return b

a, b = map(int, input().split(' '))

mn = 1 << 31
x, y = 0, 0

for i in range(a, b + 1, a):
    if i * i > a * b:
        break
    
    for j in range(i, b + 1, a):
        if i * j > a * b:
            break
        
        if i * j == a * b and gcd(i, j) == a:
            if i + j < mn:
                x, y = i, j
                mn = min(mn, i + j)
print(x, y)