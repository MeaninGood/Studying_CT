import sys

input = lambda: sys.stdin.readline().strip()

arr = [list(map(int, input().split())) for _ in range(3)]
idxs = []
for i in range(3):
    for j in range(3):
        idxs.append([i, j])


def check_row():
    if sum(arr[0]) == sum(arr[1]) == sum(arr[2]):
        return sum(arr[0])

    return 0


def check_col():
    total = [0, 0, 0]
    for i in range(3):
        for j in range(3):
            total[i] += arr[j][i]

    if total[0] == total[1] == total[2]:
        return total[0]

    return 0


def check_dia():
    sum1 = arr[0][0] + arr[1][1] + arr[2][2]
    sum2 = arr[0][2] + arr[1][1] + arr[2][0]

    if sum1 == sum2:
        return sum1

    return 0


ret = 1 << 31
visited = [False for _ in range(10)]


def recur(cur, total):
    global ret

    if cur == 9:
        if check_row() == check_col() == check_dia() != 0:
            ret = min(ret, total)
        return

    x, y = idxs[cur]
    tmp = arr[x][y]
    for i in range(1, 10):
        if visited[i]:
            continue

        visited[i] = True
        arr[x][y] = i
        recur(cur + 1, total + abs(i - tmp))
        arr[x][y] = tmp
        visited[i] = False


recur(0, 0)
print(ret)
