n = int(input())

arr = [i for i in range(65)]

s = 1
e = 64
cnt = 1

if n < 64:
    while 1:
        mid = (s + e) // 2
        
        if n == arr[mid]:
            break
        
        if n < arr[mid]:
            e = mid - 1
        
        if n > arr[mid]:
            s = mid + 1
            cnt += 1

    print(cnt)

else:
    print(1)