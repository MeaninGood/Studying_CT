import sys

input = lambda: sys.stdin.readline().strip()

n, m = map(int, input().split())
tarr = list(map(int, input().split()))
arr = sorted(list(map(int, input().split())))

hi, arc, tie = 0, 0, 0
for target in tarr:
    lb = -1
    s, e = 0, m - 1
    while s <= e:
        mid = (s + e) // 2
        
        if arr[mid] >= target:
            lb = mid
            e = mid - 1
            
        else:
            s = mid + 1
            
    ub = -1
    s, e = 0, m - 1
    while s <= e:
        mid = (s + e) // 2
        if arr[mid] > target:
            ub = mid
            e = mid - 1
            
        else:
            s = mid + 1
    
    if lb == ub == -1:
        hi += m
    elif lb != -1 and ub == -1:
        hi += lb
        tie += m - lb
        
    else:
        hi += lb
        arc += m - ub
        tie += ub - lb
    
print(hi, arc, tie)

