# def in_range(x, y):
#     return 0 <= x < n and 0 <= y < m

# def range_check(x, y):
#     for i in range(2):
#         for j in range(2):
#             if not in_range(x + i, y + j):
#                 return False
            
#     return True

# def block_check(x, y):
#     if arr[x][y] != '.' and arr[x][y] != '#' and arr[x][y] == arr[x + 1][y] == arr[x][y + 1] == arr[x + 1][y + 1]:
#         return True
    
#     return False

# def move():
#     for i in range(n)[::-1]:
#         for j in range(m):
#             idx = arr2[i][j]
#             if (i + 1 < n) and arr2[i][j] != '.' and arr2[i][j] != '#':
#                 if arr2[i + 1][j] == '.' or arr2[i + 1][j] == '#':
#                     x = i
#                     while x < n:
#                         arr2[x][j] = '#'
                        
#                         if arr2[x + 1][j] != '.' and arr2[x + 1][j] != '#':
#                             arr2[x][j] = idx
#                             break
                        
#                         x += 1

                
# def solution(m, n, board):
#     global arr, arr2
#     answer = 0
#     m, n = n, m
    
#     arr = []
#     arr2 = []
#     for i in range(n):
#         arr.append(list(board[i]))
#         arr2.append(list(board[i]))

#     idx = 0
#     while idx < 2:
#         tmp = []
#         for i in range(n):
#             for j in range(m):
#                 if not range_check(i, j) or not block_check(i, j):
#                     continue
                
#                 else:
#                     tmp.append([[i, j], [i + 1, j], [i, j + 1], [i + 1, j + 1]])
                    
#         if tmp == []:
#             break
        
#         print(tmp)
        
#         for i in range(n):
#             for j in tmp:
#                 for k in j:
#                     a, b = k
#                     arr2[a][b] = '.'
        
#         move()
        
#         idx += 1
#         print(arr)
#         print(arr2)
    
#     return answer

# board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
# m = 6
# n = 6

# print(solution(m, n, board))



# def in_range(x, y):
#     return 0 <= x < n and 0 <= y < m

# def range_check(x, y):
#     for i in range(2):
#         for j in range(2):
#             if not in_range(x + i, y + j):
#                 return False
            
#     return True

# def block_check(x, y):
#     if arr[x][y] != '.' and arr[x][y] == arr[x + 1][y] == arr[x][y + 1] == arr[x + 1][y + 1]:
#         return True
    
#     return False

# def move():
#     for i in range(n)[::-1]:
#         for j in range(m):
#             idx = arr[i][j]
#             if (i + 1 < n) and arr[i][j] != '.':
#                 if arr[i + 1][j] == '.':
#                     x = i
#                     while x < n:
#                         arr[x][j] = '.'
                        
#                         if arr[x + 1][j] != '.':
#                             arr[x][j] = idx
#                             break
                        
#                         x += 1

                
# def solution(m, n, board):
#     global arr
#     answer = 0
#     m, n = n, m
    
#     arr = []
#     for i in range(n):
#         arr.append(list(board[i]))

#     idx = 0
#     while 1:
#         tmp = []
#         for i in range(n):
#             for j in range(m):
#                 if not range_check(i, j) or not block_check(i, j):
#                     continue
                
#                 else:
#                     tmp.append([[i, j], [i + 1, j], [i, j + 1], [i + 1, j + 1]])
                    
#         if tmp == []:
#             break
        
#         print(tmp)
        
#         for i in range(n):
#             for j in tmp:
#                 for k in j:
#                     a, b = k
#                     arr[a][b] = '.'
        
#         move()
    
#     for i in range(n):
#         for j in range(m):
#             if arr[i][j] == '.':
#                 answer += 1
    
#     return answer

# board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
# m = 6
# n = 6

# print(solution(m, n, board))


# from pprint import pprint


# def solution(m, n, board):
#     def in_range(x, y):
#         return 0 <= x < n and 0 <= y < m

#     def range_check(x, y):
#         for i in range(2):
#             for j in range(2):
#                 if not in_range(x + i, y + j):
#                     return False

#         return True


#     def block_check(x, y):
#         if arr[x][y] != '.' and arr[x][y] == arr[x + 1][y] == arr[x][y + 1] == arr[x + 1][y + 1]:
#             return True

#         return False

#     def move():
#         for i in range(n)[::-1]:
#             for j in range(m):
#                 idx = arr[i][j]
#                 if (i + 1 < n) and arr[i][j] != '.':
#                     if arr[i + 1][j] == '.':
#                         x = i
#                         while x < n:
#                             arr[x][j] = '.'

#                             if (x + 1 >= n) or arr[x + 1][j] != '.':
#                                 arr[x][j] = idx
#                                 break

#                             x += 1

#     answer = 0
#     m, n = n, m
    
#     arr = []
#     for i in range(n):
#         arr.append(list(board[i]))

#     pprint(arr)
#     while 1:
#         tmp = []
#         for i in range(n - 1):
#             for j in range(m - 1):
#                 if not range_check(i, j) or not block_check(i, j):
#                     continue
                
#                 else:
#                     tmp.append([[i, j], [i + 1, j], [i, j + 1], [i + 1, j + 1]])
                    
#         if tmp == []:
#             break
        
        
#         for i in range(n):
#             for j in tmp:
#                 for k in j:
#                     a, b = k
#                     arr[a][b] = '.'
        
#         pprint(arr)
        
#         move()
        
#         pprint(arr)
        
    
#     for i in range(n):
#         for j in range(m):
#             if arr[i][j] == '.':
#                 answer += 1
#     return answer


# print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))







def solution(m, n, board):
    def in_range(x, y):
        return 0 <= x < n and 0 <= y < m

    def range_check(x, y):
        for i in range(2):
            for j in range(2):
                if not in_range(x + i, y + j):
                    return False

        return True


    def block_check(x, y):
        if arr[x][y] != '.' and arr[x][y] == arr[x + 1][y] == arr[x][y + 1] == arr[x + 1][y + 1]:
            return True

        return False

    def move():
        for i in range(n)[::-1]:
            for j in range(m):
                idx = arr[i][j]
                if (i + 1 < n) and arr[i][j] != '.':
                    if arr[i + 1][j] == '.':
                        x = i
                        while x < n:
                            arr[x][j] = '.'

                            if (x + 1 >= n) or arr[x + 1][j] != '.':
                                arr[x][j] = idx
                                break

                            x += 1

    answer = 0
    m, n = n, m
    
    arr = []
    for i in range(n):
        arr.append(list(board[i]))

    while 1:
        tmp = []
        for i in range(n - 1):
            for j in range(m - 1):
                if not range_check(i, j) or not block_check(i, j):
                    continue
                
                else:
                    tmp.append([[i, j], [i + 1, j], [i, j + 1], [i + 1, j + 1]])
                    
        if tmp == []:
            break

        for i in tmp:
            for j in i:
                a, b = j
                arr[a][b] = '.'
   
        move()
    
    for i in range(n):
        for j in range(m):
            if arr[i][j] == '.':
                answer += 1
                
    return answer