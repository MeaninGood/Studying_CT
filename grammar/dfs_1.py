# # 연결 요소의 크기 구하는 함수
# # def dfs(cur):
# #     ret = 1
# #     visited[cur] = True

# #     for nxt in v[cur]:
# #         if visited[nxt]:
# #             continue

# #         ret += dfs(nxt) # 각 노드당 ret +1 씩 돼서 더해짐

# #     return ret

# # n = int(input())
# # m = int(input())
# # v = [[] for i in range(n + 1)]

# # for i in range(m):
# #     a, b = map(int, input().split())

# #     v[a].append(b)
# #     v[b].append(a)

# # visited = [False for i in range(n + 1)]

# # print(dfs(1))


# def dfs(cur):
#     visited = True
    
#     for nxt in v[cur]:
#         if visited[nxt]:
#             continue
        
#         dfs(nxt)

# # 연결 요소 개수 구하기
# n, m = map(int, input())
# v = [[] for i in range(n + 1)]

# for i in range(m):
#     a, b = map(int, input().split())
    
#     v[a].append(b)
#     v[b].append(a)
    

# visited = [False for i in range(n + 1)]

# cnt = 0
# for i in range(1, n + 1):
#     if visited[i]:
#         continue
    
#     dfs(i)
#     cnt += 1
    
# print(cnt)