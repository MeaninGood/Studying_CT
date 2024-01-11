import sys
input = lambda: sys.stdin.readline().strip()

a, b = map(int, input().split(' '))

ans = 0
for i in range(a, b + 1):
    cnt = 0
    x = i
    while x % 2 == 0:
        cnt += 1
        x //= 2
    ans += 2 ** cnt if cnt else 1
    
print(ans)