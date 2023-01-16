import sys
input = lambda : sys.stdin.readline().strip()


n, x, y = map(int, input().split())

arr = []
cnt = 1
for i in range(1, n + 1, 2):
    if i == x and i + 1 == y:
        print(cnt)
        exit()
    
    if i == y and i + 1 == x:
        print(cnt)
        exit()
    
    if i + 1 == x:
        arr.append(x)
        
    elif i + 1 == y:
        arr.append(y)
    
    else:
        arr.append(i)

tmp = []

while arr:
    m = len(arr)
    for i in range(0, m, 2):
        if arr[i] == x and (i + 1 < m and arr[i + 1] == y):
            print(cnt + 1)
            exit()
            
        if arr[i] == y and (i + 1 < m and arr[i + 1] == x):
            print(cnt + 1)
            exit()
            
        if arr[i] == x or (i + 1 < m and arr[i + 1] == x):
            tmp.append(x)
        
        elif arr[i] == y or (i + 1 < m and arr[i + 1] == y):
            tmp.append(y)
        
        else:
            tmp.append(arr[i])

    cnt += 1
    arr = tmp
    tmp = []

print(-1)