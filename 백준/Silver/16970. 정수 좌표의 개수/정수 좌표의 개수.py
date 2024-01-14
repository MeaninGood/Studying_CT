import sys
input = lambda : sys.stdin.readline().strip()

def gcd(a, b):
    if b == 0: return a
    
    while a % b != 0:
        a, b = b, a % b
        
    return b

n, m, k = map(int, input().split())

cnt = 0
for x1 in range(n + 1):
    for y1 in range(m + 1):
        for x2 in range(n + 1):
            for y2 in range(m + 1):
                # 시작점 포함 +1
                if gcd(abs(x2 - x1), abs(y2 - y1)) + 1 == k:
                    cnt += 1
                    
print(cnt // 2)