import sys
input = sys.stdin.readline


def find_(x):
    if par[x] == x:
        return x
    
    else:
        return find_(par[x])

def union_(a, b):
    a, b = find_(a), find_(b)
    
    if rnk[a] > rnk[b]:
        par[b] = a
        
    if rnk[b] > rnk[a]:
        par[a] = b
        
    else:
        rnk[a] += 1
        par[b] = a
    

n, m = map(int, input().split())

par = [i for i in range(n + 1)]
rnk = [1 for _ in range(n + 1)]
for i in range(1,m + 1):
    a, b = map(int, input().split())
    
    a, b = find_(a), find_(b)
    
    if a == b:
        print(i)
        exit()
        
    union_(a, b)
    
print(0)