# import sys
# input = sys.stdin.readline

# n = int(input())
# arr = [int(input()) for i in range(n)]
# v = [0 for i in range(n + 1)]

# for i in arr:
#     v[i] += 1
    
# print(v.index(max(v)))


import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for i in range(n)]
arr.sort()

d = {}
mx = -100000
for i in arr:
    d[i] = d.get(i, 0) + 1
    mx = max(mx, d[i])
    
for i in d:
    if d[i] == mx:
        print(i)
        break
    
