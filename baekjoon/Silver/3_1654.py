n, m = map(int, input().split())
arr = [int(input()) for i in range(n)]
arr.sort()
s = 1
e = arr[n - 1]

while s <= e:
    mid = (s + e) // 2

    cnt = 0
    for i in range(n):
        cnt += arr[i] // mid
    
    if cnt < m:
        e = mid - 1
    
    if cnt >= m:
        s = mid + 1
        

print(e)