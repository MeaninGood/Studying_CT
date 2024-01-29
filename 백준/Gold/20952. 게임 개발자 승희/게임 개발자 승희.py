import sys
input = lambda : sys.stdin.readline().strip()

n, m = map(int, input().split())
narr = list(map(int, input().split()))
marr = list(map(int, input().split()))

visited = [False for _ in range(7)]
cnt = 0
for i in range(n):
    if not visited[narr[i] % 7]:
        visited[narr[i] % 7] = True
        cnt += 1

    if cnt == 7:
        break

total = 0
chk = 0
for i in range(m):
    tmp = 7 - (chk + marr[i]) % 7 if (chk + marr[i]) % 7 != 0 else 0

    if visited[tmp]:
        if cnt == 1:
            continue
        visited[tmp] = False
        cnt -= 1

    chk = (chk + marr[i]) % 7
    total += marr[i]
    total %= (10**9 + 7)

ans = []
for i in range(n):
    if visited[narr[i] % 7]:
        ans.append((narr[i] + total) % (10**9 + 7))

print(len(ans))
print(*ans)