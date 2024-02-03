# import sys

# input = lambda: sys.sys.stdin.readline().strip()

# n, m = map(int, input().split())
# arr = [[0 for _ in range(m + 2)]] + [[0] + list(map(int, input())) + [0] for _ in range(n)] + [[0 for _ in range(m + 2)]]

# prefix = [[0 for _ in range(m + 2)] for _ in range(n + 2)]
# suffix = [[0 for _ in range(m + 2)] for _ in range(n + 2)]
# mx = 0
# for i in range(1, n + 1):
#     for j in range(1, m + 1):
#         prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + (arr[i][j] == 0)
#         suffix[i][j] = suffix[i - 1][j] + suffix[i][j - 1] - suffix[i - 1][j - 1] + (arr[i][j] == 1)
        
#         if arr[i][j] == 1:
#             continue
        
#         for x in range(i):
#             for y in range(j):
#                 if suffix[i][j] or suffix[x][y]:
#                     continue
                
#                 mx = max(prefix[i][j] - prefix[x][j] - prefix[i][y] + prefix[x][y], mx)
# print(mx)


# import sys

# input = lambda: sys.sys.stdin.readline().strip()

# n, m = map(int, input().split())
# arr = [[0] + list(map(int, input())) for _ in range(n)]
# print(arr)
# dp = [[0] * (m + 1) for _ in range(n + 1)]

# mx = 0
# for i in range(1, n + 1):
#     for j in range(1, m + 1):
#         if arr[i-1][j-1] == 0:
#             dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
#             mx = max(mx, dp[i][j])
# print(dp)
# print(mx * mx)


# import sys

# n, m = map(int, sys.stdin.readline().split())
# arr = []
# for _ in range(n):
#     row = list(map(int, sys.stdin.readline().rstrip()))
#     arr.append(row)

# # 높이 배열 구하기
# heights = [[0]*m for _ in range(n)]
# for j in range(m):
#     cnt = 0
#     for i in range(n):
#         if arr[i][j] == 0:
#             cnt += 1
#             heights[i][j] = cnt
#         else:
#             cnt = 0
#             heights[i][j] = 0

# # 정답 계산
# ans = 0
# for i in range(n):
#     # 이전 높이와 현재 높이를 구분하기 위한 변수
#     cur_height = 0

#     # 사각형 크기를 가지고 있기 위한 변수
#     square = 0

#     for j in range(m):
#         # 만약에 높이가 0이면 볼 필요가 없다
#         if heights[i][j] == 0:
#             ans = max(ans, square)
#             square = 0
#             cur_height = 0
#             continue

#         # 높이가 이전과 다르다면 지금까지 계산했던 것으로 정답을 업데이트
#         if heights[i][j] != cur_height:
#             cur_height = heights[i][j]
#             ans = max(ans, square)
#             square = heights[i][j]
#         else:  # 높이가 이전과 같다면 사각형 사이즈를 증가
#             square += heights[i][j]

#     # 한줄이 끝나면 사각형 크기 업데이트
#     ans = max(ans, square)
# print(heights)
# print(ans)


import sys

n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]

# 높이 배열 구하기
heights = [[0] * m for _ in range(n)]
for j in range(m):
    cnt = 0
    for i in range(n):
        cnt = cnt + 1 if arr[i][j] == 0 else 0
        heights[i][j] = cnt

# 정답 계산
ans = 0
for i in range(m):
    for j in range(m):
        s = 0
        total = 0
        for k in range(n):
            tmp = heights[k][j] - heights[k][s]
            
            if tmp == total:
                ans = max(ans, (j - s + 1) * (k - s + 1))

            if tmp > total:
                s = k + 1

            total = tmp
            
        
print(ans)

