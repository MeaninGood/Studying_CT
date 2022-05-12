import sys
input = sys.stdin.readline


def find_(x):
    if par[x] == x:
        return x
    
    return find_(par[x])

def union_(a, b):
    a, b = find_(a), find_(b)
    
    if a == b:
        return
    
    if rnk[a] > rnk[b]:
        par[b] = a
    
    elif rnk[a] < rnk[b]:
        par[a] = b
        
    else:
        par[a] = b
        rnk[b] += 1
    

n, m = map(int, input().split())
arr = ['#'] + list(map(str, input().split()))
v = [list(map(int, input().split())) for _ in range(m)]
v.sort(key = lambda x: x[2])

par = [i for i in range(n + 1)]
rnk = [0 for _ in range(n + 1)]


cnt = 0
total = 0
for a, b, c in v:
    if arr[a] == arr[b]:
        continue
    
    a, b = find_(a), find_(b)
    
    if a == b:
        continue
    
    union_(a, b)
    cnt += 1
    total += c
    
    if cnt == n - 1:
        break
    
print(total if cnt == n - 1 else -1)