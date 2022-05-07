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
    
    if rk[a] > rk[b]:
        par[b] = a
        
    elif rk[a] < rk[b]:
        par[a] = b
        
    else:
        par[a] = b
        rk[b] += 1


n = int(input())
m = int(input())

v = []
for i in range(m):
    a, b, c = map(int, input().split())
    v.append([a, b, c])

v.sort(key = lambda x: x[2])
par = [i for i in range(n + 1)]
rk = [0 for _ in range(n + 1)]

cnt = 0
total = 0
for i in range(m):
    a, b, c = v[i]
    
    a = find_(a)
    b = find_(b)
    
    if a == b:
        continue
    
    union_(a, b)
    cnt += 1
    total += c
    
    if cnt == n - 1:
        break
    
print(total)
    