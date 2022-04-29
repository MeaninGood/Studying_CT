import sys
input = sys.stdin.readline

n = int(input())

arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append([a, b])
    
arr.sort(key = lambda x: x[0])

total = -1000000
idx = 0
for i in range(n):
    tmp = 0
    for j in range(i, n):
        if arr[i][0] - arr[j][1] < 0:
            continue
        
        tmp += arr[i][0] - arr[j][1]

    a = max(total, tmp)
    if total < tmp:
        total = tmp
        idx = i

if total == 0:
    print(0)
elif total > 0:
    print(arr[idx][0])