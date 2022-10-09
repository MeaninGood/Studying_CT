# 여행 가자

import sys
input = lambda : sys.stdin.readline().strip()


def find_(x):
    if par[x] != x:
        par[x] = find_(par[x])

    return par[x]

def union_(a, b):
    a, b = find_(a), find_(b)

    if rnk[a] > rnk[b]:
        par[b] = a
        sz[a] += sz[b]
    
    elif rnk[b] > rnk[a]:
        par[a] = b
        sz[b] += sz[a]

    else:
        rnk[a] += 1
        par[b] = a
        sz[a] += sz[b]

n = int(input())
m = int(input())

par = [i for i in range(n + 1)]
rnk = [0 for i in range(n + 1)]
sz = [1 for i in range(n + 1)]

arr =[[0] + list(map(int, input().split())) for _ in range(n)]
z = len(arr[0])

arr = [[0 for _ in range(z)]] + arr

for i in range(1, n + 1):
    for j in range(len(arr[i])):
        if arr[i][j] == 1:
            union_(i, j)

v = set(map(find_, map(int, input().split())))

if len(v) == 1:
    print('YES')
else:
    print('NO')
