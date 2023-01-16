# # 게임 개발자 승희

# import sys
# input = lambda : sys.stdin.readline().strip()


# n, m = map(int, input().split())
# arr1 = list(map(int, input().split()))
# arr2 = [0] + list(map(int, input().split()))

# arr = [0 for i in range(7)]
# prefix = [0 for i in range(m + 1)]

# for i in arr1:
#     arr[i % 7] += 1

# for i in range(1, m + 1):
#     prefix[i] = prefix[i - 1] + arr2[i]

# print(arr)
# tmp = 0
# for i in range(1, m + 1):
#     idx = arr[prefix[i] % 7]
#     arr[prefix[i] % 7] = 0
    
#     cnt = 0
#     for j in range(7):
#         if arr[j] == 0:
#             cnt += 1
    
#     if cnt == 7:
#         arr[prefix[i] % 7] = idx
#         tmp += 1
#         continue
    
#     for j in range(1):
#         if arr[j] != 0:
#             arr[(j + prefix[i]) % 7] = arr[j]
#             arr[j] = 0
            
# print(arr)
# print(prefix)

# k = 0
# for i in arr:
#     if i != 0:
#         k += i

# print(arr)
# print(prefix)


# if tmp == m:
#     print(*arr1)
#     exit()

# print(arr)

# for i in range(n):
#     if arr[i % 7] != 0:
#         print((arr1[i] + prefix[-1]) % (10**9 + 7), end = ' ')
        

# # for i in range(n):
# #     for j in range(1, 8):
# #         if arr[j] != 0:
# #             idx = 0
# #             while idx < arr[j]:
# #                 print(arr1[i])
# #                 idx += 1


# import sys
# input = lambda : sys.stdin.readline().strip()


# n, m = map(int, input().split())
# arr1 = list(map(int, input().split()))
# prefix = list(map(int, input().split()))
# arr = [0 for _ in range(7)]

# for i in arr1:
#     arr[i % 7] += 1

# for i in range(m):
#     idx = arr[(7 - prefix[i]) % 7]
#     arr[(7 - prefix[i]) % 7] = 0
#     tmp = arr[:]

#     cnt = 0
#     for j in range(7):
#         if arr[j] == 0:
#             cnt += 1
            
#     if cnt == 7:
#         arr[(7 - prefix[i]) % 7] = idx
#         continue
        
#     for j in range(7):
#         arr[(j + prefix[i]) % 7] = tmp[j]

# k = 0
# for i in arr:
#     if i != 0:
#         k += i

# if k == 0:
#     print(n)
#     print(*arr1)
    
# else:
#     print(k)
#     for i in range(n):
#         # print(arr1)
#         if arr[i % 7] != 0:
#             print(arr1[i] + sum(prefix) % (10**9 + 7), end = ' ')
#             arr[i % 7] -= 1


# import sys
# input = lambda : sys.stdin.readline().strip()

"""
n, m 제한 = 10만 (최대 n * n)
완탐 다 돌면 10!이 나옴, 완탐 x
"""

# n, m = map(int, input().split())
# arr = list(map(int, input().split()))
# arr2 = list(map(int, input().split()))
# idx = [0 for _ in range(7)]
# mx = 0
# for i in arr:
#     idx[i % 7] += 1
#     if idx[i % 7] > mx:
#         mx = idx[i % 7]

# zero = 0
# for i in range(7):
#     if idx[i] == 0:
#         zero += 1

# if zero == 6:
#     answer = []
#     for i in range(n):
#         answer.append(arr[i] % (10**9 + 7))

#     print(m)
#     print(*answer)

#     exit()

# for i in range(m):
#     tmp = idx[(7 - (arr2[i] % 7)) % 7]
#     tmp2 = idx[:]

#     idx = idx[(7 - (arr2[i] % 7)) % 7:] + idx[:((7 - (arr2[i] % 7)) % 7)]
#     idx[(7 - (arr2[i] % 7)) % 7] = 0
#     zero += 1

#     if zero == 6:
#         zero -= 1
#         idx[(7 - (arr2[i] % 7)) % 7] = tmp
#         idx = tmp2


# print(idx)

# cnt = 0
# total = sum(arr2)
# answer = []
# for i in range(n* mx):
#     print(i // 7, ((i // 7) * 7) + (i % 7))
#     if idx[i % 7] != 0 and ((i // 7) * 7) + (i % 7) <= n:
#         idx[i % 7] -= 1
#         answer.append((arr[((i // 7) * 7) + (i % 7)] + total) % (10**9 + 7))
#         cnt += 1

#     print(idx)

# print(cnt)
# print(*answer)


import sys
input = lambda : sys.stdin.readline().strip()

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
idx = [0 for _ in range(7)]

for i in arr:
    idx[i % 7] += 1

zero = 0
for i in idx:
    if i == 0:
        zero += 1

answer = []

prefix = [0 for i in range(m)]
prefix[0] = arr2[0] % (10**9 + 7)
for i in range(1, m):
    prefix[i] = prefix[i - 1] + arr2[i]

for i in range(m):
    if idx[(7 - ((prefix[i] % 7))) % 7] != 0:
        tmp = idx[(7 - ((prefix[i] % 7))) % 7] # 값 저장
        idx[(7 - ((prefix[i] % 7))) % 7] = 0 # 바꾸기
        zero += 1 # 0 개수 += 1

        if zero == 6:
            idx[(7 - ((prefix[i] % 7))) % 7] = tmp # 값 돌리기
            break


for i in range(7):
    if idx[i] != 0:
        for j in range(n):
            if arr[j] % 7 == i:
                answer.append((arr[j] + (prefix[-1] % (10**9 + 7))) % (10**9 + 7))

if answer == []:
    print(m)
    print(*arr)
    exit()

answer.sort()
print(sum(idx))
print(*answer)