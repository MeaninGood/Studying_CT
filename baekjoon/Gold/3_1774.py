import sys, heapq
input = sys.stdin.readline

def get_dist(a, b):
    x = a[0] - b[0]
    y = a[1] - b[1]
    return (x ** 2 + y ** 2) ** (1 / 2)   


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
        par[a] = b
        rnk[b] += 1


n, m = map(int, input().split())

par = [i for i in range(n + 1)]
rnk = [0 for i in range(n + 1)]
dist = [100000000 for _ in range(n + 1)]
arr = [[0, 0]]

for i in range(n):
    a, b = map(int, input().split())
    arr.append([a, b])
    
for i in range(m):
    a, b = map(int, input().split())
    union_(a, b)
    
data = []
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        data.append([get_dist(arr[i], arr[j]), i, j])
    
data.sort()

ans = 0
for d, a, b in data:
    if find_(a) != find_(b):
        ans += d
        union_(a, b)

print(f'{ans:.2f}')