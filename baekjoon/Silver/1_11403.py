# 11403번_경로 찾기

## 가중치 없는 방향 그래프 G가 주어졌을 때,
## 모든 정점 (i, j)에 대해서, i에서 j로 가는 경로가 있는지 없는지 구하는 프로그램을 작성

'''
# 첫째 줄에 정점의 개수 N (1 ≤ N ≤ 100)
# 둘째 줄부터 N개 줄에는 그래프의 인접 행렬이 주어짐
# i번째 줄의 j번째 숫자가 1인 경우에는 i에서 j로 가는 간선이 존재한다는 뜻
# 0인 경우는 없다는 뜻
# i번째 줄의 i번째 숫자는 항상 0
## 총 N개의 줄에 걸쳐서 문제의 정답을 인접행렬 형식으로 출력
## 정점 i에서 j로 가는 경로가 있으면 i번째 줄의 j번째 숫자를 1로, 없으면 0으로 출력

(입력)
3
0 1 0
0 0 1
1 0 0

(출력)
1 1 1
1 1 1
1 1 1

'''

from re import L
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

v = [[] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            v[i].append(j)
            v[j].append(i)

print(v)


def bfs(s):
    que = deque()

    
    que.append(s)
    visited[s] = True
    
    while len(que) > 0:
        size = len(que)
        
        for _ in range(size):
            cur = que.popleft()
            
            for nxt in v[cur]:
                if visited[nxt]:
                    continue
                
                que.append(nxt)
                visited[nxt] = True


visited = [False for _ in range(n)]
for i in range(n):
    if v[i] and not visited[i]:
        bfs(i)

print(visited)