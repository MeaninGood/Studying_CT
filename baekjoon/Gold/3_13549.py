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



# import heapq
#
# n, m = map(int, input().split())
# s = int(input())
# v = [[] for i in range(n + 1)]
#
# for i in range(m):
#     a, b, c = map(int, input().split())
#
#     v[a].append([b, c])
#
# dist = [1000000000 for i in range(n + 1)]
#
# pq = []
#
# dist[s] = 0
# heapq.heappush(pq, (0, s))
# while len(pq) > 0:
#     # mn = 100000000
#     # cur = 0
#     # for i in range(1, n + 1):
#     #     if not visited[i] and dist[i] < mn:
#     #         mn = dist[i]
#     #         cur = i
#     d, cur = heapq.heappop(pq)
#
#     # if visited[cur]:
#     #     continue
#     #
#     # visited[cur] = True
#
#     if dist[cur] != d:
#         continue
#
#     for i in range(len(v[cur])):
#         nxt = v[cur][i][0]
#         nd = dist[cur] + v[cur][i][1]
#
#         if dist[nxt] > nd:
#             dist[nxt] = nd
#             heapq.heappush(pq, (nd, nxt))
#
#
# for i in range(1, n + 1):
#     if dist[i] == 1000000000:
#         print('INF')
#     else:
#         print(dist[i])