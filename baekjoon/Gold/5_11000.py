import sys
import heapq
input = lambda : sys.stdin.readline().strip()

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)] # 강의실 배정 받을 배열

pq = [] # 강의실 배정 받은 배열
heapq.heapify(arr) # heapq로 만들어줌

mx = 0 # 최대 강의실 개수
while arr:
    s, e = heapq.heappop(arr) # 제일 빨리 시작하는 시간, 끝나는 시간
    
    if pq: # pq에 값이 있을 때
        while pq and s >= pq[0]: # pq에 값이 있고, 시작 시간이 노드 값(최소값)보다 작을 때
            heapq.heappop(pq)   # 즉, pq에 있던 끝나는 시간이 시작 시간보다 빠를 때
                                # pq에는 강의실 배정 받은 애들만 있으므로 끝난 애들 다 비우기

    heapq.heappush(pq, e) # 끝나는 시간 새로 넣어주기
    mx = max(mx, len(pq)) # pq의 최대 값이 최대 강의실 갯수가 됨

          
print(mx)

"""
5
4 6
1 3
5 8
2 4
3 5

"""