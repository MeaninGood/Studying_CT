# 퇴사, 퇴사 2

# n = int(input())
# arr = [list(map(int, input().split())) for i in range(n)]
# dp = [-1 for i in range(1500010)]
#
# ans = 0
#
# def recur(cur, total):
#     global ans
#
#     if cur > n:
#         return
#
#     if cur == n:
#         ans = max(ans, total)
#         return
#
#     recur(cur + arr[cur][0], total + arr[cur][1])
#     recur(cur + 1, total)
#
# def recur(cur):
#     if cur > n:
#         return -1000000000
#
#     if cur == n:
#         return 0
#
#     return max(recur(cur + arr[cur][0]) + arr[cur][1], recur(cur + 1))
#
# def recur(cur):
#     if cur > n:
#         return -1000000000
#
#     if cur == n:
#         return 0
#
#     if dp[cur] != -1:
#         return dp[cur]
#
#     dp[cur] = max(recur(cur + arr[cur][0]) + arr[cur][1], recur(cur + 1))
#
#     return dp[cur]
#
#
# print(recur(0))






# 1, 2, 3 더하기

# def recur(total):
#     global cnt
#
#     if total > n:
#         return
#
#     if total == n:
#         cnt += 1
#         return
#
#     for i in range(1, 4):
#         recur(total + i)


# dp = [-1 for i in range(1000010)]
#
# def recur(total):
#     ret = 0
#
#     if total < 0:
#         return 0
#
#     if total == 0:
#         return 1
#
#     if dp[total] != -1:
#         return dp[total]
#
#     for i in range(1, 4):
#         ret += recur(total - i)
#
#     dp[total] = ret
#
#     return dp[total]
#
#
# t = int(input())
#
# for _ in range(t):
#     n = int(input())
#
#     print(recur(n))






# 제곱수의 합


# n = int(input())

# ans = 10000
# def recur(cur, total):
#     global ans
#
#     if total == n:
#         ans = min(ans, cur)
#         return
#
#     for i in range(1, n + 1):
#         if i * i > n - total:
#             break
#
#         recur(cur + 1, total + i * i)


# dp = [-1 for i in range(100010)]
#
# def recur(total):
#     if total == n:
#         return 0
#
#     if dp[total] != -1:
#         return dp[total]
#
#     ret = 100000
#     for i in range(1, n + 1):
#         if i * i > n - total:
#             break
#
#         ret = min(ret, recur(total + i * i) + 1)
#
#     dp[total] = ret
#
#     return dp[total]
#
#
# print(recur(0))




# 1, 2, 3 더하기 바텀업 코드

# dp = [0 for i in range(1000010)]

# dp[1] = 1
# dp[2] = 2
# dp[3] = 4
# for i in range(4, 1000010):
#     dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % 1000000009

# t = int(input())
# for _ in range(t):
#     n = int(input())

#     print(dp[n])


# n = int(input())
#
# dp = [100000 for i in range(n + 1)]
#
# dp[0] = 0
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if j * j > i:
#             break
#
#         dp[i] = min(dp[i], dp[i - j * j] + 1)
#
# print(dp[n])



# n = int(input())
# dp = [0 for i in range(1100)]
#
# dp[1] = 1
# dp[2] = 3
# for i in range(3, n + 1):
#     dp[i] = (dp[i - 1] + 2 * dp[i - 2]) % 10007
#
# print(dp[n])




# n = int(input())
#
# dp = [False for i in range(1010)]

# dp[1] = True
# dp[2] = False
# dp[3] = True
# dp[4] = True

# for i in range(5, n + 1):
#     if not (dp[i - 1] and dp[i - 3] and dp[i - 4]):
#         dp[i] = True
#     else:
#         dp[i] = False

# if dp[n]:
#     print('SK')
# else:
#     print('CY')



# 경우의 수를 구해라? => 무조건 DP
# 최대값을 구해라 => 이진탐색 or DP
# 누가 이기냐 => 무조건 DP


# n = int(input())
# arr = list(map(int, input().split()))
#
# ans = 0
#
# ans = arr[0]
# mx = arr[0]
# for i in range(1, n):
#     mx = max(mx + arr[i], arr[i])
#
#     ans = max(ans, mx)
#
# print(ans)




# n = int(input())
# arr = [int(input()) for i in range(n)] + [0 for i in range(10)]
# dp = [[-1 for i in range(3)] for j in range(310)]
#
# def recur(cur, cnt):
#     if cur > n - 1:
#         return -1000000000
#     if cnt == 3:
#         return -1000000000
#
#     if cur == n - 1:
#         return 0
#
#     if dp[cur][cnt] != -1:
#         return dp[cur][cnt]
#
#     dp[cur][cnt] = max(recur(cur + 1, cnt + 1) + arr[cur + 1], recur(cur + 2, 1) + arr[cur + 2])
#
#     return dp[cur][cnt]
#
# print(recur(-1, 0))




# n = int(input())
# arr = list(map(int, input().split())) + [-1]
#
# dp = [[-1 for i in range(1010)] for j in range(1010)]
#
# def recur(cur, prv):
#     if cur == n:
#         return 0
#
#     if dp[cur][prv] != -1:
#         return dp[cur][prv]
#
#     if arr[cur] > arr[prv]:
#         ret = max(recur(cur + 1, cur) + 1, recur(cur + 1, prv))
#     else:
#         ret = recur(cur + 1, prv)
#
#     dp[cur][prv] = ret
#
#     return dp[cur][prv]
#
# print(recur(0, n))
#
#
#
#
#
# n = int(input())
# arr = list(map(int, input().split()))
# dp = [1 for i in range(n)]
#
# for i in range(n):
#     for j in range(i):
#         if arr[i] > arr[j]:
#             dp[i] = max(dp[i], dp[j] + 1)
#
# print(max(dp))




