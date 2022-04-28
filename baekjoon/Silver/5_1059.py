# n = int(input())
# arr = list(map(int, input().split()))
# k = int(input())


# cnt = 0
# for i in range(1, n):
#     s = 0
#     e = 0
#     if arr[i - 1] <= k <= arr[i]:
#         if k - arr[i - 1] > 1:
#             for j in range(arr[i - 1] + 1, k + 1):
#                 cnt += 1
        
#         if k - arr[i - 1] == 1:
#             for j in range(k + 1, arr[i]):
#                 cnt += 1
        
        

        
# print(cnt)


n = int(input())
arr = list(map(int, input().split()))
s = int(input())


cnt = 0
for i in range(1, n):
    if arr[i - 1] < s < arr[i]:
        for j in range(arr[i - 1] + 1, s + 1):
            for k in range(j + 1, arr[i]):
                print(f'#{arr[i-1]} {arr[i]} {j} {k}')
                cnt += 1

        # for j in range(arr[i - 1] + 1, s):
        #     cnt += 1

        
        # for j in range(s + 1, arr[i]):
        #     cnt += 1
        #     print(f'%{j}')
print(cnt)