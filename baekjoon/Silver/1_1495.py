# import sys
# input = sys.stdin.readline


# def recur(cur):
#     ret = s
#     if not (0 <= ret < m):
#         return -10000000
    
#     if cur == n:
#         return ret
#     print(ret)
#     ret = max(recur(cur + 1) + arr[cur], recur(cur + 1) - arr[cur])
#     return ret

        

# n, s, m = map(int, input().split())
# arr = list(map(int, input().split()))

# print(recur(0))




# import sys
# input = sys.stdin.readline

# dp = [[-1 for i in range(1010)] for j in range(60)]
# def recur(cur, total):
#     global v

#     if not (0 <= total <= m):
#         return
    
#     if dp[cur][total] != -1:
#         return dp[cur][total]
#     elif cur == n:
#         return dp[cur][total]

#     dp[cur][total] = recur(cur + 1, total + arr[cur])
#     dp[cur][total] = recur(cur + 1, total - arr[cur])
    
#     return dp[cur][total]

# n, s, m = map(int, input().split())
# arr = list(map(int, input().split()))
# v = []
# recur(0, s)

# print(dp[n - 1][m])
# if v == []:
#     print(-1)
# else:
#     print(max(v))




# import sys
# input = sys.stdin.readline

# def recur(cur, total):
#     global ans
#     if not (0 <= total <= m):
#         return
    
#     elif cur == n:
#         ans = max(ans, total)
#         return

#     recur(cur + 1, total + arr[cur])
#     recur(cur + 1, total - arr[cur])
    
#     # return total

# n, s, m = map(int, input().split())
# arr = list(map(int, input().split()))
# # v = []
# ans = 0

# recur(0, s)

# if ans == 0:
#     print(-1)
# else:
#     print(ans)



import sys
input = sys.stdin.readline

def recur(cur, total):
    if not (0 <= total <= m):
        return -1000000
    
    if dp[cur][total] != -1:
        return dp[cur][total]
    
    if cur == n:
        return total

    dp[cur][total] = max(recur(cur + 1, total + arr[cur]) , recur(cur + 1,  total - arr[cur]))

    return dp[cur][total]

n, s, m = map(int, input().split())
arr = list(map(int, input().split()))
dp = [[-1 for i in range(m + 1)] for j in range(n + 1)]

ans = recur(0, s)
if ans == -1000000:
    print(-1)
else:
    print(ans)