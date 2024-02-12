import sys
input = lambda : sys.stdin.readline().strip()

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]

d = {}
for i in range(m):
    tmp = ''
    for j in range(n):
        tmp += arr[j][i]

    d[tmp] = d.get(tmp, 0) + 1

cnt = 0
for i in range(n - 1):
    tmp = {}
    for key in d.keys():
        key = key[1:]
        tmp[key] = tmp.get(key, 0) + 1

        if tmp[key] >= 2:
            print(cnt)
            exit()

    d = tmp
    cnt += 1

print(cnt)