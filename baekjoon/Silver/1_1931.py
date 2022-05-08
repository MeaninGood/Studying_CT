import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key = lambda x: (x[1], x[0]))


e = 0
cnt = 0
for i in range(n):
    if arr[i][0] >= e:
        e = arr[i][1]
        cnt += 1

print(cnt)