from collections import deque

def bfs(s):
    que = deque()
    visited = [False for i in range(e + 1)]
    cnt = 1
    
    que.append(s)
    visited[s] = True
    
    while len(que) > 0:
        size = len(que)
        
        for _ in range(size):
            cur = que[0]
            que.popleft()
            print(cur, end = ' ')
            
            for nxt in v[cur]:
                if visited[cur]:
                    continue
                
                que.append(v[nxt])
                visited[nxt] = True
        cnt += 1
        
    return cnt

e, n = map(int, input().split())
arr = [0] + list(map(int, input().split()))
v = [[] for _ in range(e * 2)]
for i in range(1, e * 2, 2):
    v[arr[i]].append(arr[i + 1])
# print(arr)
    
# print(v)
print(bfs(n))

'''
5 1
2 1 2 5 1 6 5 3 6 4

'''

# visited = [False for i in range(e * 2)]
# def dfs(cur):
#     visited[cur] = True
    
#     cnt = 0
#     for nxt in v[cur]:
#         if visited[nxt]:
#             continue
        
#         cnt += 1
#         dfs(nxt)
#         visited[nxt] = False
#         cnt =
    

# for i in range(1, e + 2):
#         dfs(i)

    

            
            
    