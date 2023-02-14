import sys
input = lambda : sys.stdin.readline().strip()


def recur(cur, tmp):
    # print(tmp)
    if cur >= n:
        # print(*tmp)
        # return
        print(*tmp)
        exit()
    
    num = int(arr[cur])
    if not visited[num]:
        visited[num] = True
        recur(cur + 1, tmp + [num])
        visited[num] = False


    if cur + 1 < n and int(arr[cur] + arr[cur + 1]) <= m and not visited[int(arr[cur] + arr[cur + 1])]:
        num = int(arr[cur] + arr[cur + 1])
        visited[num] = True
        recur(cur + 2, tmp + [num])
        visited[num] = False


arr = input()
n = len(arr)
m = len(arr) if len(arr) < 10 else 9 + (len(arr) - 9) // 2
visited = [False for _ in range(n + 1)]
visited[0] = True

recur(0, [])
