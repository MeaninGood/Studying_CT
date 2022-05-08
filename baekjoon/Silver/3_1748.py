import sys
input = sys.stdin.readline

n = int(input())

tmp = n
cnt = 1
idx = 9
ans = 0
while tmp // 10:
    ans += cnt * idx
    n -= idx
    cnt += 1
    idx *= 10
    tmp //= 10

ans += n * cnt
print(ans)