# 1389번_케빈 베이컨의 6단계 법칙

## 모든 사람은 최대 6단계 이내에 서로 아는 사람으로 연결됨
## 유저의 수와 친구 관계가 입력으로 주어졌을 때, 케빈 베이컨의 수가 가장 작은 사람을 구하는 프로그램

'''
# 첫째 줄에 유저의 수 N (2 ≤ N ≤ 100)과 친구 관계의 수 M (1 ≤ M ≤ 5,000)
# 둘째 줄부터 M개의 줄에는 친구 관계가 주어짐
# 친구 관계는 A와 B로 이루어져 있으며, A와 B가 친구라는 뜻이다. A와 B가 친구이면, B와 A도 친구
# 친구 관계는 중복되어 들어올 수도 있으며, 친구가 한 명도 없는 사람은 없다
# 모든 사람은 친구 관계로 연결되어져 있음
## 첫째 줄에 BOJ의 유저 중에서 케빈 베이컨의 수가 가장 작은 사람을 출력
## 그런 사람이 여러 명일 경우에는 번호가 가장 작은 사람을 출력

(입력)
5 5
1 3
1 4
4 5
4 3
3 2

(출력)
3

'''

from collections import deque

def bfs(s):
    que = deque()
    visited = [False for i in range(n + 1)]
    
    que.append(s)
    visited[s] = True
    
    ret = 0
    
    while len(que) > 0:
        size = len(que)
        
        for _ in range(size):
            cur = que.popleft()
            
            if cur == i:
                return ret
            
            for nxt in v[cur]:
                if visited[nxt]:
                    continue
                
                que.append(nxt)
                visited[nxt] = True
                
        ret += 1
    return ret
        


n, m = map(int, input().split())

v = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    
    v[a].append(b)
    v[b].append(a)


ans = [[] for _ in range(n + 1)]
visited = [False for i in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        ans[i].append(bfs(j))
    
mn = 10000000
idx = 0
for i in range(1, n + 1):
    if sum(ans[i]) < mn:
        mn = min(mn, sum(ans[i]))
        idx = i

print(idx)