# 1697번_숨바꼭질

## 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있음
## 수빈이는 걷거나 순간이동을 할 수 있다.
## 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동
## 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동
## 수빈이와 동생의 위치가 주어졌을 때,
## 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램

'''
# 첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K(둘 다 정수)
# 수빈이가 동생을 찾는 가장 빠른 시간을 출력

(입력)
5 17

(출력)
4

'''


from collections import deque

n, k  = map(int, input().split())

def bfs(s):
    que = deque()
    visited = [False for _ in range(200010)]
    
    que.append(s)
    visited[s] = True
    
    d = 0
    while len(que) > 0:
        size = len(que)
        
        for _ in range(size):
            cur = que[0]
            que.popleft()
            
            if cur == k:
                print(d)
                break
            
            for nxt in [cur-1, cur+1, 2 * cur]:
                if not (0 <= nxt < 200010) or visited[nxt]:
                    continue
                
                que.append(nxt)
                visited[nxt] = True
        
        d += 1
        
bfs(n)