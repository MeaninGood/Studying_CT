# 2239번_스도쿠

## 스도쿠 빈칸 채우기

'''
# 9개의 줄에 9개의 숫자로 보드가 입력
# 아직 숫자가 채워지지 않은 칸에는 0이 주어짐
## 9개의 줄에 9개의 숫자로 답을 출력
## 답이 여러 개 있다면 그 중 사전식으로 앞서는 것을 출력
## 81자리의 수가 제일 작은 경우를 출력

(입력)
103000509
002109400
000704000
300502006
060000050
700803004
000401000
009205800
804000107

(출력)
143628579
572139468
986754231
391542786
468917352
725863914
237481695
619275843
854396127

'''

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