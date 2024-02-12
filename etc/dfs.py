from collections import deque


n, m = map(int, input().split())
arr = [input() for i in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def bfs(x, y):
    que = deque()
    visited = [[False for i in range(m)] for j in range(n)]

    que.append([x, y])
    visited[x][y] = True

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not in_range(nx, ny) or visited[nx][ny] or arr[nx][ny] != '0':
                continue

            que.append([nx, ny])
            visited[nx][ny] = True



# 다음과 같은 기본형 코드에서 벽 뚫는 조건 추가
from collections import deque


n, m = map(int, input().split())
arr = [input() for i in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def bfs(x, y, hand):
    que = deque()
    visited = [[False for i in range(m)] for j in range(n)]

    # 8. False를 위처럼 2차원이 아니라 3차원으로 만들어 줌
    # 좀 넉넉하게 걍 3개 만들어줌
    visited = [[[False for k in range(3)]for i in range(m)] for j in range(n)]

    # 3. 밑에 다 설명 후 뚫어본 애인지, 안 뚫어본 애인지 같이 저장
    que.append([x, y, hand])

    # 9. 그렇게 해서 이 3개까지 방문처리를 함
    visited[x][y][hand] = True

    # 11. d = 1 넣어주고 - 시작점을 포함하는 문제다. 시작점 1 넣어주기
    d = 1
    while que:

        # 12. 사이즈 넣어주고
        size = len(que)

        # 13. 사이즈만큼 돌아주고
        for _ in range(size):

            # 4. 손 떨리는지 안 떨리는지 같이 저장
            x, y, hand = que.popleft()

            # 15. d += 1 해준 후 종료조건 설명
            if x == n - 1 and y == m - 1:
                return d

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                # 1. arr[nx][ny] != '0'인 조건 제거, 벽 뚫을 수 있기 때문
                if not in_range(nx, ny) or visited[nx][ny]:
                    continue

                # 17. 위에 저거 주석치고
                if not in_range(nx, ny):
                    continue

                # 2. 벽인 경우 컨티뉴해야 하는 경우는 딱 하나, 내가 벽을 뚫어봤다면 컨티뉴.
                # 이걸 어떻게 알 수 있을까?
                # 내 손이 떨리는지 안 떨리는지 확인하기 - 변수에 담아서 확인
                """
                0000
                1110
                0000
                0111
                1111
                0000
                
                0,0에서 아래로가고 아래로 가면서 방문처리 무턱대고 해버리면 안 됨.
                0에서 밑으로 출발한 애랑 오른쪽으로 출발한 애는 뚫어본 애인지 아닌지 또 다름.
                그래서 que에다가 뚫어본 애다, 안 뚫어본 애다 라는 정보를 같이 저장해줄 것.
                """

                # 5. 바로 컨티뉴 하는 게 아니고, 한 단계를 더 봄. 그게 벽이냐 아니냐
                # 만약에, 아직 한 번도 안 뚫어 봤고, arr[nx][ny]가 벽이라면 hand는 1이됨
                # 만약에, 뚫어 봤고 arr[nx][ny]가 벽이라면 hand는 2가 됨
                nhand = hand + int(arr[nx][ny])

                # 6. 벽을 뚫어본 애라면 컨티뉴 조건을 추가해주고
                if nhand > 1:
                    continue

                # 18. nhand 조건 추가
                if nhand > 1 and visited[nx][ny][nhand]:
                    continue
                
                # 6. 여기다가 nhand 같이 넘겨줌
                que.append([nx, ny, nhand])

                # 7. 그리고 아까, 방문처리 무턱대고 다 해버리면 다른 애가 못 가는 경우가 생김
                # 벽을 뚫고 지나간 애가 이미 방문처리를 해버리면 다른 경로로 가고 있던 벽 안 뚫은 애가 못 지나감
                # 그래서 벽을 뚫어본 애들이랑, 안뚫어본 애들이 방문처리를 각각 다르게 써야 함
                # 뚫어본 애들끼리만 쓰는 방문처리, 안 뚫어본 애들만 쓰는 방문처리
                # 맨 위로 올라가서 visited 3차원으로
                visited[nx][ny] = True
                
                # 10. 얘도 같이 3개까지 방문처리
                # 즉, nx에 ny에 nhand까지 다 똑같아야 같은 노드로 취급하겠다는 뜻
                # 뚫어본 횟수가 다른 애들은 다른 경로를 가는 애들이다
                visited[nx][ny][nhand] = True

                # 이렇게 했을 때, 이제 거리 구하는 코드 넣어주면 됨. 맨 위로 가서 d = 0
        
        # 14. 갈 때마다 사이즈 추가해주면 됨. 이후 que.popleft에서 종료 조건 추가
        d += 1


    # 16. n - 1, m - 1 까지 끝까지 못갔다면 -1 리턴해주면 끝
    # 아 위에 visited[nx][ny][nhand] 컨티뉴 안 해줌 위로 올라가서 조건 달아주기
    return -1

print(bfs(0, 0, 0))


"""
내가 벽을 뚫어봤다, 안 뚫어봤다 같은 경로에 대한 정보는 큐에다가 같이 넣어줘야 함
현재 위치는 어디고, 내가 지나온 경로에서 벽을 뚫어봤다, 안 뚫어봤다

큐에 3개 넣으면 방문처리 3차원, 4개면 4차원, 5개면 5차원 써라
큐에 넣는 거에 따라서 방문처리 차원 늘려주면 됨

x,y에서 벽을 깨본 애랑 안 깨본 애는 다른 애들임.
그니까 방문처리를 다르게 해줘야 함.

"""