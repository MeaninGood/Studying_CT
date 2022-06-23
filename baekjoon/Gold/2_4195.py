import sys
input = sys.stdin.readline


def find_(x):
    par[x] = par.get(x, x)
    
    if par[x] == x:
        return x
    
    return find_(par[x])


def union_(a, b):
    a, b = find_(a), find_(b)
    
    rnk[a] = rnk.get(a, 0)
    rnk[b] = rnk.get(b, 0)
    sz[a] = sz.get(a, 1)
    sz[b] = sz.get(b, 1)
    
    if rnk[a] > rnk[b]:
        par[b] = a
        sz[a] += sz[b]
    
    elif rnk[a] < rnk[b]:
        par[a] = b
        sz[b] += sz[a]
        
    else:
        par[b] = a
        rnk[a] += 1
        sz[a] += sz[b]
    

T = int(input())
for tc in range(T):
    n = int(input())
    
    par = {}
    rnk = {}
    sz = {}
    for _ in range(n):
        a, b = input().split()
        
        a, b = find_(a), find_(b)
        
        if a == b:
            print(max(sz[a], sz[b]))
            continue
        
        union_(a, b)
        print(max(sz[a], sz[b]))