



n = int(input())
ineq = input().split()
arr = [0 for i in range(n + 1)]
visited = [False for i in range(10)]

# < >
# 0 2 1

# i => i, i + 1

def recur(cur):
    if cur == n + 1:
        for i in range(n):
            if ineq[i] == '<' and arr[i] > arr[i + 1]:
                return
            if ineq[i] == '>' and arr[i] < arr[i + 1]:
                return

        print(*arr)
        return

    for i in range(10)[::-1]:
        if visited[i]:
            continue

        arr[cur] = i
        visited[i] = True
        recur(cur + 1)
        visited[i] = False

recur(0)