# T = int(input())

# for tc in range(T):
#     x, y = map(int, input().split())
    
#     sx = 0
#     sy = 0
#     cnt = 0
#     dp = [[-1 for i in range(y)] for j in range(x)]
    
# def dfs(s, e):
#     for i in range(x):
#         for j in range(y):
#             if dp[i][j] != -1:
#                 return dp[i][j]
            
#             if i == x and j == y:
#                 return dp[i][j]
            
#             a = ((sx - i)**2 + (sy - j)**2)**(1/2)
            
#             if a == int(a) and a != 0 and a != 1:
#                 cnt += 1
#                 sx, sy = i, j
#                 print(sx, sy)
                
            
      
#     print(cnt)
    

'''
3
8 6
0 0
9 15

'''
# a = ((0 - 8)**2 + (0 - 6)**2)**(1/2)
# b = 10

# print(a)
# print(int(a))
# print(a == int(a))
# print(a ** 2)

# if a == b:
#     print('#')
# else:
#     print('%')
# print(type(a))
# print(a / 1)

# a = ((0 - 0)**2 + (1 - 0)**2)**(1/2)

# print(a)

from collections import deque
from pprint import pprint
T = int(input())

for tc in range(T):
    x, y = map(int, input().split())
    
    sx = 0
    sy = 0
    cnt = 0
    arr = [[-1 for i in range(y + 1)] for j in range(x + 1)]
    li = []
    for i in range(x + 1):
        for j in range(y + 1):
            cnt = 0
            
            if x == sx and y == sy:
                print(cnt)
                
            a = ((sx - i)**2 + (sy - j)**2)**(1/2)
            
            if a == int(a):
                arr[i][j] = a
                li.append([i, j])
                
                if [x, y] in li:
                    cnt += 1
                    print(cnt)
                else:
                    
                    sx, sy = i, j
    
    