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
    
    # 둘 다 -1인 경우 : arc 무조건 패
    if lb == ub == -1:
        hi += m
    
    # lb만 있는 경우 : arc 패 또는 무승부
    elif lb != -1 and ub == -1:
        hi += lb
        tie += m - lb
    
    # 나머지 : hi, arc, tie 골고루 있음
    else:
        hi += lb
        arc += m - ub
        tie += ub - lb
    
print(hi, arc, tie)