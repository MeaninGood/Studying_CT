# 14846번_직사각형과 쿼리

## N행 N열로 이루어진 정사각형 행렬 A가 주어짐
## 왼쪽 윗칸이 (x1, y1), 오른쪽 아랫칸이 (x2, y2)인 부분 행렬에 포함되어 있는
## 서로 다른 정수의 개수를 출력

'''
# 첫째 줄에 N (1 ≤ N ≤ 300)
# 다음 N개의 줄에는 행렬의 정보가 주어지며, 각 줄은 N개의 수
# 행은 위에서부터 아래로, 열은 왼쪽부터 오른쪽으로 번호가 매겨져 있음
# 번호는 1번부터 시작
# 행렬이 포함하고 있는 정수는 10보다 작거나 같은 자연수
# 1번 칸과 100번 칸은 뱀과 사다리의 시작 또는 끝이 아님
# 다음 줄에는 Q (1 ≤ Q ≤ 100,000)
# 다음 Q개의 줄에는 쿼리의 정보 x1, y1, x2, y2. (1 ≤ x1 ≤ x2 ≤ n, 1 ≤ y1 ≤ y2 ≤ n)
## 각각의 쿼리마다 정답을 한 줄에 하나씩 출력

(입력)
3
1 2 3
3 2 1
5 6 3
3
1 1 2 3
2 2 2 2
1 1 3 3 

(출력)
3
1
5

'''

# n, m = map(int, input().split())
# arr = [[0 for i in range(n + 1)] + [0] + list(map(int, input().split())) for i in range(n)]
# prefix = [[0 for i in range(n + 1)] for j in range(n + 1)]

# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + arr[i][j]
        
# for _ in range(m):
#     a, b, c, d = map(int, input().split())
    
#     print(prefix[c][d] - prefix[a - 1][d] - prefix[c][b - 1] + prefix[a - 1][b - 1])
    
    

# import sys
# from pprint import pprint

# n = int(sys.stdin.readline())
# arr = [[0 for i in range(n + 1)]] + [[0] + list(map(int, sys.stdin.readline().split())) for j in range(n)]
# prefix = [[0 for i in range(n + 1)] for j in range(n + 1)]
# cnt = {}


# q = int(sys.stdin.readline())
# for _ in range(q):
#     x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if cnt.get(arr[i][j]):
#             cnt[arr[i][j]] += 1
#         else:
#             cnt[arr[i][j]] = 1
        
#         prefix[i][j] = cnt[arr[i][j]]

# pprint(arr)
# print(cnt)
# pprint(prefix)
# print(prefix[x1][x2])


import sys
from pprint import pprint

n = int(sys.stdin.readline())
arr = [[0 for i in range(n + 1)]] + [[0] + list(map(int, sys.stdin.readline().split())) for j in range(n)]
prefix = [[0 for i in range(n + 1)] for j in range(n + 1)]
cnt = {}


q = int(sys.stdin.readline())
for _ in range(q):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    
for i in range(1, n + 1):
    for j in range(1, n + 1):
        cnt[arr[i][j]] = 1
        
        if cnt.get(arr[i][j]):
            prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + 1
        else:
            prefix[i][j] = 1
            
'''
[[0, 0, 0, 0, 0, 0],
 [0, 1, 6, 4, 3, 7],
 [0, 6, 5, 6, 8, 4],
 [0, 2, 3, 4, 6, 4],
 [0, 2, 3, 5, 7, 4],
 [0, 4, 5, 6, 8, 9]]
{1: 1, 6: 5, 4: 6, 3: 3, 7: 2, 5: 3, 8: 2, 2: 2, 9: 1}
# 
[[0, 0, 0, 0, 0, 0],
 [0, 1, 6, 4, 3, 7],
 [0, 6, 5, 6, 8, 4]]

1 6 4 3 7



[[0, 0, 0, 0, 0, 0],
 [0, 1, 1, 1, 1, 1],
 [0, 2, 3, 4, 6, 7],



1 1 2 4
3 3 4 3
2 4 4 4
2 4 5 5





'''