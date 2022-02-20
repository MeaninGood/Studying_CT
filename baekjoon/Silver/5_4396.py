dx = [-1, -1, -1, 0, 0, 1, 1, 1] # 8방향 row
dy = [-1, 0, 1, -1, 1, -1, 0, 1] # 8방향 column


# dx = [-2, -2, -1, -1, 1, 1, 2, 2] # 체스의 나이트
# dy = [-1, 1, -2, 2, -2, 2, -1, 1] 

n = int(input())
mine = [list(input()) for i in range(n)]
arr = [list(input()) for i in range(n)]


def opened():
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'x':
                arr[i][j] = 0

# 지뢰 밟았을 떄의 함수

def count_mine(x, y):
    # .이면 그냥 return
    if arr[x][y] == '.':
        return
    
    # 8방향 확인해주기 //  같은 방향 확인하니까 dx[i], dy[i]만 쓰기
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        # 범위 체크, mine에서 *인 곳 긁어오기
        if 0 <= nx < n and 0 <= ny < n and mine[nx][ny] == '*':
            arr[x][y] += 1
            

# 지뢰 밟았는지 안 밟았는지 판별해줄 함수
die = False
for i in range(n):
    for j in range(n):
            opened()
            count_mine(i, j)
            
            # 지뢰 밟았을 때 우선 True로 해줌
            # 여기서 바로 arr[i][j]를 *로 바꾸면 지뢰 만나기 전의
            # 앞에 것들은 바뀌지 않음
            if arr[i][j] != '.' and mine[i][j] == '*':
                die = True
                
for i in range(n):
    for j in range(n):
        if die and mine[i][j] == '*':
            arr[i][j] = '*'

        # 열려 있는 칸에서 =  다 0으로 바꿔주기
        #지뢰 체크
        
        
        # 열려있는 지뢰판 8방향 확인해서 지뢰가 있는지 확인
        # 개수 세어서 넣어주기
        # 만약에 열린 칸이 지뢰칸이면 지뢰가 있는 모든 칸이 표시됨
        
for i in range(n):
    print(''.join(map(str, arr[i])))