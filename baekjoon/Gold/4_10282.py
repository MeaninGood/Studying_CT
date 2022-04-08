# 10282번_해킹

## 네트워크 시설의 한 컴퓨터를 해킹
## 이제 서로에 의존하는 컴퓨터들은 점차 하나둘 전염되기 시작
## 어떤 컴퓨터 a가 다른 컴퓨터 b에 의존한다면, b가 감염되면 그로부터 일정 시간 뒤 a도 감염
## 이때 b가 a를 의존하지 않는다면, a가 감염되더라도 b는 안전
## 해킹한 컴퓨터 번호와 각 의존성이 주어질 때,
## 해킹당한 컴퓨터까지 포함하여 총 몇 대의 컴퓨터가 감염되며 그에 걸리는 시간이 얼마인지 구하는 프로그램

'''
# 첫째 줄에 테스트 케이스의 개수
# 테스트 케이스의 개수는 최대 100개
# 첫째 줄에 컴퓨터 개수 n, 의존성 개수 d, 해킹당한 컴퓨터의 번호 c(1 ≤ n ≤ 10,000, 1 ≤ d ≤ 100,000, 1 ≤ c ≤ n)
# 이어서 d개의 줄에 각 의존성을 나타내는 정수 a, b, s(1 ≤ a, b ≤ n, a ≠ b, 0 ≤ s ≤ 1,000)
# 이는 컴퓨터 a가 컴퓨터 b를 의존하며, 컴퓨터 b가 감염되면 s초 후 컴퓨터 a도 감염됨을 뜻함
# 각 테스트 케이스에서 같은 의존성 (a, b)가 두 번 이상 존재하지 않음
## 각 테스트 케이스마다 한 줄에 걸쳐 총 감염되는 컴퓨터 수, 마지막 컴퓨터가 감염되기까지 걸리는 시간을 공백으로 구분지어 출력

(입력)
2
3 2 2
2 1 5
3 2 5
3 3 1
2 1 2
3 1 8
3 2 4

(출력)
2 5
3 6

'''

import sys
import heapq
si = sys.stdin.readline

def get_dist(s, v):
    pq = []
    
    dist[s] = 0
    heapq.heappush(pq, (0, s))
    
    ret = 0
    while len(pq) > 0:

        d, cur = heapq.heappop(pq)
        
        if dist[cur] != d:
            continue
        
        for i in range(len(v[cur])):
            nxt = v[cur][i][0]
            nd = d + v[cur][i][1]
            
            if dist[nxt] > nd:
                dist[nxt] = nd
                heapq.heappush(pq, (nd, nxt))
                
        ret += 1
        
    return ret
        
    

T = int(input())
for tc in range(T):
    n, d, s = map(int, si().split())
    
    v = [[] for i in range(n + 1)]
    
    for i in range(d):
        a, b, c = map(int, si().split())
        v[b].append([a, c])
        
    dist = [1000000000 for _ in range(n + 1)]
    
    print(get_dist(s, v), end = ' ')
    
    mx = -10000000
    for i in range(n + 1):
        if dist[i] == 1000000000:
            continue
        if mx < dist[i]:
            mx = dist[i]

    print(mx)