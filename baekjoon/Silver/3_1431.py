'''
7
ABCD
Z
145C
CB
A
A910
Z321

'''
# n = int(input())
# arr = [input() for _ in range(n)]
# arr.sort(key = lambda x: len(x))
# print(arr)

# v = []
# mlen = len(arr[0])

# for i in range(1, n):
#     if len(arr[i]) > len(arr[i - 1]):
#         continue
    
#     if len(arr[i]) == len(arr[i - 1]):
        
         
    
n = int(input())
arr = [input() for _ in range(n)]
for i in range(n):
    total = 0
    for j in arr[i]:
        if '0' <= j <= '9':
            total += int(j)
    arr[i] = [total, arr[i]]

arr.sort(key = lambda x: x[1])
arr.sort(key = lambda x: x[0])
arr.sort(key= lambda x: len(x[1]))

for a, b in arr:
    print(b)
