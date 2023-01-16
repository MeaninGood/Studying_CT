from pprint import pprint

board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]

skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]


# def solution(board, skill):
    
#     n, m = len(board), len(board[0])
    
#     answer = n * m
                    
#     for k in range(len(skill)):
#         x1, y1, x2, y2, deg = skill[k][1], skill[k][2], skill[k][3], skill[k][4], skill[k][5]
#         if skill[k][0] == 1:
#             for i in range(x1, x2 + 1):
#                 for j in range(y1, y2 + 1):
#                     if (board[i][j] >= 1) and (board[i][j] - deg < 1):
#                         answer -= 1
                        
#                     board[i][j] -= deg
        
#         elif skill[k][0] == 2:
#             for i in range(x1, x2 + 1):
#                 for j in range(y1, y2 + 1):
#                     if (board[i][j] < 1) and board[i][j] + deg >= 1:
#                         answer += 1
                        
#                     board[i][j] += deg

#     return answer


# print(solution(board, skill))

def solution(board, skill):
    answer = 0    
    n, m = len(board), len(board[0])

    prefix = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    
    for k in range(len(skill)):
        x1, y1, x2, y2, deg = skill[k][1], skill[k][2], skill[k][3], skill[k][4], skill[k][5]
        if skill[k][0] == 1:
            prefix[x1][y1] -= deg
            prefix[x1][y2 + 1] += deg
            prefix[x2 + 1][y1] += deg
            prefix[x2 + 1][y2 + 1] -= deg
        
        elif skill[k][0] == 2:
            prefix[x1][y1] += deg
            prefix[x1][y2 + 1] -= deg
            prefix[x2 + 1][y1] -= deg
            prefix[x2 + 1][y2 + 1] += deg

    pprint(prefix)      
    # for i in range(n):
    #     for j in range(m):
    
    for i in range(n + 1):
        for j in range(1, m + 1):
            prefix[i][j] += prefix[i][j - 1]
    pprint(prefix)
    
    for i in range(m + 1):
        for j in range(1, n + 1):
            prefix[j][i] += prefix[j - 1][i]
    pprint(prefix)
    
    for i in range(n):
        for j in range(m):
            board[i][j] += prefix[i][j]
            
            if board[i][j] > 0:
                answer += 1
    return answer

print(solution(board, skill))

