'''
이름				                시간복잡도		n제한
순열(백트래킹 1,2번 템플릿)		n!			    8~10
조합(백트래킹 3,4번 템플릿)		2^n			    15~20
3중 for				            n^3			    100~300
2차원 DP				            n^2~n^3			100~1,000, 300~500=>어지간하면 2차원 DP
2중 for				            n^2			    1,000~3,000
정렬, 이진탐색		            nlogn			100,000~200,000
스택, 투포인터			        n			    100,000~1,000,000
'''


# n = int(input())
# m = int(input())
#
# v = [[] for i in range(n + 1)]
#
# for i in range(m):
#     a, b = map(int, input().split())
#
#     v[a].append(b)
#     v[b].append(a)
#
# visited = [False for i in range(n + 1)]
#
# def dfs(cur):
#     cnt = 1
#     visited[cur] = True
#
#     for nxt in v[cur]:
#         if visited[nxt]:
#             continue
#
#         cnt += dfs(nxt)
#
#     return cnt
#
# print(dfs(1) - 1)


# static boolean visited[] = new boolean[1000010];

# void dfs(int cur){
#     visited[cur] = true;
#
#     for(int i = 0; i < v[cur].size(); i++){
#         int nxt = v[cur].get(i);
#
#         if(visited[nxt]) continue;
#
#         dfs(nxt);
#     }
# }

# ArrayList<Integer> v[] = new ArrayList[];
#
# n = sc.nextInt();
#
# for(int i = 0; i < n + 1; i++) v[i] = new ArrayList<>();

# for(int i = 0; i < m; i++){
#     a = sc.nextInt();
#     b = sc.nextInt();
#
#     v[a].add(b);
#     v[b].add(a);
# }





# n, m = map(int, input().split())
# v = [[] for i in range(n + 1)]
#
# for i in range(m):
#     a, b = map(int, input().split())
#
#     v[a].append(b)
#     v[b].append(a)
#
# visited = [False for i in range(n + 1)]
#
# def dfs(cur):
#     visited[cur] = True
#
#     for nxt in v[cur]:
#         if visited[nxt]:
#             continue
#
#         dfs(nxt)
#
# cnt = 0
# for i in range(1, n + 1):
#     if not visited[i]:
#         cnt += 1
#         dfs(i)
#
# print(cnt)



# n, m, k = map(int, input().split())
# arr = [0] + list(map(int, input().split()))
# v = [[] for i in range(n + 1)]
#
# for i in range(m):
#     a, b = map(int, input().split())
#
#     v[a].append(b)
#     v[b].append(a)
#
# visited = [False for i in range(n + 1)]
#
# def dfs(cur):
#     ret = arr[cur]
#     visited[cur] = True
#
#     for nxt in v[cur]:
#         if visited[nxt]:
#             continue
#
#         ret = min(ret, dfs(nxt))
#
#     return ret
#
# ans = 0
# for i in range(1, n + 1):
#     if visited[i]:
#         continue
#
#     ans += dfs(i)
#
# print(ans)





# n = int(input())
# arr = [input() for i in range(n)]
# visited = [[False for i in range(n)] for j in range(n)]
# dx = [1, 0, -1, 0]
# dy = [0, 1, 0, -1]
#
# def in_range(x, y):
#     return 0 <= x < n and 0 <= y < n
#
# def dfs(x, y):
#     ret = 1
#     visited[x][y] = True
#
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#
#         if not in_range(nx, ny) or visited[nx][ny] or arr[nx][ny] != '1':
#             continue
#
#         ret += dfs(nx, ny)
#
#     return ret
#
# cnt = 0
# ans = []
# for i in range(n):
#     for j in range(n):
#         if visited[i][j] or arr[i][j] == '0':
#             continue
#
#         cnt += 1
#         ans.append(dfs(i, j))
#
# ans.sort()
#
# print(cnt)
# for i in ans:
#     print(i)

# 노드 하나 => 정수 하나
# 노드 하나 => 정수 두개(좌표)

# public static boolean in_range(int x, int y){
#     return x >= 0 && x < n && y >= 0 && y < n;
# }


