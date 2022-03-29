# 9184번_신나는 함수 실행

##  재귀함수 w(a, b, c)
## a, b, c가 주어졌을 때, w(a, b, c)를 출력하는 프로그램을 작성

'''
# 입력은 세 정수 a, b, c로 이루어져 있으며, 한 줄에 하나씩 주어짐
# 입력의 마지막은 -1 -1 -1
# 세 정수가 모두 -1인 경우는 입력의 마지막을 제외하면 없음
# -50 ≤ a, b, c ≤ 50
## 입력으로 주어진 각각의 a, b, c에 대해서, w(a, b, c)를 출력

(입력)
1 1 1
2 2 2
10 4 6
50 50 50
-1 7 18
-1 -1 -1

(출력)
w(1, 1, 1) = 2
w(2, 2, 2) = 4
w(10, 4, 6) = 523
w(50, 50, 50) = 1048576
w(-1, 7, 18) = 1

'''
dp = [[[-1 for i in range(51)] for j in range(51)] for k in range(51)]
def recur(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    
    if dp[a][b][c] != -1:
        return dp[a][b][c]
    
    if a > 20 or b > 20 or c > 20:
        return recur(20, 20, 20)
    
    if a < b and b < c:
        dp[a][b][c] = recur(a, b, c - 1) + recur(a, b - 1, c - 1) - recur(a, b - 1, c)
        return dp[a][b][c]
        
    else:
        dp[a][b][c] = recur(a - 1, b, c) + recur(a - 1, b - 1, c) + recur(a - 1, b, c - 1) - recur(a - 1, b - 1, c - 1)
        return dp[a][b][c]
    
while 1:
    a, b, c = map(int, input().split())
    
    if a == -1 and b == -1 and c == -1:
        break
    
    print(f'w({a}, {b}, {c}) = {recur(a, b, c)}')