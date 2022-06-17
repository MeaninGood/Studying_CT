import sys
input = sys.stdin.readline


def find_(x):
    if par[x] == x:
        return x
    else:
        x = find_(par[x])
        return x
    

def union_(a, b):
    a, b = find_(a), find_(b)
    
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
        

n, m, k = map(int, input().split())
v = [[] for _ in range(n + 1)]
par = [i for i in range(n + 1)]
rnk = [0 for _ in range(n + 1)]
sz = [1 for _ in range(n + 1)]

x, y = 0, 0
for i in range(1, m + 1):
    a, b = map(int, input().split())
    
    if i == k:
        x, y = a, b
        continue
    
    a, b = find_(a), find_(b)
    
    if a == b:
        continue
    
    union_(a, b)

x, y = find_(x), find_(y)

if x == y:
    print(0)
else:
    print(sz[x] * sz[y])