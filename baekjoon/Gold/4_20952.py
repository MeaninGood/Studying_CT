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


import sys
input = lambda : sys.stdin.readline().strip()


n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
prefix = list(map(int, input().split()))
arr = [0 for _ in range(7)]

for i in arr1:
    arr[i % 7] += 1

for i in range(m):
    idx = arr[(7 - prefix[i]) % 7]
    arr[(7 - prefix[i]) % 7] = 0
    tmp = arr[:]

    cnt = 0
    for j in range(7):
        if arr[j] == 0:
            cnt += 1
            
    if cnt == 7:
        arr[(7 - prefix[i]) % 7] = idx
        continue
        
    for j in range(7):
        arr[(j + prefix[i]) % 7] = tmp[j]

k = 0
for i in arr:
    if i != 0:
        k += i

if k == 0:
    print(n)
    print(*arr1)
    
else:
    print(k)
    for i in range(n):
        print(arr1)
        if arr[i % 7] != 0:
            print(arr1[i] + sum(prefix), end = ' ')
            arr[i % 7] -= 1
