n = int(input())
visited = [False for i in range(n)]
visited2 = [False for i in range(3*n)]
visited3 = [False for i in range(3*n)]

answer = 0

def recur(cur):
    global answer

    if cur == n:
        answer += 1
        return

    for i in range(n):
        if visited[i] or visited2[cur + i] or visited3[cur - i + n]:
            continue

        visited[i] = True
        visited2[cur + i] = True
        visited3[cur - i + n] = True
        recur(cur + 1)
        visited[i] = False
        visited2[cur + i] = False
        visited3[cur - i + n] = False

recur(0)

print(answer)