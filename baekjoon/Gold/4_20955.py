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
        
    elif rnk[a] < rnk[b]:
        par[a] = b
        
    else:
        par[b] = a
        rnk[a] += 1

n, m = map(int, input().split())

par = [i for i in range(n + 1)]
rnk = [0 for i in range(n + 1)]

ans = 0
cnt = 0
for _ in range(m):
    a, b = map(int, input().split())
    
    a, b = find_(a), find_(b)
    
    if a == b:
        ans += 1
        continue
    
    union_(a, b)
    cnt += 1
    
ans += n - cnt - 1

print(ans)