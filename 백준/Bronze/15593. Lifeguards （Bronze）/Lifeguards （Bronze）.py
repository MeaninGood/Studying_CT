n = int(input())
times = [list(map(int, input().split(' '))) for _ in range(n)]

arr = [0 for _ in range(1010)]
for x, y in times:
    for i in range(x, y):
        arr[i] += 1
    
mx = 0
for i in range(n):
    cnt = 0
    for j in range(1010):
        x, y = times[i]
        
        if not arr[j] or (x <= j < y and arr[j] - 1 <= 0):
            continue

        cnt += 1

    mx = max(mx, cnt)
    
print(mx)