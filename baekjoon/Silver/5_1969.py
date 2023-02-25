import sys
input = lambda : sys.stdin.readline().strip()

n, m = map(int, input().split())
arr = [input() for _ in range(n)]


d = [{} for _ in range(m)]
for i in range(n):
    for j in range(m):
        d[j][arr[i][j]] = d[j].get(arr[i][j], 0) + 1

print(arr)
print(d)

total = n * m
answer =  ''
for i in range(m):
    tmp = list(d[i].items())
    tmp.sort(key = lambda x: (-x[1], x[0]))

    answer += tmp[0][0]
    total -= tmp[0][1]

print(answer)
print(total)