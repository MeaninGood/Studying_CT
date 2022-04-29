# from pprint import pprint

# n, m = map(int, input().split())
# arr = [input() for _ in range(n)]

# visited = [[False for i in range(m)] for j in range(n)]
# print(arr)

# cnt = 0
# for i in range(n):
#     for j in range(m):
#         if visited[i][j]:
#             continue
        
#         if arr[i][j] == '-':
#             for k in range(j + 1, m):                
#                 if visited[j][k]:
#                     continue
                                
#                 if arr[j][k] == arr[j][k - 1]:
#                     visited[j][k] = True
#                     visited[j][k - 1] = True

                    
#                     if k == m - 1:
#                         cnt += 1
#                         break
                    
#                     print(f'같을 때의 visitied {i}')
#                     pprint(visited)
#                     continue
                    
#                 elif arr[j][k] != arr[j][k - 1]:
#                     visited[j][k] = True
#                     cnt += 1
#                     print(f'다를 때의 visited {i}')
#                     pprint(visited)
        
#         # if arr[i][j] == '|':
#         #     if i + 1 == n:
#         #         continue
            
#         #     elif arr[i][j] == arr[i + 1][j]:
#         #         visited[i][j] = True
#         #         visited[i + 1][j] = True
#         #         cnt += 1
                
#         #     elif arr[i][j] != arr[i + 1][j]:
#         #         visited[i][j] = True
#         #         cnt += 1
# print(cnt)





from pprint import pprint

n, m = map(int, input().split())
arr = [input() for _ in range(n)]

visited = [[False for i in range(m)] for j in range(n)]

cnt = 0
for i in range(n):
    for j in range(m):
        if visited[i][j]:
            continue
        
        if arr[i][j] == '-':
            for k in range(j + 1, m):
                if arr[i][j] != arr[i][k]:
                    break 
                visited[i][k] = True
                
            cnt += 1
        
        if arr[i][j] == '|':
            for l in range(i + 1, n):
                if arr[i][j] != arr[l][j]:
                    break
                
                visited[l][j] = True
                
            cnt += 1
print(cnt)