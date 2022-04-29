n, m = map(int, input().split())
arr = [input() for _ in range(n)]

arr2 = []
for i in range(m):
    tmp = ''
    for j in range(n):
        # arr2[i][j] = arr[j][i]
        tmp += arr[j][i]
        
    arr2.append(tmp)


v = []
for i in range(n):
    v.append(arr[i].split('#'))

for i in range(m):
    v.append(arr2[i].split('#'))

ans = []
for i in range(len(v)):
    for j in v[i]:
        if len(j) >= 2:
            ans.append(j)
            
ans.sort()
print(ans[0])