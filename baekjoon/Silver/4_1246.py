n, m = map(int, input().split())
arr = [int(input()) for _ in range(m)]

arr.sort()

if n >= m:
    ans = -100000
    idx = 0
    for i in range(m):
        tmp = 0
        for j in range(i, m):
            tmp += arr[i]
        
        if tmp > ans:
            ans = tmp
            idx = arr[i]

if n < m:
    ans = -100000
    idx = 0
    for i in range(m):
        tmp = 0
        cnt = 0
        for j in range(i, m):
            if cnt == n:
                break
            
            tmp += arr[i]
            cnt += 1

        if tmp > ans:
            ans = tmp
            idx = arr[i]
        
print(idx, ans)