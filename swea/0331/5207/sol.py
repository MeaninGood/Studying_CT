T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    arr = sorted(list(map(int, input().split())))
    arr2 = list(map(int, input().split()))

    cnt = 0
    for i in arr2:
        s = 0
        e = n - 1
        v1, v2 = 0, 0
        while s <= e:
            
            mid = (s + e) // 2
            
            if arr[mid] == i:
                if v1 < 2 and v2 < 2:
                    cnt += 1
                break
                
            elif arr[mid] < i:
                s = mid + 1
                v1 += 1
                v2 = 0
            
            else:
                e = mid - 1
                v2 += 1
                v1 = 0
                        
    print(f'#{tc} {cnt}')

'''
5 5
1 3 5 7 9
1 2 3 4 5
3??

'''