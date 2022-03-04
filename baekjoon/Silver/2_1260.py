# 1260번_DFS와 BFS

## 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성
## 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문
## 더 이상 방문할 수 있는 점이 없는 경우 종료
## 정점 번호는 1번부터 N번까지

'''
# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V
# 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호
# 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있음
# 입력으로 주어지는 간선은 양방향
## 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력
## V부터 방문된 점을 순서대로 출력


(입력)
4 5 1
1 2
1 3
1 4
2 4
3 4

(출력) 
1 2 4 3
1 2 3 4

'''

from collections import deque
n, m, v = map(int, input().split())
arr = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    
    arr[a].append(b)
    arr[b].append(a)
    
visited = [False for i in range(n+1)]

def dfs(cur):
    visited[cur] = True
    
    for nxt in arr[cur]:
        if visited[nxt]:
            continue
        
        dfs(cur)
        
        
def bfs(v):
    que = deque()
    li = [False for i in range(n+1)]
    
    que.append(v)
    li[v] = True
    while len(que) > 0:
        
    