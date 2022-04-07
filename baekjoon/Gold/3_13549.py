# 13549번_숨바꼭질 3

## 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있음
## 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동
## 순간이동을 하는 경우에는 0초 후에 2*X의 위치로 이동
## 수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하기


'''
# 첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어짐. N과 K는 정수
## 수빈이가 동생을 찾는 가장 빠른 시간을 출력

(입력)
5 17

(출력)
2

'''

import heapq

s, e = map(int, input().split())
# v = [[i, 0] for i in range(100010)]
dist = [1000000000 for i in range(100010)]

def in_range(x):
    return 0 <= x < 100010

pq = []
dist[s] = 0
heapq.heappush(pq, (0, s))
while len(pq) > 0:
    d, cur = heapq.heappop(pq)
    
    if cur == e:
        print(dist[cur])
        break
    
    if dist[cur] != d:
        continue
    
    for i in [cur - 1, cur + 1, cur * 2]:
        nxt = i
        nd = dist[cur] + 1
        
        if not in_range(nxt):
            continue
        
        if i == cur * 2:
            nxt = i
            nd = dist[cur]
        
        if dist[nxt] > nd:
            dist[nxt] = nd
            heapq.heappush(pq, (nd, nxt))
            