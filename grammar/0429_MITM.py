# n = int(input())
# arr = [[] for i in range(4)]
#
# for i in range(n):
#     a, b, c, d = map(int, input().split())
#
#     arr[0].append(a)
#     arr[1].append(b)
#     arr[2].append(c)
#     arr[3].append(d)
#
# v = [[] for i in range(2)]
#
# for i in range(n):
#     for j in range(n):
#         v[0].append(arr[0][i] + arr[1][j])
#         v[1].append(arr[2][i] + arr[3][j])
#
# v[0].sort()
# v[1].sort()
#
# # s = 0
# # e = len(v[1]) - 1
# # cnt = 0
# # while s < len(v[0]) and e >= 0:
# #     if v[0][s] + v[1][e] == 0:
# #         temp = v[0][s]
# #         x = 0
# #         while s < len(v[0]) and v[0][s] == temp:
# #             x += 1
# #             s += 1
# #
# #         temp = v[1][e]
# #         y = 0
# #         while e >= 0 and v[1][e] == temp:
# #             y += 1
# #             e -= 1
# #
# #         cnt += x * y
# #     elif v[0][s] + v[1][e] < 0:
# #         s += 1
# #     else:
# #         e -= 1
#
# cnt = 0
# for i in v[0]:
#     l = 1
#     r = 0
#
#     s = 0
#     e = len(v[1]) - 1
#     while s <= e:
#         mid = (s + e) // 2
#
#         if v[1][mid] >= -i:
#             l = mid
#             e = mid - 1
#         else:
#             s = mid + 1
#
#     s = 0
#     e = len(v[1]) - 1
#     while s <= e:
#         mid = (s + e) // 2
#
#         if v[1][mid] <= -i:
#             r = mid
#             s = mid + 1
#         else:
#             e = mid - 1
#
#     cnt += r - l + 1
#
# print(cnt)
#



# n, m = map(int, input().split())
# arr = list(map(int, input().split()))
# v = [[] for i in range(2)]
#
# def recur(cur, total, idx, e):
#     if cur == e:
#         v[idx].append(total)
#         return
#
#     recur(cur + 1, total + arr[cur], idx, e)
#     recur(cur + 1, total, idx, e)
#
# recur(0, 0, 0, n // 2)
# recur(n // 2, 0, 1, n)




# n = int(input())
# s = '#' + input() + '#'
# w = [0 for i in range(n + 2)]
# e = [0 for i in range(n + 2)]
#
# for i in range(1, n + 1):
#     w[i] = w[i - 1] + (s[i] == 'W')
#
# for i in range(1, n + 1)[::-1]:
#     e[i] = e[i + 1] + (s[i] == 'E')
#
# ans = 0
# for i in range(1, n + 1):
#     if s[i] == 'H':
#         ans += w[i] * ((pow(2, e[i], 1000000007) - e[i] - 1 + 1000000007) % 1000000007)
#         ans %= 1000000007
#
# print(ans)


# n = int(input())
# arr = [list(map(int, input().split())) for i in range(n)]
# visited = [[False for i in range(3 * n)] for j in range(2)]
# ans = 0
#
# def recur(x, y, cnt):
#     global ans
#
#     if y == n:
#         x += 1
#         y = 0
#     if x == n:
#         ans = max(ans, cnt)
#         return
#
#     if arr[x][y] == 1 and not visited[0][x + y] and not visited[1][x - y]:
#         visited[0][x + y] = True
#         visited[1][x - y] = True
#         recur(x, y + 2, cnt + 1)
#         visited[0][x + y] = False
#         visited[1][x - y] = False
#
#     recur(x, y + 2, cnt)
#
# recur(0, 0, 0)
# recur(0, 1, 0)
#
# print(ans)



# def dfs(cur):
#     if cycle[cur] != -1:
#         return -1
#
#     if visited[cur]:
#         return cur
#
#     visited[cur] = True
#
#     ret = dfs(arr[cur])
#
#     if ret == -1:
#         cycle[cur] = 0
#         return -1
#
#     cycle[cur] = 1
#     if cur == ret:
#         ret = -1
#
#     return ret
#
# t = int(input())
#
# for _ in range(t):
#     n = int(input())
#     arr = [0] + list(map(int, input().split()))
#     visited = [False for i in range(n + 1)]
#     cycle = [-1 for i in range(n + 1)]
#
#     for i in range(1, n + 1):
#         if not visited[i]:
#             dfs(i)
#
#     cnt = 0
#     for i in range(1, n + 1):
#         if cycle[i] == 0:
#             cnt += 1
#
#     print(cnt)


def dfs(cur):
    visited[cur] = True

    for nxt in v[cur]:
        if visited[nxt]:
            continue

        dfs(nxt)

    st.append(cur)

# def dfs2(cur):
#     visited[cur] = True
#
#     for nxt in v[cur]:
#         if visited[nxt]:
#             continue
#
#         dfs2(nxt)

def rdfs(cur):
    visited[cur] = True

    for nxt in rv[cur]:
        if visited[nxt]:
            continue

        rdfs(nxt)

n, m = map(int, input().split())
v = [[] for i in range(n + 1)]
rv = [[] for i in range(n + 1)]
visited = [False for i in range(n + 1)]
st = []

for i in range(m):
    a, b = map(int, input().split())

    v[a].append(b)
    rv[b].append(a)

for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)

cnt = 0
visited = [False for i in range(n + 1)]
while len(st) > 0:
    if not visited[st[-1]]:
        rdfs(st[-1])
        cnt += 1

    st.pop()

print(cnt)

#코사라주 알고리즘


# cnt = 0
# visited = [False for i in range(n + 1)]
# while len(st) > 0:
#     if not visited[st[-1]]:
#         dfs2(st[-1])
#         cnt += 1
#
#     st.pop()
#
# print(cnt)