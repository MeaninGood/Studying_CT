# arr = input()
# n = len(arr)

# T = int(input())
# v = []
# idx = 'b'
# for tc in range(T):
#     a, b, c = input().split()
#     idx = a
#     v.append([int(b), int(c)])
    
# print(idx)
# print(v)
# print(n)


# prefix = [0 for i in range(n)]
# suffix = [0 for i in range(n)]

# if arr[0] == idx:
#     prefix[0] = 1

# for i in range(1, n):
#     if idx == arr[i]:
#         prefix[i] = prefix[i - 1] + 1
#     else:
#         prefix[i] = prefix[i - 1]
        
# for i in range(n - 1)[::-1]:
#     if idx == arr[i]:
#         suffix[i] = suffix[i + 1] + 1
#     else:
#         suffix[i] = suffix[i + 1]

# print(prefix)
# print(suffix)
# for x, y in v:
#     print(prefix[x] + prefix[y - 1])


a = [int(input()) for _ in range(4)]

if a[0] < a[1] < a[2] < a[3]:
    print('Fish Rising')
elif a[0] == a[1] == a[2] == a[3]:
    print('Fish At Constant Depth')
elif a[0] > a[1] > a[2] > a[3]:
        print('Fish Diving')
else:
    print('No Fish')