import sys
import heapq
input = lambda : sys.stdin.readline().strip()

n = int(input())
pq = []
for i in range(n):
    a, b = map(int, input().split())
    heapq.heappush(pq, (-b, a))

d = {}
while pq:
    score, day = heapq.heappop(pq)
    for i in range(1, day + 1)[::-1]:
        if d.get(i):
            continue
        
        d[i] = d.get(i, -score)
        break
    
print(d)
print(sum(d.values()))
    
    
"""
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort(key = lambda x: -x[1])

# print(arr)
# idx = 0
# total = 0
# cnt = 0
# while arr:
#     if arr[0][0] > idx and cnt <= idx:
#         idx = arr[0][0]
#         total += arr[0][1]
#         cnt += 1
        
#     elif arr[0][0] <= idx and cnt < idx:
#         total += arr[0][1]
#         cnt += 1

#     arr.pop(0)
    
# print(total)
"""