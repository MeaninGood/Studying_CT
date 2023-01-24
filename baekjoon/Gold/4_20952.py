# # # 게임 개발자 승희

# # import sys
# # input = lambda : sys.stdin.readline().strip()


# # n, m = map(int, input().split())
# # arr1 = list(map(int, input().split()))
# # arr2 = [0] + list(map(int, input().split()))

# # arr = [0 for i in range(7)]
# # prefix = [0 for i in range(m + 1)]

# # for i in arr1:
# #     arr[i % 7] += 1

# # for i in range(1, m + 1):
# #     prefix[i] = prefix[i - 1] + arr2[i]

# # print(arr)
# # tmp = 0
# # for i in range(1, m + 1):
# #     idx = arr[prefix[i] % 7]
# #     arr[prefix[i] % 7] = 0
    
# #     cnt = 0
# #     for j in range(7):
# #         if arr[j] == 0:
# #             cnt += 1
    
# #     if cnt == 7:
# #         arr[prefix[i] % 7] = idx
# #         tmp += 1
# #         continue
    
# #     for j in range(1):
# #         if arr[j] != 0:
# #             arr[(j + prefix[i]) % 7] = arr[j]
# #             arr[j] = 0
            
# # print(arr)
# # print(prefix)

# # k = 0
# # for i in arr:
# #     if i != 0:
# #         k += i

# # print(arr)
# # print(prefix)


# # if tmp == m:
# #     print(*arr1)
# #     exit()

# # print(arr)

# # for i in range(n):
# #     if arr[i % 7] != 0:
# #         print((arr1[i] + prefix[-1]) % (10**9 + 7), end = ' ')
        

# # # for i in range(n):
# # #     for j in range(1, 8):
# # #         if arr[j] != 0:
# # #             idx = 0
# # #             while idx < arr[j]:
# # #                 print(arr1[i])
# # #                 idx += 1


# # import sys
# # input = lambda : sys.stdin.readline().strip()


# # n, m = map(int, input().split())
# # arr1 = list(map(int, input().split()))
# # prefix = list(map(int, input().split()))
# # arr = [0 for _ in range(7)]

# # for i in arr1:
# #     arr[i % 7] += 1

# # for i in range(m):
# #     idx = arr[(7 - prefix[i]) % 7]
# #     arr[(7 - prefix[i]) % 7] = 0
# #     tmp = arr[:]

# #     cnt = 0
# #     for j in range(7):
# #         if arr[j] == 0:
# #             cnt += 1
            
# #     if cnt == 7:
# #         arr[(7 - prefix[i]) % 7] = idx
# #         continue
        
# #     for j in range(7):
# #         arr[(j + prefix[i]) % 7] = tmp[j]

# # k = 0
# # for i in arr:
# #     if i != 0:
# #         k += i

# # if k == 0:
# #     print(n)
# #     print(*arr1)
    
# # else:
# #     print(k)
# #     for i in range(n):
# #         # print(arr1)
# #         if arr[i % 7] != 0:
# #             print(arr1[i] + sum(prefix) % (10**9 + 7), end = ' ')
# #             arr[i % 7] -= 1


# # import sys
# # input = lambda : sys.stdin.readline().strip()

# """
# n, m 제한 = 10만 (최대 n * n)
# 완탐 다 돌면 10!이 나옴, 완탐 x
# """

# # n, m = map(int, input().split())
# # arr = list(map(int, input().split()))
# # arr2 = list(map(int, input().split()))
# # idx = [0 for _ in range(7)]
# # mx = 0
# # for i in arr:
# #     idx[i % 7] += 1
# #     if idx[i % 7] > mx:
# #         mx = idx[i % 7]

# # zero = 0
# # for i in range(7):
# #     if idx[i] == 0:
# #         zero += 1

# # if zero == 6:
# #     answer = []
# #     for i in range(n):
# #         answer.append(arr[i] % (10**9 + 7))

# #     print(m)
# #     print(*answer)

# #     exit()

# # for i in range(m):
# #     tmp = idx[(7 - (arr2[i] % 7)) % 7]
# #     tmp2 = idx[:]

