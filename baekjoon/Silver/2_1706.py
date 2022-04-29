# n, m = map(int, input().split())
# arr = [input() for _ in range(n)]

# v = []
# for i in range(n):
#     tmp1 = []
#     tmp2 = []
#     for j in range(i, m):
#         if arr[i][j] == '#':
#             v.append(tmp1)
#             break
        
#         tmp1.append(arr[i][j])
        
#     for j in range(i, n):
#         if arr[j][i] == '#':
#             v.append(tmp2)
#             break
        
#         tmp2.append(arr[j][i])


# n, m = map(int, input().split())
# arr = [input() for _ in range(n)]

# v = []
# for i in range(n):
#     tmp1 = []
#     for j in range(i, m):
#         if arr[i][j] == '#':
#             v.append(tmp1)
#             tmp1 = []
#             continue
        
#         tmp1.append(arr[i][j])


    
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