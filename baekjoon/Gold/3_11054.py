# 11054번_가장 긴 바이토닉 부분 수열

## 수열 S가 어떤 수 Sk를 기준으로 S1 < S2 < ... Sk-1 < Sk > Sk+1 > ... SN-1 > SN을 만족한다면,
## 수열 A가 주어졌을 때
## 그 수열의 부분 수열 중 바이토닉 수열이면서 가장 긴 수열의 길이를 구하는 프로그램 작성

'''
# 첫째 줄에 수열 A의 크기 N
# 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어짐(1 ≤ N ≤ 1,000, 1 ≤ Ai ≤ 1,000)
## 첫째 줄에 수열 A의 부분 수열 중에서 가장 긴 바이토닉 수열의 길이를 출력

(입력)
10
1 5 2 1 4 3 4 5 2 1

(출력)
7

'''

# import sys
# si = sys.stdin.readline
# sys.setrecursionlimit(10000)

# def recur(cur):
    
#     ret = 1
#     print(ret)
#     if cur >= n - 1:
#         return ret
#     # if arr[cur] < arr[cur + 1]:
#     #     r1 = max(recur(cur) + 1, recur(cur + 1))
    
#     # if arr[cur] > arr[cur + 1]:
#     #     r2 = max(recur(cur) + 1, recur(cur + 1))
    
#     # if arr[cur - 1] < arr[cur] < arr[cur + 1]:
#     #     r3 = max(recur(cur) + 1, recur(cur + 1))
        
#     # ret = max(r1, r2, r3)
    
#     if arr[cur] < arr[cur + 1]:
#         ret = max(ret, recur(cur + 1) + 1)
#     else:
#         recur(cur + 1)
    
#     # if arr[cur] > arr[cur + 1]:
#     #     r2 = max(ret, recur(cur + 1) + 1)
#     #     ret = max(ret, r2)
    
#     # if arr[cur - 1] < arr[cur] < arr[cur + 1]:
#     #     r3 = max(ret, recur(cur + 1) + 1)
#     #     ret = max(ret, r3)
    
#     return ret


# n = int(si())
# arr = list(map(int, si().split()))
# print(recur(0))






####### arr[cur] < arr[cur + 1]


# import sys
# si = sys.stdin.readline
# sys.setrecursionlimit(10000)

# def recur(cur):
    
#     ret = 0
#     print(ret)
#     if cur >= n - 1:
#         return -100000000
    
#     if arr[cur] < arr[cur + 1]:
#         ret = max(ret, recur(cur + 1) + 1)
#     else:
#         ret = recur(cur + 1)
    
#     return ret


# n = int(si())
# arr = list(map(int, si().split()))
# print(recur(0))



#### arr[cur] > arr[cur + 1] 

# import sys
# si = sys.stdin.readline
# sys.setrecursionlimit(10000)

# def recur(cur):
    
#     ret = 0
#     print(ret)
#     if cur >= n - 1:
#         return -100000000
    
#     if arr[cur] > arr[cur + 1]:
#         ret = max(ret, recur(cur + 1) + 1)
#     else:
#         ret = recur(cur + 1)
    
#     return ret


# n = int(si())
# arr = list(map(int, si().split()))
# print(recur(0))


# import sys
# si = sys.stdin.readline
# sys.setrecursionlimit(10000)

# def recur(cur):
#     if cur > n - 1:
#         return -100000000
    
#     ret = 1
#     print(ret)
    
#     if arr[cur - 1] < arr[cur]:
#         ret = max(ret, recur(cur + 1) + 1)
#     else:
#         recur(cur + 1)
    
#     return ret


# n = int(si())
# arr = list(map(int, si().split()))
# print(recur(1))




# import sys
# si = sys.stdin.readline
# sys.setrecursionlimit(10000)

# def recur(cur):
#     if cur >= n - 1:
#         return -10000000
    
#     ret = 1
#     for i in range(cur):
#         if arr[cur - 1] < arr[cur]:
#             ret = max(ret, recur(cur + 1) + 1)
            
#     return ret
        
    

# n = int(si())
# arr = list(map(int, si().split()))

# mx = -10000000
# for i in range(1, n):
#     mx = max(mx, recur(i))
    
# print(mx)



import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [1 for _ in range(1010)]
dp2 = [1 for _ in range(1010)]

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

arr2 = arr[::-1]
for i in range(n):
    for j in range(i):
        if arr2[i] > arr2[j]:
            dp2[i] = max(dp2[i], dp2[j] + 1)

ans = 0
dp3 = dp2[:n][::-1]
for i in range(n):
    ans = max(ans, dp[i] + dp3[i])
    
print(ans - 1)