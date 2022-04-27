arr = input().split('-')

for i in range(len(arr)):
    if '+' in arr[i]:
        tmp = arr[i].split('+')
        total = 0
        for j in tmp:
            total += int(j)
            
        arr[i] = total
        
if len(arr) == 1:
    print(arr[0])

else:
    ans = int(arr[0])
    for i in range(1, len(arr)):
        ans -= int(arr[i])
    print(ans)


