n = int(input())
arr = [list(map(str, input().split())) for _ in range(n)]

print(arr)

d = {}

for i in range(n):
    for j in range(len(arr[i])):
        for k in range(len(arr[i][j])):
            if arr[i][j][k] in d:
                continue
            d[arr[i][j][k].upper()] = d.get(arr[i][j][k].upper(), arr[i][j][k])
            
for i in range(len(arr)):
    for j in range(len(arr[i])):
        for k in range(len(arr[i][j])):
            if len(arr[i]) == 1 and k == 0:
                if arr[i][j][k] in d:
                    del d[arr[i][j][k]]
                    print(f'[{arr[i][j][k]}]', end = '')
                    print(arr[i][j][1:])
                    arr.remove(arr[i])

for i in range(len(arr)):
    for j in range(len(arr[i])):
        for k in range(len(arr[i][j])):
            if len(arr[i]) > 1 and j > 0 and k == 0:
                if arr[i][j][k] in d:
                    del d[arr[i][j][k]]
                    print(*arr[i][0:j], end = ' ')
                    print(f'[{arr[i][j][k]}]', end = '')
                    print(arr[i][j][1:], end = ' ')
                    print(*arr[i][j + 1:], end = ' ')
                    arr.remove(arr[i])

for i in range(len(arr)):
    for j in range(len(arr[i])):
        for k in range(len(arr[i][j])):
            if arr[i][j][k].upper() in d:
                if j == 0:
                    print(arr[i][j][0:k], end = '')
                    print(f'[{arr[i][j][k]}]', end = '')
                    print(arr[i][j][k:], end = ' ')
                    print(arr[i][0:j], end = ' ')
    
print(d)

'''
5
New
Open
Save
Save As New open
save All

'''