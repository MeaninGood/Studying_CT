n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

s = arr[0]
e = arr[0] + m
cnt = 1
for i in range(n):
    if s <= arr[i] < e:
        continue
    
    else:
        s = arr[i]
        e = arr[i] + m
        cnt += 1

print(cnt)