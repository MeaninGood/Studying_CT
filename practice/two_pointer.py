# CPU -> 1초에 1억번



# n = 10000
# for i in range(n):
#     pass # 총 10000번의 연산
#     for j in range(n):
#         pass # 10000번의 연산

# arr = [1, 2, 2, 3, 4, 6]

# s = 0
# e = 5
# cnt = 0
# while e > s:
#     if arr[s] + arr[e] > 6:
#         e -= 1
        
#     elif arr[s] + arr[e] < 6:
#         s += 1
        
#     else:
#         cnt += 1
#         s += 1

# print(cnt)


# n, m = map(int, input().split())
# arr = list(map(int, input().split())) + [0]

# s = 0
# e = 0
# total = arr[0]
# cnt = 0

# while e < n:
#     if total == m:
#         cnt += 1
#         e += 1
#         total += arr[e]
        
#     elif total < m:
#         e += 1
#         total += arr[e]
        
#     else:
#         total -= arr[s]
#         s += 1
        
# print(cnt)


n = int(input()) # x


import sys
input = lambda : sys.stdin.readline().strip()


n = int(input())
arr = list(map(int, input().split()))