# n = int(input())
# arr = [0] + [int(input()) for i in range(n)]
# visited = [False for i in range(n + 1)]
#
# def dfs(cur, start):
#     visited[cur] = True
#
#     if arr[cur] == start:
#         return True
#
#     if visited[arr[cur]]:
#         return False
#
#     return dfs(arr[cur], start)
#
# cnt = 0
# ans = []
# for i in range(1, n + 1):
#     visited = [False for i in range(n + 1)]
#
#     if dfs(i, i):
#         cnt += 1
#         ans.append(i)
#
# print(cnt)
# for i in ans:
#     print(i)



# from collections import deque
#
# n = int(input())
# m = int(input())
# v = [[] for i in range(n + 1)]
#
# for i in range(m):
#     a, b = map(int, input().split())
#
#     v[a].append(b)
#     v[b].append(a)
#
# que = deque()
# visited = [False for i in range(n + 1)]
#
# que.append(1)
# visited[1] = True
# while len(que) > 0:
#     cur = que[0]
#     que.popleft()
#
#     for nxt in v[cur]:
#         if visited[nxt]:
#             continue
#
#         que.append(nxt)
#         visited[nxt] = True

# import java.util.Queue;
# import java.util.LinkedList;
#
# Queue<Integer> que = new LinkedList<>();
#
# que.add(1);
# visited[1] = true;
# while(!que.isEmpty()){
#     cur = que.poll();
#
#     for(int i = 0; i < v[cur].size(); i++){
#         int nxt = v[cur].get(i);
#
#         if(visited[nxt]) continue;
#
#         que.add(nxt);
#         visited[nxt] = true;
#     }
# }






# from collections import deque
#
# n, m = map(int, input().split())
# que = deque()
# visited = [False for i in range(200010)]
#
# que.append(n)
# visited[n] = True
# d = 0
# while len(que) > 0:
#     size = len(que)
#
#     for _ in range(size):
#         cur = que.popleft()
#
#         if cur == m:
#             print(d)
#             exit()
#
#         for nxt in [cur - 1, cur + 1, 2 * cur]:
#             if not (0 <= nxt < 200010) or visited[nxt]:
#                 continue
#
#             que.append(nxt)
#             visited[nxt] = True
#
#     d += 1




# from collections import deque
#
# n, m = map(int, input().split())
# arr = [input() for i in range(n)]
# dx = [1, 0, -1, 0]
# dy = [0, 1, 0, -1]
#
# def in_range(x, y):
#     return 0 <= x < n and 0 <= y < m
#
# def bfs(x, y):
#     que = deque()
#     visited = [[False for i in range(m)] for j in range(n)]
#
#     d = 0
#     que.append([x, y])
#     visited[x][y] = True
#     while len(que) > 0:
#         size = len(que)
#
#         for _ in range(size):
#             x, y = que[0][0], que[0][1]
#             que.popleft()
#
#             for i in range(4):
#                 nx = x + dx[i]
#                 ny = y + dy[i]
#
#                 if not in_range(nx, ny) or visited[nx][ny] or arr[nx][ny] != 'L':
#                     continue
#
#                 que.append([nx, ny])
#                 visited[nx][ny] = True
#
#         d += 1
#
#     return d - 1
#
# ans = 0
# for i in range(n):
#     for j in range(m):
#         if arr[i][j] == 'L':
#             ans = max(ans, bfs(i, j))
#
# print(ans)


# from collections import deque
#
# n, m = map(int, input().split())
# arr = [input() for i in range(n)]
# visited = [[[False for k in range(3)] for i in range(m)] for j in range(n)]
# dx = [1, 0, -1, 0]
# dy = [0, 1, 0, -1]
# que = deque()
#
# def in_range(x, y):
#     return 0 <= x < n and 0 <= y < m
#
# d = 1
# que.append([0, 0, 0])
# visited[0][0][0] = True
# while len(que) > 0:
#     size = len(que)
#
#     for _ in range(size):
#         x, y, hand = que[0][0], que[0][1], que[0][2]
#         que.popleft()
#
#         if x == n - 1 and y == m - 1:
#             print(d)
#             exit()
#
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#
#             if not in_range(nx, ny):
#                 continue
#
#             nhand = hand + int(arr[nx][ny])
#
#             if nhand > 1 or visited[nx][ny][nhand]:
#                 continue
#
#             que.append([nx, ny, nhand])
#             visited[nx][ny][nhand] = True
#
#     d += 1
#
# print(-1)



# n = int(input())
# v = [[] for i in range(n + 1)]
# par = [0 for i in range(n + 1)]

