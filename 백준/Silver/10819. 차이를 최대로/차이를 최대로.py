import sys
input = lambda : sys.stdin.readline().strip()

n = int(input())
arr = list(map(int, input().split()))

visited = [False for _ in range(n)]
ans = 0
def recur(cur, tmp):
    global ans
    if cur == n:
        total = 0
        for i in range(1, n):
            total += abs(tmp[i] - tmp[i - 1])

        ans = max(ans, total)
        return
    
    for i in range(n):
        if visited[i]:
            continue

        visited[i] = True
        recur(cur + 1, tmp + [arr[i]])
        visited[i] = False

recur(0, [])

print(ans)