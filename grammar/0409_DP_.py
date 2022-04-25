# def recur(a, b):
#     ret = False
#
#     if dp[a][b] != -1:
#         return dp[a][b]
#
#     for i in range(3):
#         if a >= arr[i]:
#             if not recur(a - arr[i], b):
#                 ret = True
#         if b >= arr[i]:
#             if not recur(a, b - arr[i]):
#                 ret = True
#
#     return ret
#
# arr = list(map(int, input().split()))
# dp = [[-1 for i in range(510)] for j in range(510)]
#
# for _ in range(5):
#     a, b = map(int, input().split())
#
#     for i in range(a + 1):
#         for j in range(b + 1):
#             dp[i][j] = False
#
#             for k in range(3):
#                 if i >= arr[k] and not dp[i - arr[k]][j]:
#                     dp[i][j] = True
#                 if j >= arr[k] and not dp[i][j - arr[k]]:
#                     dp[i][j] = True
#
#     if dp[a][b]:
#         print('A')
#     else:
#         print('B')

# def recur(cur, cnt, prv):
#     ret = 0
#
#     if cur == n:
#         if cnt == m:
#             return 1
#         else:
#             return 0
#
#     if dp[cur][cnt][prv] != -1:
#         return dp[cur][cnt][prv]
#
#     for i in range(2):
#         ret += recur(cur + 1, cnt + prv * i, i)
#
#     dp[cur][cnt][prv] = ret
#     return ret
#
# t = int(input())
#
# for _ in range(t):
#     n, m = map(int, input().split())
#
#     dp = [[[0 for i in range(2)] for j in range(110)] for k in range(110)]
#
#     for i in range(110):
#         for j in range(2):
#             if i == m:
#                 dp[n][i][j] = 1
#
#     for i in range(n)[::-1]:
#         for j in range(n)[::-1]:
#             for k in range(2):
#                 for l in range(2):
#                     dp[i][j][k] += dp[i + 1][j + k * l][l]
#
#     print(dp[0][0][0])



# n, m = map(int, input().split())
# arr = list(map(int, input().split()))
# dp = [[10000000 for i in range(310)] for j in range(310)]

# dp[0][0] = arr[0]
# for i in range(1, m):
#     dp[i][i] = max(dp[i - 1][i - 1], arr[i])

# for i in range(n):
#     for j in range(0, min(i, m)):
#         total = 0
#         for k in range(j, i + 1)[::-1]:
#             total += arr[k]
#             dp[i][j] = min(dp[i][j], max(dp[k - 1][j - 1], total))

# print(dp[n - 1][m - 1])


n = int(input())
arr = [[0 for i in range(3)]] + [list(map(int, input().split())) for i in range(n)]
dp = [[0 for i in range(3)] for j in range(n + 1)]

for i in range(1, n + 1):
    mn = 1000000
    midx = 0
    for j in range(3):
        if mn > dp[i - 1][j]:
            mn = dp[i - 1][j]
            midx = j

    for j in range(3):
        if j == midx:
            continue

        dp[i][j] = mn + arr[i][j]

    mn = 1000000
    for j in range(3):
        if j == midx:
            continue

        mn = min(mn, dp[i - 1][j])

    dp[i][midx] = mn + arr[i][midx]

print(min(dp[n]))

# n = int(input())
# arr = list(map(int, input().split()))
# dp = [0 for i in range(n)]
#
# for i in range(n):
#     dp[i] = arr[i]
#     for j in range(i):
#         if arr[j] < arr[i]:
#             dp[i] = max(dp[i], dp[j] + arr[i])
#
# print(max(dp))




# n = int(input())
# arr = list(map(int, input().split()))
# dp = [0 for i in range(n)]
# v = [-1000000]
#
# for i in range(n):
#     s = 0
#     e = len(v) - 1
#     idx = 0
#     while s <= e:
#         mid = (s + e) // 2
#
#         if v[mid] < arr[i]:
#             idx = mid
#             s = mid + 1
#         else:
#             e = mid - 1
#
#     if idx == len(v) - 1:
#         v.append(arr[i])
#     else:
#         v[idx + 1] = arr[i]
#
#     dp[i] = idx + 1
#
# print(len(v) - 1)

# a = '#' + input()
# b = '#' + input()
# dp = [[0 for i in range(len(b) + 1)] for j in range(len(a) + 1)]
#
# for i in range(1, len(a)):
#     for j in range(1, len(b)):
#         if a[i] == b[j]:
#             dp[i][j] = dp[i - 1][j - 1] + 1
#         else:
#             dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
#
# print(dp[len(a) - 1][len(b) - 1])


# n = int(input())
# dp = [[0, 0, 0], [0, 0, 0]]
# idx = 0
#
# for i in range(n):
#     arr = list(map(int, input().split()))
#
#     for j in range(3):
#         dp[idx][j] = 0
#
#         for k in range(3):
#             if abs(j - k) >= 2:
#                 continue
#
#             dp[idx][j] = max(dp[idx][j], dp[idx ^ 1][k] + arr[j])
#
#     idx ^= 1
#
# print(max(dp[idx ^ 1]))


