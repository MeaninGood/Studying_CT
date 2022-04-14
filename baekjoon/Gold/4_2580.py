# 2580번_스도쿠

## 스도쿠 빈 칸(0) 채우기

'''
# 아홉 줄에 걸쳐 한 줄에 9개씩 게임 시작 전 스도쿠판 각 줄에 쓰여 있는 숫자가 한 칸씩 띄워서 차례로 주어짐
# 스도쿠 판의 빈 칸의 경우에는 0이 주어짐
# 스도쿠 판을 규칙대로 채울 수 없는 경우의 입력은 주어지지 않는다
## 모든 빈 칸이 채워진 스도쿠 판의 최종 모습을 아홉 줄에 걸쳐 한 줄에 9개씩 한 칸씩 띄워서 출력
## 스도쿠 판을 채우는 방법이 여럿인 경우는 그 중 하나만을 출력

(입력)
0 3 5 4 6 9 2 7 8
7 8 2 1 0 5 6 0 9
0 6 0 2 7 8 1 3 5
3 2 1 0 4 6 8 9 7
8 0 4 9 1 3 5 0 6
5 9 6 8 2 0 4 1 3
9 1 7 6 5 2 0 8 0
6 0 3 7 0 1 9 5 2
2 5 8 3 9 4 7 6 0

(출력)
1 3 5 4 6 9 2 7 8
7 8 2 1 3 5 6 4 9
4 6 9 2 7 8 1 3 5
3 2 1 5 4 6 8 9 7
8 7 4 9 1 3 5 2 6
5 9 6 8 2 7 4 1 3
9 1 7 6 5 2 3 8 4
6 4 3 7 8 1 9 5 2
2 5 8 3 9 4 7 6 1

'''



# import sys
# si = sys.stdin.readline

# def check_x(y, cur):
#     global i
#     for i in range(1, 10):
#         if arr[cur][y] == i:
#             return True
#         return False

# def check_y(x, cur):
#     global i
#     for i in range(1, 10):
#         if arr[x][cur] == i:
#             return True
#         return False



# def check_b(x, y, cur):
#     global i
#     nx = (x - 1) // 3
#     ny = (y - 1) // 3
#     cur = cur - 1
    
    
#     for i in range(1, 10):
#         if arr[(nx * 3) + 1 + cur // 3][(ny * 3) + 1 + cur % 3] == i:
#             return True
#         return False


# def check_b(x, y, cur):
#     global i
#     for i in range(1, 10):
#         for j in range(x // 3 * 3, x // 3 * 3 + 3):
#             for k in range(y // 3 * 3, y // 3 * 3 + 3):
#                 if arr[j][k] == i:
#                     return True
                
#         return False

# row: 1~3 column: 1~3 1구역

# def check_b(x, y):
#     # 1구역
#     if 0 <= x < 3 and 0 <= y < 3:
#         for i in range(1, 10):
#             for j in range(3):
#                 for k in range(3):
#                     if arr[i][j] == i:
#                         return True
#             return False
#     # 2구역    
#     elif 0 <= x < 3 and 3 <= y < 6:
#         for i in range(1, 10):
#             for j in range(3):
#                 for k in range(3, 6):
#                     if arr[i][j] == i:
#                         return True
#             return False
#     # 3구역    
#     elif 0 <= x < 3 and 6 <= y < 9:
#         for i in range(1, 10):
#             for j in range(3):
#                 for k in range(6, 9):
#                     if arr[i][j] == i:
#                         return True
#             return False
#     # 4구역    
#     elif 3 <= x < 6 and 0 <= y < 3:
#         for i in range(1, 10):
#             for j in range(3, 6):
#                 for k in range(3):
#                     if arr[i][j] == i:
#                         return True
#             return False
#     # 5구역    
#     elif 3 <= x < 6 and 3 <= y < 6:
#         for i in range(1, 10):
#             for j in range(3, 6):
#                 for k in range(3, 6):
#                     if arr[i][j] == i:
#                         return True
#             return False
#     # 6구역    
#     elif 3 <= x < 6 and 6 <= y < 9:
#         for i in range(1, 10):
#             for j in range(3, 6):
#                 for k in range(6, 9):
#                     if arr[i][j] == i:
#                         return True
#             return False
#     # 7구역    
#     elif 6 <= x < 9 and 0 <= y < 3:
#         for i in range(1, 10):
#             for j in range(6, 9):
#                 for k in range(3):
#                     if arr[i][j] == i:
#                         return True
#             return False
#     # 8구역    
#     elif 6 <= x < 9 and 3 <= y < 6:
#         for i in range(1, 10):
#             for j in range(6, 9):
#                 for k in range(3, 6):
#                     if arr[i][j] == i:
#                         return True
#             return False
#     # 9구역    
#     elif 6 <= x < 9 and 6 <= y < 9:
#         for i in range(1, 10):
#             for j in range(6, 9):
#                 for k in range(6, 9):
#                     if arr[i][j] == i:
#                         return True
#             return False

# import sys
# si = sys.stdin.readline

# def check_x(y, cur):
#     global i
#     for i in range(1, 10):
#         if arr[cur][y] == i:
#             return True
#         return False

# def check_y(x, cur):
#     global i
#     for i in range(1, 10):
#         if arr[x][cur] == i:
#             return True
#         return False

# def check_b(x, y, cur):
#     global i
#     for i in range(1, 10):
#         for j in range(x // 3 * 3, x // 3 * 3 + 3):
#             for k in range(y // 3 * 3, y // 3 * 3 + 3):
#                 if arr[j][k] == i:
#                     return True
                
#         return False

# arr = [list(map(int, si().split())) for _ in range(9)]

# li = []
# for i in range(9):
#     for j in range(9):
#         if arr[i][j] == 0:
#             li.append([i, j])

# print(li)

# def recur(num):
#     if num == len(li):
#         return
#     for cur in range(9):
#         if not check_x(li[0][1], cur) and not check_y(li[0][0], cur) and not check_b(li[0][0], li[0][1], cur):
#             arr[li[0][0]][li[0][1]] = i
#             recur(num + 1)
#             arr[li[0][0]][li[0][1]] = 0

# recur(0)

# print(arr)

# def recur(num):
#     if num == len(li):
#         return
#     for cur in range(1, 10):
#         if not check_x(li[0][1], cur) and not check_y(li[0][0], cur) and not check_b(li[0][0], li[0][1], cur):
#             arr[li[0][0]][li[0][1]] = cur
#             recur(num + 1)
#             arr[li[0][0]][li[0][1]] = 0


import sys
si = sys.stdin.readline

def check_x(x, cur):
    for i in range(9):
        if arr[x][i] == cur:
            return True
    return False
    
def check_y(y, cur):
    for i in range(9):
        if arr[i][y] == cur:
            return True
    return False

def check_b(x, y, cur):
    for i in range(x // 3 * 3, x // 3 * 3 + 3):
        for j in range(y // 3 * 3, y // 3 * 3 + 3):
            if arr[i][j] == cur:
                return True
    return False

def recur(num):
    if num == len(li):
        for i in range(9):
            print(*arr[i], sep='')
        exit()
    
    x1, y1 = li[num]
    for cur in range(1, 10):
        if not check_x(x1, cur) and not check_y(y1, cur) and not check_b(x1, y1, cur):
            arr[x1][y1] = cur
            recur(num + 1)
            arr[x1][y1] = 0
        

arr = [list(map(int, si().rstrip())) for _ in range(9)]

li = []
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            li.append([i, j])
            
recur(0)
