import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())
cnt = 1
for i in range(2, n + 1):
    if i * i > n:
        break

    cnt += 1

print(cnt)