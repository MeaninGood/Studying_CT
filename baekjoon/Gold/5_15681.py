# 15681번_트리와 쿼리

## 간선에 가중치와 방향성이 없는 임의의 루트 있는 트리가 주어짐
## 정점 U를 루트로 하는 서브트리에 속한 정점의 수를 출력

'''
# 트리의 정점의 수 N과 루트의 번호 R, 쿼리의 수 Q(2 ≤ N ≤ 105, 1 ≤ R ≤ N, 1 ≤ Q ≤ 105)
# 이어 N-1줄에 걸쳐, U V의 형태로 트리에 속한 간선의 정보가 주어짐 (1 ≤ U, V ≤ N, U ≠ V)
# 이는 U와 V를 양 끝점으로 하는 간선이 트리에 속함을 의미
# 이어 Q줄에 걸쳐, 문제에 설명한 U가 하나씩 주어진다. (1 ≤ U ≤ N)
# 입력으로 주어지는 트리는 항상 올바른 트리임이 보장
## Q줄에 걸쳐 각 쿼리의 답을 정수 하나로 출력

(입력)
9 5 3
1 3
4 3
5 4
5 6
6 7
2 3
9 6
6 8
5
4
8

(출력)
9
4
1

'''

# def dfs(cur, prv):
#     sz[cur] = 1
    
#     for nxt in v[cur]:
#         if nxt == prv:
#             continue
        
#         sz[cur] += dfs(nxt, cur)
        
#     return sz[cur]


# n, r, q = map(int, input().split())

# v = [[] for i in range(n + 1)]
# sz = [0 for i in range(n + 1)]
# for i in range(n - 1):
#     a, b = map(int, input().split())
#     v[a].append(b)
#     v[b].append(a)
    
# dfs(r, -100)

# for i in range(q):
#     x = int(input())
    
#     print(sz[x])




def find_(x):
    if par[x] == x:
        return x
    
    return find_(par[x])

def union_(a, b):
    a, b = find_(a), find_(b)
    
    if a == b:
        return
    
    if rnk[a] < rnk[b]:
        par[a] = b
        sz[b] += sz[a]
        
    if rnk[a] > rnk[b]:
        par[b] = a
        sz[a] += sz[b]
    
    else:
        par[b] = a
        sz[a] += sz[b]
        rnk[a] += 1
        
n, r, q = map(int, input().split())

par = [i for i in range(n + 1)]
rnk = [0 for i in range(n + 1)]
sz = [1 for i in range(n + 1)]

v = []
for i in range(n - 1):
    c, d = map(int, input().split())
    
    if c == r:
        union_(c, d)
    else:
        v.append([c, d])
print(v)
for i in range(len(v)):
    e, f = v[i]
    
    union_(e, f)

for i in range(q):
    x = int(input())
    print(sz[x])
























# n, r, q = map(int, input().split())
# v = [[] for i in range(n + 1)]

# for i in range(n - 1):
#     a, b = map(int, input().split())

#     v[a].append(b)
#     v[b].append(a)

# sz = [0 for i in range(n + 1)]

# def dfs(cur, prv):
#     sz[cur] = 1

#     for nxt in v[cur]:
#         if nxt == prv:
#             continue

#         sz[cur] += dfs(nxt, cur)

#     return sz[cur]

# dfs(r, -1)

# for i in range(q):
#     x = int(input())

#     print(sz[x])