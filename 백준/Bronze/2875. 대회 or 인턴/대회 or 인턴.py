n, m, inter = map(int, input().split(' '))

cnt = 0
for i in range(1, 110):
    if 2 * i <= n and i <= m and (n - 2 * i) + (m - i) >= inter:
        cnt += 1
print(cnt)