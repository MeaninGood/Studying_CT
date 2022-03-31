def qsort(arr):
    if len(arr) <= 1:
        return arr
    
    pv = arr[len(arr) // 2]
    larr, earr, garr = [], [], []
    
    for num in arr:
        if num < pv:
            larr.append(num)
        
        elif num > pv:
            garr.append(num)
        
        else:
            earr.append(num)
    
    return qsort(larr) + earr + qsort(garr)

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    
    print(f'#{tc} {qsort(arr)[n // 2]}')