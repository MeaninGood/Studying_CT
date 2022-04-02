'''

오늘 알려드릴 것들은 거의 모두 구현 팁
=> 구현을 최대한 쉽게 하자
=> 개발 관점에서 진짜 안좋은 코드들일 수 있다.
=> 전역변수, 메모리 3~4배

구현 => 구현, 아이디어, 배경지식

시뮬레이션 => 구현

'''

# n, m = map(int, input().split())
# x, y, d = map(int, input().split())
# arr = [list(map(int, input().split())) for i in range(n)]
#
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
#
# cnt = 0
#
# while True:
#     if arr[x][y] == 0:
#         cnt += 1
#
#     arr[x][y] = 2
#
#     flag = False
#     for i in range(4):
#         d = (d + 3) % 4
#
#         nx = x + dx[d]
#         ny = y + dy[d]
#
#         if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
#             flag = True
#             break
#
#     if flag:
#         x += dx[d]
#         y += dy[d]
#     else:
#         nx = x - dx[d]
#         ny = y - dy[d]
#
#         if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 2:
#             x = nx
#             y = ny
#         else:
#             break
#
# print(cnt)


'''
1. 전체적인 설계
2. 쉬운 구현 문제를 빠르게 풀 수 있어야 된다.
'''




'''
삼성 시뮬레이션 문제에서 자주 나오는 컨셉
=> 2차원 평면에서 어떤 객체들이 이동, 소멸, 생성
=> 객체의 위치 등에 대한 정보 어떻게 저장?

1. 2차원 배열을 만들어서 [i][j] 위치에 객체가 있는지? 있다면 그 객체에 대한 정보를 그 위치에 저장.
2. 객체의 정보를 단순히 1차원 배열에 나열해서 저장.

둘을 모두 들고 있자.

1 => 2를 만드는 것은 어렵지 않다.
2 => 1을 만드는 것도 어렵지 않다.



주변 값들을 참조해서 내가 바뀌는 문제
=> 원본 배열은 그대로 두고 값이 바뀌는건 새로운 배열에 적용한 후 원본 배열에 복사
'''

# def get_cloud():
#     global cloud
#
#     cloud = []
#     for i in range(n):
#         for j in range(n):
#             if exist[i][j]:
#                 cloud.append([i, j])
#
# def get_exist():
#     global exist
#
#     exist = [[False for i in range(n)] for j in range(n)]
#     for i in range(len(cloud)):
#         exist[cloud[i][0]][cloud[i][1]] = True
#
# def move(dir, dist):
#     for i in range(len(cloud)):
#         x, y = cloud[i][0], cloud[i][1]
#
#         x = (x + dist * dx[dir] + 100 * n) % n
#         y = (y + dist * dy[dir] + 100 * n) % n
#
#         cloud[i][0] = x
#         cloud[i][1] = y
#
#     get_exist()
#
# def rain():
#     for i in range(n):
#         for j in range(n):
#             if exist[i][j]:
#                 arr[i][j] += 1
#
#     # for i in range(len(cloud)):
#     #     arr[cloud[i][0]][cloud[i][1]] += 1
#
# def water():
#     arr2 = []
#     for i in range(n):
#         arr2.append(arr[i].copy())
#
#     for i in range(n):
#         for j in range(n):
#             if exist[i][j]:
#                 for k in range(4):
#                     nx = i + dx2[k]
#                     ny = j + dy2[k]
#
#                     if 0 <= nx < n and 0 <= ny < n and arr2[nx][ny] > 0:
#                         arr[i][j] += 1
#
# def make_cloud():
#     global cloud
#
#     cloud = []
#     for i in range(n):
#         for j in range(n):
#             if not exist[i][j] and arr[i][j] >= 2:
#                 arr[i][j] -= 2
#                 cloud.append([i, j])
#
#     get_exist()
#
#
# n, m = map(int, input().split())
# arr = [list(map(int, input().split())) for i in range(n)]
# exist = [[False for i in range(n)] for j in range(n)]
# cloud = [[n - 1, 0], [n - 1, 1], [n - 2, 0], [n - 2, 1]]
# dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
# dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]
# dx2 = [-1, -1, 1, 1]
# dy2 = [-1, 1, -1, 1]
#
# get_exist()
#
# for i in range(m):
#     dir, dist = map(int, input().split())
#
#     move(dir, dist)
#     rain()
#     water()
#     make_cloud()
#
# ans = 0
# for i in range(n):
#     for j in range(n):
#         ans += arr[i][j]
#
# print(ans)





'''
미는게 나오면 밀지 말고 반대쪽에서 당겨오자.

x = arr[8]
for i in range(7)[::-1]:
    arr[i + 1] = arr[i]
arr[0] = x

0   1   2   3   4   5   6   7   8
a   b   c   d   e   f   g   h   i

i   a   b   c   d   e   f   g   h
'''




'''
오른쪽, 아래, 왼쪽, 위 네 방향에 대한 처리가 복잡하게 나오는 경우

아래로 이동하는 것만 구현
맵 전체를 회전


0   1   2   3
4   5   6   7
8   9   10  11


8   4   0
9   5   1
10  6   2
11  7   3


arr[0][0] <= arr[n - 1][0]
arr[0][1] <= arr[n - 2][0]
arr[0][2] <= arr[n - 3][0]
arr[1][0] <= arr[n - 1][1]

arr[i][j] <= arr[m - 1 - j][i]



1. 이전 방향이랑 같은 방향 혹은 반대 방향은 볼 필요 없다.
2. check에서 not r and b만 봤는데, not r or not b 상황도 본다.
3. 방문처리 하면서 BFS

'''

def rotate():
    global n, m, arr

    n, m = m, n
    arr2 = [[0 for i in range(m)] for j in range(n)]

    for i in range(n):
        for j in range(m):
            arr2[i][j] = arr[m - 1 - j][i]

    arr = []
    for i in range(n):
        arr.append(arr2[i].copy())

def move():
    rx, ry = 0, 0
    bx, by = 0, 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'R':
                arr[i][j] = '.'
                rx, ry = i, j
            elif arr[i][j] == 'B':
                arr[i][j] = '.'
                bx, by = i, j

    if rx >= bx:
        while rx < n and arr[rx][ry] == '.':
            rx += 1

        if not (rx < n and arr[rx][ry] == 'O'):
            arr[rx - 1][ry] = 'R'

        while bx < n and arr[bx][by] == '.':
            bx += 1

        if not (bx < n and arr[bx][by] == 'O'):
            arr[bx - 1][by] = 'B'
    else:
        while bx < n and arr[bx][by] == '.':
            bx += 1

        if not (bx < n and arr[bx][by] == 'O'):
            arr[bx - 1][by] = 'B'

        while rx < n and arr[rx][ry] == '.':
            rx += 1

        if not (rx < n and arr[rx][ry] == 'O'):
            arr[rx - 1][ry] = 'R'

def check():
    r = False
    b = False

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'R':
                r = True
            elif arr[i][j] == 'B':
                b = True

    if not r and b:
        return 1
    elif not r or not b:
        return -1
    else:
        return 0

def recur(cur):
    global ans

    flag = check()
    if flag == 1:
        ans = min(ans, cur)
        return
    elif flag == -1:
        return

    if cur == 10:
        return

    for i in range(4):
        arr2 = []
        for i in range(n):
            arr2.append(arr[i].copy())

        move()
        recur(cur + 1)

        for i in range(n):
            arr[i] = arr2[i].copy()

        rotate()


n, m = map(int, input().split())
arr = [list(input()) for i in range(n)]

ans = 1000

recur(0)

if ans == 1000:
    ans = -1

print(ans)