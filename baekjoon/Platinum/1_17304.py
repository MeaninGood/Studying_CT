# 17304번_변호사들

## N명의 변호사는 서로를 변호하여 전원 무사히 무죄로 처리되려고 함
## 변호사들은 자신이 신뢰하는 변호사에게만 변호를 받을 수 있음
## 신뢰관계란 M개의 (A, B)쌍으로 표현됨
## 변호사 B가 변호사 A를 신뢰한다는 의미로 이 경우에만 변호사 A가 변호사 B를 변호할 수 있음
## 1명 이상의 변호를 받은 사람은 무조건 무죄가 됨
## 두 변호사 A, B에 대해 A가 B를 변호하고, B가 A를 변호하는 경우는 매우 수상하기 때문에 둘 모두 유죄
## 각 (A, B) 쌍에 대해 변호사 A가 변호사 B를 변호할지 말지를 선택하여 모든 변호사가 무죄가 되는 것이 가능한지 판정

'''
# 첫 줄에 N과 M이 주어진다. (1 ≤ N, M ≤ 200,000)
# 두 번째 줄부터 M 줄에 걸쳐 i번째 줄에는 서로 다른 두 정수 Ai, Bi
# 이는 변호사 Ai가 변호사 Bi를 변호할 수 있다는 뜻
# 주어지는 입력에서 순서쌍 (A, B)가 중복하여 나타나는 경우는 없다
## 모든 변호사가 1명 이상의 변호를 받고, 서로를 변호하는 변호사 쌍이 없도록 할 수 있는 경우 첫 줄에 YES
## 불가능한 경우 첫 줄에 NO를 출력

(입력)
3 3
1 2
2 3
3 1

(출력)
YES

'''

# from collections import deque

# def bfs(s):
#     que = deque()
#     visited = [False for i in range(n + 1)]
    
#     que.append(s)
    
#     while len(que) > 0:
#         size = len(que)
        
#         for _ in range(size):
#             cur = que.popleft()
            
#             for nxt in v[cur]:
#                 if nxt == 0:
#                     continue
#                 if visited[nxt] or nxt == 0:
#                     continue
                
#                 que.append(nxt)
#                 visited[nxt] = True
#                 v.pop(0)
#                 print(v)
    

# import sys
# sys.setrecursionlimit(100000)
# dp = [-1 for i in range(200010)]
# def dfs(cur):
#     ret = 0
    
#     if dp[cur] != -1:
#         return dp[cur]
    
#     for nxt in v[cur]:
#         if visited[nxt]:
#             continue

#         visited[nxt] = True
#         # v.pop(0)
#         ret = dfs(nxt) + 1
#     dp[cur] = ret
#     return dp[cur]


# n, m = map(int, input().split())
# v = [[] for _ in range(n + 1)]
# for i in range(m):
#     a, b = map(int, input().split())
    
#     v[a].append(b)
    
# print(v)

# for i in range(n + 1):
#     # if v[i] == []:
#     #     continue
#     bfs(i)

# visited = [False for _ in range(n + 1)]
# ans = []
# tmp = 0
# for i in range(1, n + 1):
#     if not visited[i]:
#         ans.append(dfs(i))
#         if dfs(i) == 2:
#             tmp += 1
# print(v)

# visited.pop(0)
# print(visited)
# print(tmp)


# # if tmp > 0 and False not in visited:
# #     print('NO')
# if tmp > 0:
#     for i in visited:
#         if i == False:
#             print('NO')
#     else:
#         print('NO')
    
            
# elif tmp == 0:
#     if False in visited:
#         print('NO')
#     else:
#         print('YES') 
    

import sys
from collections import deque
input = sys.stdin.readline



def bfs(s):
    que = deque()
    que.append(s)
    
    while que:
        size = len(que)
        
        for _ in range(size):
            cur = que.popleft()
            
            for nxt in v[cur]:
                if visited[nxt]:
                    continue
                
                que.append(nxt)
                visited[nxt] = True
                
n, m = map(int, input().split())
v = [[] for _ in range(n + 1)]

visited = [False for i in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    
    v[a].append(b)
    
    if b in v[a] and a in v[b]:
        continue
    
    bfs(a)
    
visited = [False for i in range(n + 1)]

    
bfs(1)
print(visited)


par = [i for i in range(1000010)]
rnk = [0 for i in range(1000010)]

def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def union_(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return

    if rnk[a] < rnk[b]:
        par[a] = b

    elif rnk[a] > rnk[b]:
        par[b] = a

    else:
        par[a] = b
        rnk[b] += 1

    