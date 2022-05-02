# 1699번_제곱수의 합

## 어떤 자연수 N은 그보다 작거나 같은 제곱수들의 합으로 나타낼 수 있음
## 11을 그 합으로써 표현할 수 있는 제곱수 항의 최소 개수는 3
## 주어진 자연수 N을 이렇게 제곱수들의 합으로 표현할 때에 그 항의 최소개수 구하기

'''
# 첫째 줄에 자연수 N이 주어진다. (1 ≤ N ≤ 100,000)
# 주어진 자연수를 제곱수의 합으로 나타낼 때에 그 제곱수 항의 최소 개수를 출력

(입력)
7

(출력)
4

'''
# import sys
# sys.setrecursionlimit(100000)

# n = int(sys.stdin.readline())

# dp = [-1 for i in range(100010)]

# def recur(total):
#     if total == n:
#         return 0
    
#     if dp[total] != -1:
#         return dp[total]
    
#     ret = 100000
#     for i in range(1, n + 1):
#         if i * i > n - total:
#             break
        
#         ret = min(ret, recur(total + i * i) + 1)
    
#     dp[total] = ret
    
#     return dp[total]

# print(recur(0))








# n = int(input())
# dp = [0 for _ in range(n + 1)]

# dp[0] = 0
# dp[1] = 1

# for i in range(2, n + 1):
#     a = int(i**0.5)
#     b = i-a**2
#     min_num = n
#     while a**2 >= b:
#         tmp = 1 + dp[b]
#         if tmp < min_num:
#             min_num = tmp
#         a = a - 1
#         b = i-a**2
#     dp[i] = min_num
# print(dp[n])


import sys
input = sys.stdin.readline

n = int(input())
dp = [i for i in range(n + 1)]

dp[0] = 0
dp[1] = 1

for i in range(2, n + 1):
    for j in range(1, i):
        if j * j > i:
            break
        
        tmp = 1 + dp[i - (j * j)]
        if dp[i] > tmp:
            dp[i] = tmp
print(dp[n])