n = int(input())
arr = list(map(int, input().split()))
k = int(input())

arr.sort()
ans = 0
tmp = k
while arr != []:
    if tmp // len(arr) >= arr[0]:
        ans = max(ans, arr[0])
        tmp -= arr[0]
        arr.pop(0)
    else:
        ans = max(ans, tmp // len(arr))
        break
        
print(ans)