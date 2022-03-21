# bsf 이론
# bfs <-> dfs 둘 다 할 수 있는 일들
# bfs만 되는 최단거리 문제들(왜 bfs로 푸는지)
# bfs로 최단거리 구하는 세가지 방법
# 상태가 뭔지, 방문처리

# 1. 시작 노드(1)를 큐에 넣는다
# 2. 반복
# 큐에서 하나를 뺀다
# 주변 노드 중 방문 안 한 노드를 모두 방문처리 하면서 큐에 넣는다

# 1260
from collections import deque

def bfs(s):
    que = deque()
    # 재귀를 쓰지 않기 때문에 함수 안에서 만들어도 상관 없음
    # dfs는 재귀를 쓰기 때문에 visited를 밖에서 만들어야 했음
    visited = [False for i in range(n + 1)]
    
    que.append(s) # 시작노드 넣기
    visited[s] = True # .시작노드 방문처리
    while len(que) > 0 : # 큐가 빌 때까지
        cur = que[0] # 나오는 애들
        que.popleft() # 큐에서 제일 앞에 있는 걸 가져와서
        
        print(cur) # 출력을 여기서 해줌
        
        # dfs는 방문처리 visited[i] = True를 여기서 했음
        # bfs는 방문처리를 for문 안에서 해줌
        for nxt in v[cur]:
            if visited[nxt]:
                continue
            
            que.append(nxt)
            visited[nxt] = True  # 얘는 여기서 함
            

def dfs(cur):
    visited[cur] = True # 이번 노드를 어떻게 처리할 건지
                        # 함수 계속 호출하면서
    print(cur)
    
    for nxt in v[cur]:
        if visited[nxt]:
            continue
        
        dfs(nxt)

n, m, s = map(int, input().split())