# n = int(input())
# arr = list(map(int, input().split()))
# dp = [1 for i in range(n)]
# prv = [-1 for i in range(n)]
#
# for i in range(n):
#     for j in range(i):
#         if arr[j] < arr[i] and dp[j] + 1 > dp[i]:
#             dp[i] = dp[j] + 1
#             prv[i] = j
#
# mx = -1
# idx = -1
# for i in range(n):
#     if mx < dp[i]:
#         mx = dp[i]
#         idx = i
#
# print(mx)
#
# ans = []
# while idx != -1:
#     ans.append(idx)
#     idx = prv[idx]
#
# for i in ans[::-1]:
#     print(arr[i], end=' ')

# a = '#' + input()
# b = '#' + input()
# dp = [[0 for i in range(len(b))] for j in range(len(a))]
# prv = [[[-1, -1] for i in range(len(b))] for j in range(len(a))]
#
# for i in range(1, len(a)):
#     for j in range(1, len(b)):
#         if a[i] == b[j]:
#             dp[i][j] = dp[i - 1][j - 1] + 1
#             prv[i][j] = [i - 1, j - 1]
#         else:
#             if dp[i - 1][j] > dp[i][j - 1]:
#                 dp[i][j] = dp[i - 1][j]
#                 prv[i][j] = [i - 1, j]
#             else:
#                 dp[i][j] = dp[i][j - 1]
#                 prv[i][j] = [i, j - 1]
#
# print(dp[len(a) - 1][len(b) - 1])
#
# x = len(a) - 1
# y = len(b) - 1
# ans = ''
# while x != -1 or y != -1:
#     if prv[x][y][0] == x - 1 and prv[x][y][1] == y - 1:
#         ans += a[x]
#
#     x, y = prv[x][y][0], prv[x][y][1]
#
# print(ans[::-1])

# from collections import deque
#
# n, m = map(int, input().split())
# que = deque()
# visited = [False for i in range(200010)]
# prv = [-1 for i in range(200010)]
#
# d = 0
# visited[n] = True
# que.append(n)
# while len(que) > 0:
#     size = len(que)
#     for _ in range(size):
#         cur = que[0]
#         que.popleft()
#
#         if cur == m:
#             print(d)
#             break
#
#         for nxt in [cur - 1, cur + 1, 2 * cur]:
#             if not (0 <= nxt < 200010) or visited[nxt]:
#                 continue
#
#             que.append(nxt)
#             visited[nxt] = True
#             prv[nxt] = cur
#
#     d += 1
#
# cur = m
# ans = []
# while cur != -1:
#     ans.append(cur)
#     cur = prv[cur]
#
# print(*ans[::-1])




'''
&
|
^
~
<<


|               특정 비트를 킬 때 사용                   x |= 1 << 2
&               특정 비트가 켜져 있는지 확인할때 사용      (x & (1 << 2)) != 0
&               특정 비트를 끌 때 사용                   x &= ~(1 << 2)
^               특정 비트 상태를 반전시킬때 사용           x ^= (1 << 2)
x & (-x)        x의 제일 오른쪽 1이 나온다

-x => ~x + 1

101000011100 1 0000
010111100011 1 0000
01011110001101111
01011110001110000

x가 2의 거듭제곱인지 아닌지 반복문 없이 확인해봐라

(x & (-x)) == x

x = 10010001010101
    00000000000100
    11111111111011

    00000000000100
    00000000000000


'''

# def recur(cur, visit):
#     if cur == n:
#         return 0
#
#     if dp[visit] != -1:
#         return dp[visit]
#
#     ret = 1000000000
#     for i in range(n):
#         # if visited[i]:
#         #     continue
#         if (visit & (1 << i)) != 0:
#             continue
#
#         #visited[i] = True
#         #visit |= 1 << i
#         ret = min(ret, recur(cur + 1, visit | (1 << i)) + arr[cur][i])
#         #visited[i] = False
#         #visit &= ~(1 << i)
#
#     dp[visit] = ret
#     return ret
#
# n = int(input())
# arr = [list(map(int, input().split())) for i in range(n)]
# dp = [-1 for i in range(1 << 20)]
#
# print(recur(0, 0))


from collections import deque

n, m = map(int, input().split())
arr = [list(input()) for i in range(n)]
que = deque()
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
visited = [[[False for i in range(1 << 10)] for j in range(m)] for k in range(n)]

x = 0
y = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == '0':
            x = i
            y = j

d = 0
que.append([x, y, 0])
visited[x][y][0] = True
while len(que) > 0:
    size = len(que)
    for _ in range(size):
        x, y, key = que[0][0], que[0][1], que[0][2]
        que.popleft()

        if arr[x][y] == '1':
            print(d)
            exit()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < n and 0 <= ny < m):
                continue

            nkey = key
            if 'a' <= arr[nx][ny] <='f':
                nkey = key | (1 << (ord(arr[nx][ny]) - ord('a')))
            elif 'A' <= arr[nx][ny] <= 'F':
                if (key & (1 << (ord(arr[nx][ny]) - ord('A')))) == 0:
                    continue
            elif arr[nx][ny] == '#':
                continue

            if visited[nx][ny][nkey]:
                continue

            que.append([nx, ny, nkey])
            visited[nx][ny][nkey] = True

    d += 1

print(-1)