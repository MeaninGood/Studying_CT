# 트리

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


idx = 1
while 1:
    n, m = map(int, input().split())

    if n == 0 and m == 0:
        exit()

    par = [i for i in range(n + 1)]
    rnk = [0 for _ in range(n + 1)]
    sz = [1 for _ in range(n + 1)]

    li = []
    for _ in range(m):
        x, y = map(int, input().split())
        
        a, b = find_(x), find_(y)

        if a == b:
            li.append(a)
            continue
        
        union_(x, y)

    for x in li:
        x = find_(x)
        for j in range(n + 1):
            if find_(j) == x:
                par[j] = 0

    cnt = 0
    for i in range(1, n + 1):
        if par[i] == i:
            cnt += 1

    if cnt == 0:
        print(f'Case {idx}: No trees.')

    elif cnt == 1:
        print(f'Case {idx}: There is one tree.')

    else:
        print(f'Case {idx}: A forest of {cnt} trees.')

    idx += 1