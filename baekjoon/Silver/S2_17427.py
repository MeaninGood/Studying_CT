import sys
input = lambda : sys.stdin.readline().strip()

n = int(input())
ans = 0

for i in range(1, n + 1):
    ans += i * (n // i)
print(ans)