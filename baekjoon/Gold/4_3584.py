import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    n = int(input())
    
    par = [0 for i in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        
        par[b] = a
        
    
    x, y = map(int, input().split())
    
    a = []
    while x != 0:
        a.append(x)
        x = par[x]
        
    b = []
    while y != 0:
        b.append(y)
        y = par[y]
        
    idx1 = len(a) - 1
    idx2 = len(b) - 1
    while idx1 >= 0 and idx2 >= 0 and a[idx1] == b[idx2]:
        idx1 -= 1
        idx2 -= 1
    
    print(a[idx1 + 1])
        
    