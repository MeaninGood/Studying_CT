import sys
innput = sys.stdin.readline

n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]

a, b = map(int, input().split())
total = 0
for i in range(n - 1):
    c, d = map(int, input().split())
    total += (a * d) + (b * c)
    a, b = a + c, b + d
    
print(total) 