# for i in range(n - 1):
#     a, b = map(int, input().split())

#     v[a].append(b)
#     v[b].append(a)

# def dfs(cur, prv):
#     par[cur] = prv

#     for nxt in v[cur]:
#         if nxt == prv:
#             continue

#         dfs(nxt, cur)

# dfs(1, -1)

# for i in range(2, n + 1):
#     print(par[i])



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



# t = int(input())

# for _ in range(t):
#     n = int(input())
#     par = [0 for i in range(n + 1)]

#     for i in range(n - 1):
#         a, b = map(int, input().split())

#         par[b] = a

#     x, y = map(int, input().split())

#     a = []
#     while x != 0:
#         a.append(x)
#         x = par[x]

#     b = []
#     while y != 0:
#         b.append(y)
#         y = par[y]

#     idx1 = len(a) - 1
#     idx2 = len(b) - 1
#     while idx1 >= 0 and idx2 >= 0 and a[idx1] == b[idx2]:
#         idx1 -= 1
#         idx2 -= 1

#     print(a[idx1 + 1])


n = int(input())
lft = {}
rgt = {}
for i in range(n):
    a, b, c = map(str, input().split())

    lft[a] = b
    rgt[a] = c


def dfs(cur, option):
    if cur == '.':
        return

    if option == 0:
        print(cur, end='')
    dfs(lft[cur], option)
    if option == 1:
        print(cur, end='')
    dfs(rgt[cur], option)
    if option == 2:
        print(cur, end='')

dfs('A', 0)
print()
dfs('A', 1)
print()
dfs('A', 2)



# n = int(input())
# inorder = list(map(int, input().split()))
# postorder = list(map(int, input().split()))
#
# def inorder(cur):
#     print(inorder[cur])
#
#     inorder()
#     inorder()



# n = int(input())
# lft = [0 for i in range(n + 1)]
# rgt = [0 for i in range(n + 1)]
# depth = [0 for i in range(n + 1)]
# pos = [0 for i in range(n + 1)]
#
# def dfs(cur, prv):
#     if cur == -1:
#         return
#
#     depth[cur] = d
#
#     dfs(lft[cur], d + 1)
#     dfs(rgt[cur], d + 1)
#
# dfs(1, 1)
#
# def inorder(cur):
#     global cnt
#
#     if cur == -1:
#         return
#
#     inorder(lft[cur])
#     pos[cur] = cnt
#     cnt += 1
#     inorder(rgt[cur])




# n = int(input())
# v = [[] for i in range(n + 1)]
# par = [0 for i in range(n + 1)]
# depth = [0 for i in range(n + 1)]
# sz = [0 for i in range(n + 1)]

# for i in range(n - 1):
#     a, b = map(int, input().split())

#     v[a].append(b)
#     v[b].append(a)


# def dfs(cur, prv):
#     sz[cur] = 1

#     for nxt in v[cur]:
#         if nxt == prv:
#             continue

#         depth[nxt] = depth[cur] + 1
#         par[nxt] = cur

#         dfs(nxt, cur)

#         sz[cur] += sz[nxt]


from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
x, y, dir = map(int, input().split())
ex, ey, edir = map(int, input().split())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
change_dir = [0, 1, 3, 0, 2]

x -= 1
y -= 1
dir = change_dir[dir]

ex -= 1
ey -= 1
edir = change_dir[edir]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

que = deque()
visited = [[[False for i in range(5)] for j in range(m)] for i in range(n)]

d = 0
que.append([x, y, dir])
visited[x][y][dir] = True
while len(que) > 0:
    size = len(que)
    for _ in range(size):
        x, y, dir = que[0][0], que[0][1], que[0][2]
        que.popleft()

        if x == ex and y == ey and dir == edir:
            print(d)
            exit()

        for i in range(1, 4):
            nx = x + i * dx[dir]
            ny = y + i * dy[dir]

            if not in_range(nx, ny) or arr[nx][ny] == 1:
                break

            if visited[nx][ny][dir]:
                continue

            que.append([nx, ny, dir])
            visited[nx][ny][dir] = True


        ndir = (dir + 1) % 4
        if not visited[x][y][ndir]:
            que.append([x, y, ndir])
            visited[x][y][ndir] = True

        ndir = (dir + 3) % 4
        if not visited[x][y][ndir]:
            que.append([x, y, ndir])
            visited[x][y][ndir] = True

    d += 1