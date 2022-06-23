import sys
input = sys.stdin.readline


def find_(x):
    if par[x] == x:
        return x
    
    return find_(par[x])


def union_(a, b):
    a, b = find_(a), find_(b)
    
    if rnk[a] > rnk[b]:
        par[b] = a
        sz[a] += sz[b]
        
    elif rnk[a] < rnk[b]:
        par[a] = b
        sz[b] += sz[a]
        
    else:
        par[a] = b
        rnk[b] += 1
        sz[b] += sz[a]


n = int(input())
par = [i for i in range(1000010)]
rnk = [0 for _ in range(1000010)]
sz = [1 for _ in range(1000010)]

for i in range(n):
    tmp = input().split()
    
    if tmp[0] == 'I':
        a, b = find_(int(tmp[1])), find_(int(tmp[2]))
        
        if a == b:
            continue
        
        union_(a, b)

    else:
        a = int(tmp[1])
        print(sz[find_(a)])
        