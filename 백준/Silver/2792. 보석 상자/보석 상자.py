n, m = map(int, input().split())
 
arr = []
for i in range(m):
    arr.append(int(input()))

arr.sort()

def check(x):
    total = 0
    for i in range(len(arr)):
        total += arr[i] // x
        
        if arr[i] % x:
            total += 1

    return total <= n

s = 1
e = 100000000000
idx = 0
while s <= e:
    mid = (s + e) // 2
    
    if check(mid):
         idx = mid
         e = mid - 1
         
    else:
        s = mid + 1

print(idx)