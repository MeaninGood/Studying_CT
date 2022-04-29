# arr = input().split('.')

# v = [[] for _ in range(len(arr))]
# v = []
# print(arr)
# visited = [False for _ in range(len(arr))]
# for i in range(len(arr)):
#     if visited[i]:
#         continue
    
#     tmp = [arr[i]]
#     visited[i] = True
#     print(tmp)
#     if arr[i] == '.':
#         v.append(tmp)
#         continue
    
#     for j in range(1, len(arr)):
#         if arr[j - 1] != arr[j]:
#             break
#         tmp.append('X')
#         visited[j] = True
    
#     if len(tmp) % 2 and arr[i] != '.':
#         print(-1)
#         break
    
#     if len(tmp) >= 4:
#         for k in range((len(v[i]) // 4) * 4):
#             tmp[k] = 'A'
    
#     v.append(tmp)

arr = input().split('.')
v = [[] for _ in range(len(arr))]
# print(v)
for i in range(len(arr)):
    # if len(arr[i]) == 0:
    #     v[i].append('.')
    for j in range(len(arr[i])):
        # a = arr[i][j].replace('X', 'B')
        v[i].append('B')

flag = False
for i in range(len(v)):
    if len(v[i]) >= 4:
        for j in range(0, (len(v[i]) // 4) * 4):
            v[i][j] = 'A'
            # print(arr[i][j])
    if len(v[i]) % 2 and v[i] != []:
        flag = True
        break
# print(v)
if flag:
    print(-1)
else:
    for i in range(len(v)):
        if i == len(v) - 1:
            print(''.join(v[i]))
            break
        
        if len(v[i]) > 0:
            print(''.join(v[i]), end = '')
            print('.', end = '')
        elif len(v[i]) == 0:
            print('.', end = '')

