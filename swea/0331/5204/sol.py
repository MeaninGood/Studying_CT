def msort(s, e):
    global arr
    global cnt
    
    if s >= e:
        return
    
    mid = (s + e) // 2
    
    if (e - s + 1) % 2:
        mid -= 1
    
    msort(s, mid)
    msort(mid + 1, e)
    
    if arr[mid] > arr[e]:
        cnt += 1
    
    arr2 = []
    s1 = s
    s2 = mid + 1
    
    while s1 <= mid and s2 <= e:
        if arr[s1] <= arr[s2]:
            arr2.append(arr[s1])
            s1 += 1
        else:
            arr2.append(arr[s2])
            s2 += 1
            
    while s1 <= mid:
        arr2.append(arr[s1])
        s1 += 1
    
    while s2 <= e:
        arr2.append(arr[s2])
        s2 += 1
        
    for i in range(len(arr2)):
        arr[i + s] = arr2[i]
        
        
T = int(input())

for tc in range(1, T + 1):   
    n = int(input())
    arr = list(map(int, input().split()))

    cnt = 0
    msort(0, len(arr) - 1)

    print(f'#{tc} {arr[n // 2]} {cnt}')