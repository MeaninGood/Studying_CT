# 3109번_빵집

## 학생이 N명인 학교에서 모든 학생과 친구가 되려 함.
## 학생 i에게 Ai만큼의 돈을 주면 그 학생은 1달간 친구
## 친구의 친구는 친구다
## 가장 적은 비용으로 모든 사람과 친구가 되는 방법 구하기

'''
# 첫 줄에 학생 수 N (1 ≤ N ≤ 10,000)과 친구관계 수 M (0 ≤ M ≤ 10,000), 가지고 있는 돈 k (1 ≤ k ≤ 10,000,000)
# 두번째 줄에 N개의 각각의 학생이 원하는 친구비 Ai(1 ≤ Ai ≤ 10,000, 1 ≤ i ≤ N)
# 다음 M개의 줄에는 숫자 v, w
# 학생 v와 학생 w가 서로 친구라는 뜻
## 친구로 만드는데 드는 최소비용을 출력
## 만약 친구를 다 사귈 수 없다면, “Oh no”(따옴표 제거)를 출력

(입력)
5 3 20
10 10 20 20 30
1 3
2 4
5 4

(출력)
20

'''

import sys


def dfs(cur):
    ret = arr[cur]
    visited[cur] = True
    
    for nxt in v[cur]:
        if visited[nxt]:
            continue
        
        ret = min(ret, dfs(nxt))
        
    return ret
    

n, m, k = map(int, sys.stdin.readline().split())
arr = [0] + list(map(int, sys.stdin.readline().split()))
v = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    v[a].append(b)
    v[b].append(a)
    
visited = [False for i in range(n+1)]

total = 0
for i in range(n+1):
    if not visited[i]:
        total += dfs(i)

if total <= k:
    print(total)
else :        
    print("Oh no")
    

'''

5 3 20
30 40 20 20 30
1 3
2 4
5 4

'''