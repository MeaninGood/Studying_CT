import sys
input = sys.stdin.readline

n = int(input())

ans = 0

for i in range(2, n + 1):
    ans += (i * ((n // i) - 1)) % 1000000
    
print(ans % 1000000)