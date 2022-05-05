n, k = map(int, input().split())

arr = [int(input()) for _ in range(n)]
arr.sort(reverse=True)


cnt = 0
for i in range(n):
    if k - arr[i] < 0:
        continue
    
    else:
        while 1:
            a = k - arr[i]
            if a < 0:
                break

            cnt += 1
            k -= arr[i]

print(cnt)