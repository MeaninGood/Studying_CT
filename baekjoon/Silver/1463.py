import sys
sys.setrecursionlimit(1000000)
n = int(sys.stdin.readline())

dp = [-1 for i in range(20)]

def recur(cur):
    if cur < 1:
        return
    
    if cur == 1:
        return 0
    
    if dp[cur] != -1 :
        return dp[cur]

    if cur % 6 == 0:
        dp[cur] = min(recur(cur // 3) + 1, recur(cur // 2) + 1, recur(cur - 1) + 1)

    elif cur % 3 == 0:
        dp[cur] = min(recur(cur // 3) + 1, recur(cur - 1) + 1)
    
    elif cur % 2 == 0:
        dp[cur] = min(recur(cur // 2) + 1, recur(cur - 1) + 1)
    
    else:
        dp[cur] = recur(cur - 1) + 1

    return dp[cur]

print(recur(n))
# print(dp)


# import sys
# # sys.setrecursionlimit(1000000)
# n = int(sys.stdin.readline())

# dp = [-1 for i in range(20)]

# dp[1] = 1
# dp[2] = 1
# dp[3] = 1
# for i in range(4, n + 1):
#     if i % 3 == 0:
#         dp[i] = min(dp[i - 1] + 1, dp[i - 3] + 1)
#     elif i % 2 == 0:
#         dp[i] = min(dp[i - 1] + 1, dp[i - 2] + 1)
#     else:
#         dp[i] = dp[i - 1]
# print(dp[n])
# print(dp)


n = int(input())
dp = [0, 0, 1, 1]
for i in range(4, n+1):
    if i % 6 == 0:
        dp.append(min(dp[i//3]+1, dp[i//2]+1, dp[i-1]+1))
    elif i % 3 == 0:
        dp.append(min(dp[i//3]+1, dp[i-1]+1))
    elif i % 2 == 0:
        dp.append(min(dp[i//2]+1, dp[i-1]+1))
    else:
        dp.append(dp[i-1]+1)

print(dp[n])