# #     idx = idx[(7 - (arr2[i] % 7)) % 7:] + idx[:((7 - (arr2[i] % 7)) % 7)]
# #     idx[(7 - (arr2[i] % 7)) % 7] = 0
# #     zero += 1

# #     if zero == 6:
# #         zero -= 1
# #         idx[(7 - (arr2[i] % 7)) % 7] = tmp
# #         idx = tmp2


# # print(idx)

# # cnt = 0
# # total = sum(arr2)
# # answer = []
# # for i in range(n* mx):
# #     print(i // 7, ((i // 7) * 7) + (i % 7))
# #     if idx[i % 7] != 0 and ((i // 7) * 7) + (i % 7) <= n:
# #         idx[i % 7] -= 1
# #         answer.append((arr[((i // 7) * 7) + (i % 7)] + total) % (10**9 + 7))
# #         cnt += 1

# #     print(idx)

# # print(cnt)
# # print(*answer)


# # import sys
# # input = lambda : sys.stdin.readline().strip()

# # n, m = map(int, input().split())
# # arr = list(map(int, input().split()))
# # arr2 = list(map(int, input().split()))
# # idx = [0 for _ in range(7)]

# # for i in arr:
# #     idx[i % 7] += 1

# # zero = 0
# # for i in idx:
# #     if i == 0:
# #         zero += 1

# # answer = []

# # prefix = [0 for i in range(m)]
# # prefix[0] = arr2[0] % (10**9 + 7)
# # for i in range(1, m):
# #     prefix[i] = prefix[i - 1] + arr2[i]

# # for i in range(m):
# #     if idx[(7 - ((prefix[i] % 7))) % 7] != 0:
# #         tmp = idx[(7 - ((prefix[i] % 7))) % 7] # 값 저장
# #         idx[(7 - ((prefix[i] % 7))) % 7] = 0 # 바꾸기
# #         zero += 1 # 0 개수 += 1

# #         if zero == 6:
# #             idx[(7 - ((prefix[i] % 7))) % 7] = tmp # 값 돌리기
# #             break


# # for i in range(7):
# #     if idx[i] != 0:
# #         for j in range(n):
# #             if arr[j] % 7 == i:
# #                 answer.append((arr[j] + (prefix[-1] % (10**9 + 7))) % (10**9 + 7))

# # if answer == []:
# #     print(m)
# #     print(*arr)
# #     exit()

# # answer.sort()
# # print(sum(idx))
# # print(*answer)





# """
# 10만 * 7 = 70만

# 길이 n인 수열 a, 길이 m인 수열 b
# 수열 a에 대해 m번 연산 수행
# 1. i번째 연산은 수열 a의 모든 원소에 b[i]를 더한 후
# 2. 7의 배소인 원소들 제거 (v)
# 연산을 수행한 결과 수열 a의 모든 원소가 제거된다면 연산 수행 x (V)

# n, m <= 10만
# a[i], b[i] <= 십억

# 7 * 7 = 49
# n제한 : 10만


# """


# import sys
# input = lambda : sys.stdin.readline().strip()

# n, m = map(int, input().split())
# arr1 = list(map(int, input().split())) # 길이 n의 배열
# arr2 = list(map(int, input().split())) # m번 연산할 배열

# idx = [0 for i in range(7)]
# for i in arr1:
#     idx[i % 7] += 1
    
# print("초기 idx", idx)
    
# prefix = [0 for i in range(m)]
# prefix[0] = arr2[0]

# # 10만
# for i in range(1, m):
#     prefix[i] = prefix[i - 1] + arr2[i]
    
# print("초기 prefix", prefix)

# for i in range(m): # m번의 연산 수행
#     """
#     1일 때 6, 2일 때 5, 3일 때 4... 7일 때 0 지우기
#     """
#     tmp = idx[(7 - (prefix[i] % 7)) % 7]
    
#     idx[(7 - (prefix[i] % 7)) % 7] = 0 # 7의 배수 지우기
#     cnt = 0
#     for j in range(7): # 모든 원소가 제거되었는지 확인
#         if not idx[j]: # 0인 것 개수
#             cnt += 1
#     if cnt == 7: # 지울 숫자가 없는 경우
#         idx[(7 - (prefix[i] % 7)) % 7] = tmp # 복구
        

