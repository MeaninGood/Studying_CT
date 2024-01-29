import sys

input = lambda : sys.stdin.readline().strip()

n, m = map(int, input().split())
aarr = list(map(int, input().split()))
barr = list(map(int, input().split()))


newarr = []
a, b = 0, 0
while a != n or b != m:
    if a == n:
        newarr.append(barr[b])
        b += 1
        
    elif b == m:
        newarr.append(aarr[a])
        a += 1
        
    else:
        if aarr[a] < barr[b]:
            newarr.append(aarr[a])
            a += 1
            
        else:
            newarr.append(barr[b])
            b += 1
        
print(*newarr)