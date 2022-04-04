# 2668번_숫자고르기

## 세로 두 줄, 가로로 N개의 칸으로 이루어진 표
## 첫째 줄의 각 칸에는 정수 1, 2, …, N이 차례대로 들어 있고
## 둘째 줄의 각 칸에는 1이상 N이하인 정수가 들어 있다
## 첫째 줄에서 숫자를 적절히 뽑으면, 그 뽑힌 정수들이 이루는 집합과, 뽑힌 정수들의 바로 밑의 둘째 줄에 들어있는 정수들이 이루는 집합이 일치
## 이러한 조건을 만족시키도록 정수들을 뽑되, 최대로 많이 뽑는 방법을 찾는 프로그램을 작성

'''
# 첫째 줄에는 N(1≤N≤100)을 나타내는 정수 하나가 주어짐
# 그 다음 줄부터는 표의 둘째 줄에 들어가는 정수들이 순서대로 한 줄에 하나씩 입력
## 첫째 줄에 뽑힌 정수들의 개수를 출력
## 그 다음 줄부터는 뽑힌 정수들을 작은 수부터 큰 수의 순서로 한 줄에 하나씩 출력

(입력)
7
3
1
1
5
5
4
6

(출력)
3
1
3
5

'''

# def dfs(cur, visit):
#     visited[cur][visit] = True
#     ret = 1
    
#     for nxt in v[cur]:
#         if visited[nxt][visit] and cur == nxt:
#             return ret
#         elif visited[nxt][visit] and cur != nxt:
#             continue
        
#         ret += dfs(nxt, visit + 1) + 1
        
#     return ret

# n = int(input())
# v = [[] for i in range(n + 1)]
# for i in range(1, n + 1):
#     a = int(input())
#     v[i].append(a)

# for i in range(1, n + 1):
#     visited = [[False for _ in range(2)] for _ in range(n + 1)]
#     if not visited[i]:
#         dfs(i)
# print(v)


# import sys
# sys.setrecursionlimit(10000)
# def dfs(cur):
#     global ans
#     visited[cur] = True
    
#     ret = 1
    
#     for nxt in v[cur]:
#         if visited[nxt] and nxt == i:
#             ans.append(i)
#             return ret
        
#         elif visited[nxt] and nxt != i:
#             continue
        
#         ret += dfs(nxt) + 1
#         visited[nxt] = False
        
#     return ret

# n = int(input())
# v = [[] for i in range(n + 1)]
# for i in range(1, n + 1):
#     a = int(input())
#     v[i].append(a)

# ans = []
# total = 0
# for i in range(1, n + 1):
#     visited = [False for _ in range(n + 1)]
#     dfs(i)

# print(len(ans))
# for i in ans:
#     print(i)


import sys
sys.setrecursionlimit(10000)
def dfs(cur):
    global ans
    visited[cur] = True
    
    for nxt in v[cur]:
        if visited[nxt] and nxt == i:
            ans.append(i)
            return
        
        elif visited[nxt] and nxt != i:
            continue
        
        dfs(nxt)
        visited[nxt] = False

n = int(input())
v = [[] for i in range(n + 1)]
for i in range(1, n + 1):
    a = int(input())
    v[i].append(a)

ans = []
total = 0
for i in range(1, n + 1):
    visited = [False for _ in range(n + 1)]
    dfs(i)

print(len(ans))
for i in ans:
    print(i)