def rotate(x, d, k):
    temp = [ 0 for i in range(m)] # m개 짜리 원판 만들어 놓고
                                    # 각 원판마다 회전 시킨 숫자 저장
     
    if d == 0: # 시계방향
        for i in range(m):
            # 범위 벗어날 수 있으니까 % m
            temp[(i + k) % m] = arr[x][i] # temp에 회전한 후의 숫자 저장
        # d == 0이면 arr[x][i]에 있던 게 arr[x][i + k]로 이동
        
    else:
        for i in range(m):
            # 음수 될 수 있으니까 +m
            temp[(i - k + m) % m] = arr[x][i] 
        # d == 1이면 arr[x][i]에 있던 게 arr[x][i - k]로 이동
        
    for i in range(m):
        arr[x][i] = temp[i] # 원판에 있는 숫자 바꿔주기
        

def check():
    for x in range(1, n + 1):
        for y in range(m):
            if arr[x][y] == 0: # 애들이 지워져있으면 continue
                                # 회전이 여러번 이루어짐
                continue
            
            for i in range(4):
                nx = x + dx[i]
                ny = (y + dy[i] + m) % m

                if nx < 1 or nx > n:
                    continue

                if arr[x][y] == arr[nx][ny]:
                    return True

    return False


def erase():
    # T, F로 구성된 배열 만들어서 원판에서 지워질 숫자 체크 해놓고
    # 한 번에 다 지울 것
    visited = [[False for i in range(m)] for j in range(n+1)]
    for x in range(1, n+1): # 모든 숫자 다 확인
        for y in range(m):
            for i in range(4): # 각 숫자의 상하좌우 4방향 확인
                nx = x + dx[i]
                # 각 원판의 숫자는 끝이 없으므로 % 로 쓰기
                # y + dy[i]가 음수가 될 수 있으니까 +m 해주기
                ny = (y + dy[i] + m) % m 
                
                # 1번 원판과 n번 원판은 각 끝에 위치하므로 범위 지정
                if nx < 1 or nx > n :
                    continue
                
                if arr[x][y] == arr[nx][ny]: # 같은 숫자가 있으면
                    visited[x][y] = True # 지워질 수 있는 위치 visited에 체크 

    for i in range(1, n+1): # 원판에서 숫자 제거
        for j in range(m):
            if visited[i][j]:
                arr[i][j] = 0
                

def to_avg(): # 인접하면서 수가 같은 게 없는 경우 평균 만들기
    total = 0
    cnt = 0
    for i in range(1, n+1):
        for j in range(m):
            if arr[i][j] == 0: # 숫자가 지워져있으면 continue 
                continue
            
            total += arr[i][j] # 아니면 total에 더해주고
            cnt += 1 # 숫자 개수 세어주기
            
    for i in range(1, n+1):
        for j in range(m):
            if arr[i][j] == 0:
                continue
            
            # 평균 구하기
            # total / cnt에서 cnt를 양 변에 곱해줌
            # 실수 연산 오차 없애기 위해서
            if arr[i][j] * cnt > total:
                arr[i][j] -= 1
                
            elif arr[i][j] * cnt < total:
                arr[i][j] += 1
                
                
n, m, t =map(int, input().split())
arr = [ [0 for i in range(m)]] + [list(map(int, input().split())) for i in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(t):
    x, d, k = map(int, input().split())
    
    # 원판 하나를 회전시켜주는 함수
    
    for i in range(x, n+1, x): #번호가 x의 배수인 원판을 회전시켜야 함
        rotate(i, d, k) # i번쨰 원판을 d방향으로 k칸 회전하는 함수
        
    if check(): # 인접하면서 같은 수가 있으면
        erase() # 지우고
        
    else : # 없으면
        to_avg() # 평균을 구하고 평균보다 큰 수에서 ...
        
ans = 0 # 전체 원판의 합 구하기
for i in range(1, n+1):
    for j in range(m):
        ans += arr[i][j]

print(ans)