v = [[] for i in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    
    v[a].append(b)
    v[b].append(a)



# dfs vs bfs
# 1. s에서 갈 수 있는 모든 노드 방문처리
# 2. 같은 연결요소에 포함된 노드의 개수 구하기(크기)
# 3. 연결 요소의 개수
# 4. 플러드필

# bfs로 저거 다 할 수 있는데 왜 dfs 쓰냐?
# -> 구현이 편함. 경로 저장, 큐의 메모리초과 해결


# 바이러스 - 연결 요소 크기 구하기, 2606

def bfs(cur):
    que = deque()
    visited = [False for i in range(n + 1)]
    
    cnt = 0 # append해줄 때마다 cnt ㄹ하나씩 늘려주기
    que.append(s)
    visited[que] = True
    while len(que) > 0:
        cur = que[0]
        que.popleft()
        
        cnt += 1 # 방법 2. 큐에서 뺄 때마다 cnt += 1
        
        for nxt in v[cur]:
            if visited[nxt]:
                continue
            
            # cnt += 1 # 방법 1. append해줄 때마다 cnt += 1
            que.append(nxt)
            visited[nxt] = True
            
n = int(input())
m = int(input())


# # 연결요소의 개수


def bfs(cur):
    que = deque()
 
    que.append(s)
    visited[que] = True
    while len(que) > 0:
        cur = que[0]
        que.popleft()
        
        for nxt in v[cur]:
            if visited[nxt]:
                continue
            
            que.append(nxt)
            visited[nxt] = True
            
n, m = map(int, input().split())
v = [[] for i in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    
    v[a].append(b)
    v[b].append(a)
    
visited = [False for i in range(n+1)] # 방문처리 여기서 해줌
cnt = 0

# dfs로 풀 때
for i in range(1, n+1):
    if visited[i]:
        continue
    
    bfs[i]
    cnt += 1
    
print(cnt)



# 3. bfs로만 되는 것들 - 최단거리 구하기
# 발견하는 순간 최단거리였다는 것을 알 수 있음!
# 1. visited 배열에 방문여부가 아니라 거리를 저장
# 2. visited[nxt] = 0

# 숨바꼭질 2
from collections import deque
from operator import truediv
s, e = map(int, input().split())
visited = [ -1 for i in range(200010)] # 안전하게 20만개로
# 1. False가 아니라 -1로 만들고, -1은 방문 안 한 점
# 노드에 대한 정보를 배열에 저장

que = deque()

que.append(s)
visited[s] = 0
while len(s) > 0:
    cur = que[0] # cur이 나고, nxt가 내가 갈 수 있는 애들이니까
                # nxt는 무조건 cur보다 1이 더 크다 (다음에 갈 수 있는 애들이니까)
    que.popleft()
    
    if cur == e:
        print(visited)
    
    # 간선이 3개로 주어지니까, 3개로 만들어줌
    nxt = cur - 1 # 좌
    if 0 <= nxt < 200010 and visited[nxt] == -1:
        que.append(nxt)
        visited[nxt] = visited[cur] + 1
        
    nxt = cur + 1 # 우
    if 0 <= nxt < 200010 and visited[nxt] == -1:
        que.append(nxt)
        visited[nxt] = visited[cur] + 1


    nxt = 2 * cur # 순간이동
    if 0 <= nxt < 200010 and visited[nxt] == -1:
        que.append(nxt)
        visited[nxt] = visited[cur] + 1

print(visited[e])


from collections import deque
s, e = map(int, input().split())
visited = [ -1 for i in range(200010)] # 안전하게 20만개로
# 2. 거리정보를 큐에 같이 저장 (리스트로)
# 경로에 대한 정보를 큐에 저장


que = deque()

que.append([s, 0])
visited[s] = True
while len(s) > 0:
    cur = que[0][0] # cur이 나고, nxt가 내가 갈 수 있는 애들이니까
                # nxt는 무조건 cur보다 1이 더 크다 (다음에 갈 수 있는 애들이니까)
    d = que[0][1] # 거리 정보
    que.popleft()
    
    if cur == e:
        print(d)
        
    
    # 간선이 3개로 주어지니까, 3개로 만들어줌
    nxt = cur - 1 # 좌
    if 0 <= nxt < 200010 and not visited[nxt]:
        que.append([nxt, d+1])
        visited[nxt] = visited[cur] + 1
        
    nxt = cur + 1 # 우
    if 0 <= nxt < 200010 and not visited[nxt]:
        que.append([nxt, d+1])
        visited[nxt] = visited[cur] + 1


    nxt = 2 * cur # 순간이동
    if 0 <= nxt < 200010 and not visited[nxt]:
        que.append([nxt, d+1])
        visited[nxt] = visited[cur] + 1

print(visited[e])


# 3. level 단위로 실행
# 0층 -> 1층 -> 2층, size 정하고 for문으로 돌려줌
# 거리 바로 뽑아줄 수 있음
from collections import deque
s, e = map(int, input().split())
visited = [False for i in range(200010)]

que = deque()

d = 0
que.append(s)
visited[s] = True

while len(s) > 0:
    size = len(que)
    
    for _ in range(size):
        cur = que[0] # cur이 나고, nxt가 내가 갈 수 있는 애들이니까
                # nxt는 무조건 cur보다 1이 더 크다 (다음에 갈 수 있는 애들이니까)
        que.popleft()
    
        if cur == e:
            print(d) # 지금이 몇 레벨인지에 대한 정보가 d에 저장되어 있음
    
        # 간선이 3개로 주어지니까, 3개로 만들어줌
        nxt = cur - 1 # 좌
        if 0 <= nxt < 200010 and not visited[nxt]:
            que.append(nxt)
            visited[nxt] = True
            
        nxt = cur + 1 # 우
        if 0 <= nxt < 200010 and not visited[nxt]:
            que.append(nxt)
            visited[nxt] = True


        nxt = 2 * cur # 순간이동
        if 0 <= nxt < 200010 and not visited[nxt]:
            que.append(nxt)
            visited[nxt] = True

    d += 1
    
print(visited[e])


# 미로 찾기
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
n, m = map(int, input().split())

def bfs(s):
    q = deque()
    visited = [False for i in range(n+1)]
    
    que.append(s)
    visited[s] = True
    
    while len(que) > 0:
        cur = que[0]
        que.popleft()
        
        for nxt in v[cur]:
            if visited[nxt]:
                continue
            
            que.append(nxt)
            visited[nxt]


def bfs(s):
    que = deque()
    visited = [False for i in range(n + 1)]

    que.append(s)
    visited[s] = True
    while len(que) > 0:
        cur = que[0]
        que.popleft()

        for nxt in v[cur]:
            if visited[nxt]:
                continue

            que.append(nxt)
            visited[nxt]




def bfs(x, y):
    que = deque()
    visited = [[False for i in range(m)] for j in range(n)]

    que.append([x, y])
    visited[x][y] = True
    
    while len(que) > 0:
        x = que[0][0]
        y = que[0][1]
        que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if not (0 <= nx < n and 0 <= ny < m) or visited[nx][ny] or arr[nx][ny] != '1':
                continue
            
            que.append([nx, ny])
            visited[nx][ny] = True