# 트리의 정의
# 1. 노드의 개수가 N일 떄, 간선의 개수가 N-1이다
# 2. 모든 노드가 하나의 연결요소 or 사이클이 없다.

# 서브트리 : 아무 노드나 잡고 그의 자식, 자식 없는 경우 노드 하나도 트리

### 트리에서의 dfs - 사이클이 없음
## 1에서 6으로 들어가면, 바로 1로 다시 돌아가는 경로가 없다.
## 왔던 길을 돌아가지 않으면 절대로 방문했던 곳을 갈 일 없다.

## 방문처리 대신 prv 써줌
## 주변 노드에서 이전 노드 빼고 다 들어가라



### 트리의 부모 찾기
n = int(input())
v = [[] for i in range(n + 1)]
par = [0 for i in range(n + 1)]

for i in range(n - 1):
    a, b = map(int, input().split())
    v[a].append(b)
    v[b].append(a)
    
def dfs(cur, prv):
    # 이전에 방문한 곳이 부모노드가 됨
    # 저장해주기
    par[cur] = prv
    
    for nxt in v[cur]:
        if nxt == prv:
            continue
        
        # par[nxt] = cur 여기서 해줘도 됨
        dfs(nxt, cur)
        
dfs(1, -1)

for i in range(2, n + 1):
    print(par[i])
    
    

### 트리와 쿼리 - 서브트리
## 연결요소의 크기 구하기의 트리버전

n, r, q = map(int, input().split())
v = [[] for i in range(n + 1)]

for i in range(n - 1):
    a, b = map(int, input().split())
    v[a].append(b)
    v[b].append(a)
    
    
size = [0 for i in range(n + 1)]

def dfs(cur, prv):
    size[cur] = 1
    for nxt in v[cur]:
        if nxt == prv:
            continue
        
        size[cur] += dfs(nxt, cur)
        
    return size[cur]
        
dfs(r, -1)

for i in range(q):
    x = int(input())
    
    print(size[x])
    
    
    
### 가장 가까운 공통 조상

t = int(input())

for _ in range(t):
    n = int(input())
    par = [0 for i in range(n + 1)]
    
    for i in range(n - 1):
        a, b = map(int, input().split())
        
    # 부모가 누구인지만 저장    
    par[b] = a
    
    x, y = map(int, input().split())
    
    a = []
    # 조상 리스트 구하기
    # 내가 루트가 아니여도 넣어주기
    # 나를 포함 안 시키려면
    # while par[x] != 0:
    #     x = par[x]
    #     a.append(x)
    while x != 0:
        a.append(x)
        x = par[x]
        
    b = []
    while par[y] != 0:
        y = par[y]
        b.append(y)
            
    idx1 = len(a) - 1
    idx2 = len(b) - 1
    while idx1 >= 0 and idx2 >= 0 and a[idx1] == b[idx2]:
        idx1 -= 1
        idx2 -= 1
        
    print(a[idx1 + 1])
    
    
    
### 트리의 지름
# 아무 노드나 제일 먼 노드를 찾고
# 그 제일 먼 노드에서 제일 멀리 떨어진 노드를 찾으면
# 트리의 지름!



### 이진트리
# 전위 순회
# 중위 순회
# 후위 순회

###  ? -> 무조건 왼쪽-> ? -> 오른쪽 -> ?
## 전위는 맨 앞 ? 에서 출력
## 중위는 가운데 ? 에서 출력
# 후위는 맨 뒤 ? 에서 출력