# # 예외처리

# if idx[0] == m:
#     print(m)
#     print(*arr1)

# else:
#     print("&&&&&&&&&&&&&&&&&&", idx)
#     answer = []
#     for i in range(7):
#         if not idx[i]:
#             continue
        
#         # i + 7n인 것들만 넣기, n번도 필요 없음
#         tmp_cnt = 0
#         while tmp_cnt < n // 7:
#             # 1, 3, 4, 6 -> 2, 3, 5, 7로 들어가야 함
#             # answer.append((arr1[i + 1 + (7 * tmp_cnt)]) + prefix[-1])
#             if i == 0:
#                 answer.append((arr1[6 + (7 * tmp_cnt)] + prefix[-1]) % (10**9 + 7))
#             else:
#                 answer.append((arr1[i - 1 + (7 * tmp_cnt)] + prefix[-1]) % (10**9 + 7))

#             tmp_cnt += 1
#             print(answer, "*************")
            

#     answer.sort()
# # print(1 // 7)
# # print(7//7)
# # print(8//7)
# # print("=====", idx)
# # print("=====", prefix)
#     print(len(answer))
#     print(*answer)

        



        

# # 1. i번째 연산은 수열 a의 모든 원소에 b[i]를 더한 후 <- 이거 남음
# """ 
# prefix = [1, 3, 6]
# idx = [1, 1, 1, 1, 1, 1, 1]

# prefix[0] = 1
# idx = [1, 1, 1, 1, 1, 1, 1]
# 처음에서 다 한 칸씩 밀림

# prefix[1] = 3
# 처음에서 다 3칸 밀림

# 배열 %
# idx -> idx[i + prefix[]]prefix[i]

# 1칸
# [1, 1, 1, 1, 1, 1] + [1]
# [1] +  [1, 1, 1, 1, 1, 1]


# 3칸
# [1, 1, 1, 1] + [1, 1, 1]
# [1, 1, 1] + [1, 1, 1, 1]

# """


# # # idx 배열에서 7의 배수 지우기
# # for i in range(7):
# #     tmp = idx[i]
# #     if idx[i] == 0: # ?
# #         idx[i] = 0
        
# #         # 모든 원소가 제거되었는지 확인
# #         cnt = 0
# #         for j in range(7):
# #             if not idx[j]: # 0인 것 개수
# #                 cnt += 1
# #         if cnt == 7: # 모두 0인 경우
# #             idx[i] = tmp # tmp 다시 넣기


# # idx 배열에서 7의 배수 지우기 - idx[0]만 확인

# # for i in range(m): # m번의 연산 수행
# #     tmp_idx = idx[-prefix[i]:] + idx[:-prefix[i]]
    
# #     tmp = tmp_idx[0] # tmp에 저장
# #     tmp_idx[0] = 0 # 7의 배수 지우기
# #     cnt = 0
# #     for j in range(7): # 모든 원소가 제거되었는지 확인
# #         if not tmp_idx[j]: # 0인 것 개수
# #             cnt += 1
# #     if cnt != 7: # 지울 숫자가 있는 경우 == 모두 7이 아닌 경우



import sys
input = lambda : sys.stdin.readline().strip()

n, m = map(int, input().split())
narr = list(map(int, input().split()))
marr = list(map(int, input().split()))

visited = [False for _ in range(7)]
cnt = 0
for i in range(n):
    if not visited[narr[i] % 7]:
        visited[narr[i] % 7] = True
        cnt += 1

    if cnt == 7:
        break

total = 0
chk = 0
for i in range(m):
    tmp = 7 - (chk + marr[i]) % 7 if (chk + marr[i]) % 7 != 0 else 0

    if visited[tmp]:
        if cnt == 1:
            continue
        visited[tmp] = False
        cnt -= 1

    chk = (chk + marr[i]) % 7
    total += marr[i]
    total %= (10**9 + 7)

ans = []
for i in range(n):
    if visited[narr[i] % 7]:
        ans.append((narr[i] + total) % (10**9 + 7))

print(len(ans))
print(*ans)
