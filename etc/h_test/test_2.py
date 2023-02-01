# import sys
# from collections import deque
# input = lambda : sys.stdin.readline().strip()


# def in_range(x, y):
#     return 0 <= x < 8 and 0 <= y < 8    
    
# bishops = ["C6"]
# bishop1 = ["C6", "A4", "E5"]
# chess = [[False for _ in range(8)] for _ in range(8)]

# arr = []
# for i in range(len(bishops)):
#     arr.append([ord(bishops[i][0]) - ord('A'), int(bishops[i][1])])

# move = 0

# visited = [[False for i in range(8)] for j in range(8)]
# dx = [-1, -1, 1, 1]
# dy = [-1, 1, -1, 1]


# print(arr)
# print(64 - move)