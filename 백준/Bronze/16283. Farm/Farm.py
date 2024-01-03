import sys
input = lambda : sys.stdin.readline().strip()

a, b, n, w = map(int, input().split(' '))
ans = []
for i in range(1, n + 1 // 2):
    if (a * i) + b * (n - i) == w:
        ans.append([i, n - i])
    
if len(ans) > 1 or len(ans) == 0:
    print(-1)
else:
    print(*ans[0])
