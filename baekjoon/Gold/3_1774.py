import sys, heapq
input = sys.stdin.readline

def get_dist(x, y):
    pass


def find_(x):
    if par[x] == x:
        return x
    
    return find_(par[x])
    
    
def union_(a, b):
    a, b = find_(a), find_(b)
    
    if rnk(a) > rnk(b):
        par[b] = a
    
    elif rnk(a) < rnk(b):
        par[a] = b
        
    else:
        par[a] = b
        rnk[b] += 1


n, m = map(int, input().split())

par = [i for i in range(n + 1)]
rnk = [0 for i in range(n + 1)]
dist = [100000000 for _ in range(n + 1)]
arr = []
for i in range(n):
    a, b = map(int, input().split())
    c = (a ** 2 + b ** 2) ** (1 / 2)
    arr.append([a, b, c])
    
for i in range(m):
    a, b = map(int, input().split())
    c = (a ** 2 + b ** 2) * 1/2
    
print(arr)