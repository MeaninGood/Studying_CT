import sys
import heapq
input = lambda : sys.stdin.readline().strip()

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]
heapq.heapify(arr) # 처음에는 보석을 무게 순으로 최소힙에 넣음(무게 낮은 것 우선)
heapq.heapify(bags) # 가방도 최소힙에 넣음


pq = []
total = 0
while bags: # 가방에 보석을 넣을 수 있을 때까지만 실행
    
    tmp = heapq.heappop(bags) # 가방
    while arr and arr[0][0] <= tmp: # 훔칠 보석이 있고, 무게가 작거나 같을 때
        w, v = heapq.heappop(arr) # 꺼내서
        heapq.heappush(pq, -v) # 가치 기준으로 최대힙에 넣음(가치 높은 것 우선)
    
    if pq: # 훔칠 수 있는 보석이 있을 때
        total += -heapq.heappop(pq) # 그들 중 가치가 가장 높은 것 더하기

print(total)