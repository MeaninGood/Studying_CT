import sys
input = sys.stdin.readline


def find_(x):
    if par[x] == x:
        return x
    else:
        par[x] = find_(par[x])
        return par[x]

def union_(a, b):
    a, b = find_(a), find_(b)
    
    if rnk[a] < rnk[b]:
        par[a] = b
        
    elif rnk[a] > rnk[b]:
        par[b] = a
        
    else:
        par[b] = a
        rnk[a] += 1


n = int(input())
arr = []

for i in range(n):
    a, b, c = map(int, input().split())
    arr.append([a, b, c, i])

v = []
for k in range(3):
    arr.sort(key = lambda x: x[k])
    for i in range(1, n):
        v.append([abs(arr[i][k] - arr[i - 1][k]), arr[i][3], arr[i - 1][3]])
        
v.sort(key = lambda x: x[0])


par = [i for i in range(n)]
rnk = [0 for i in range(n)]

ans = 0
cnt = 0
for i in range(len(v)):
    a, b, c = v[i][1], v[i][2], v[i][0]
    
    a, b = find_(a), find_(b)
    
    if par[a] == par[b]:
        continue
    
    union_(a, b)
    ans += c
    cnt += 1
    
    if cnt == n - 1:
        print(ans)
        break