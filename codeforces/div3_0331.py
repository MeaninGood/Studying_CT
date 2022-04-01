## 1

# n = int(input())
# for i in range(n):
#     a, b = map(int, input().split())
    
#     if a != 0 and b != 0:
#         print((1 * a) + (2 * b) + 1)
        
#     elif a == 0:
#         print(1)
        
#     elif b == 0:
#         print(1 * a + 1)
        
#     else:
#         print(1)


## 2

# def check():
#     if arr[0] <= 1:
#         return 'YES'
#     else:
#         return 'NO'

# T = int(input())
# for tc in range(T):
#     n = int(input())
#     arr = list(map(int, input().split()))
    
#     if n == 1:
#         print(check())
#         continue
        
    
#     mx = max(arr)
#     arr.pop(arr.index(mx))
#     mx2 = max(arr)
    
#     if mx - mx2 <= 1:
#         print('YES')
#     else:
#         print('NO')



# T = int(input())
# for i in range(T):
#     n = int(input())
#     arr = list(input())
#     arr2 = []
#     cnt = 0
#     for i in range(len(arr) - 1):
#         if arr == []:
#             if arr[i] == arr[i + 1]:
#                 arr2.append(arr[i])
#             elif arr[i] != arr[i + 1]:
#                 cnt += 1
#                 continue
        
#         if arr[i] == arr2[-1]:
#             arr2.append(arr[i])
        
#         if arr[i] != arr[i + 1]:
            



n = int(input())
arr = list(map(int, input().split()))

s = 0
e = 0
total = 1
cnt = 0

prefix = [-1 for i in range(n)]
prefix[0] = arr[0]
for i in range(1, n):
    prefix[i] = prefix[i - 1] * arr[i]

suffix = [-1 for i in range(n)]
suffix[0] = arr[-1]
for i in range(1, n)[::-1]:
    print(i)
    suffix[i] = suffix[n - i] * arr[i]

print(prefix)
print(suffix)
